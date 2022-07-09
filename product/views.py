from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Reseller, Item, Article
from django.utils import timezone

from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Min

from .utils import currency_in_indian_format, date_last_modified_static

from django.views.decorators.http import last_modified

# Create your views here.

def home(request):
    return render(request, 'home.html')

@last_modified(lambda request: date_last_modified_static(request, 'product', 'about.html'))
def about(request):
    return render(request, 'about.html')

def viewMac(request, slug):
    product, items = viewProduct(slug)
    return render(request, 'product/view.html', { 'product': product, 'items' : items })

def viewAllMacs(request, **kwargs):        
    products, article, paginator, page_number, page_obj = viewAllProducts(request, 'mac', **kwargs)
    return render(request, 'product/mac.html', { 'page_obj': page_obj, 'article': article })

def viewiPhone(request, slug):
    product, items = viewProduct(slug)
    return render(request, 'product/view.html', { 'product': product, 'items' : items })

def viewAlliPhones(request):
    products, article, paginator, page_number, page_obj = viewAllProducts(request, 'iphone')
    return render(request, 'product/iphone.html', { 'page_obj': page_obj, 'article': article })

def viewiPad(request, slug):
    product, items = viewProduct(slug)
    return render(request, 'product/view.html', { 'product': product, 'items' : items })

def viewAlliPads(request):
    products, article, paginator, page_number, page_obj = viewAllProducts(request, 'ipad')
    return render(request, 'product/ipad.html', { 'page_obj': page_obj })    

def viewWatch(request, slug):
    product, items = viewProduct(slug)
    return render(request, 'product/view.html', { 'product': product, 'items' : items })

def viewAllWatches(request):
    products, article, paginator, page_number, page_obj = viewAllProducts(request, 'watch')
    return render(request, 'product/watch.html', { 'page_obj': page_obj })    

def viewReseller(request, slug):    
    return render(request, 'reseller.html')

def viewResellers(request):  
    resellers = Reseller.objects.all()
    return render(request, 'resellers.html', { 'resellers' : resellers })    

def viewService(request):  
    resellers = Reseller.objects.all()
    return render(request, 'service.html', { 'resellers' : resellers })    

def viewAllProducts(request, typeOfProduct, **kwargs):

    if typeOfProduct == 'mac':
        
        if kwargs.get('type') == 'air':
            query = Q(type='MBA')
        elif kwargs.get('type') == 'pro':
            query = Q(type='MBP')
        else:
            query = Q(type='MBP') | Q(type='MBA') | Q(type='iMAC') | Q(type='iMACPRO') | Q(type='MINI') | Q(type='MACPRO')
            query = Q(type__in=['MBA', 'MBP', 'iMAC', 'iMACPRO', 'MINI', 'MACPRO']) # Either one works

        article_query = Q(product__in=['MBA', 'MBP', 'iMAC', 'iMACPRO', 'MINI', 'MACPRO'])

    elif typeOfProduct == 'iphone':
        query = Q(type__in=['iPHONE'])
        article_query = Q(product__in=['iPHONE'])
        
    elif typeOfProduct == 'ipad':
        query = Q(type__in=['iPADPRO', 'iPADAIR', 'iPADMINI', 'iPAD'])
        article_query = Q(product__in=['iPADPRO', 'iPADAIR', 'iPADMINI', 'iPAD'])

    elif typeOfProduct == 'watch':
        query = Q(type__in=['WATCH'])
        article_query = Q(product__in=['WATCH'])

    products = Product.objects.all().filter(query).annotate(minimal_price=Min('item__price')).order_by('-year')
    
    # article = Article.objects.all().filter(article_query).order_by('pub_date')[0]
    try:
        article = Article.objects.filter(article_query).latest('pub_date')
        # print("article : ", article.source)
    except Article.DoesNotExist:
        article = {}
    print("article : ", article)
    
    # article = Article.objects.last().filter(article_query)

    for product in products:
        product.price_locale = "₹{}".format(currency_in_indian_format(product.minimal_price))[:-3]

    paginator = Paginator(products, 25)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return (products, article, paginator, page_number, page_obj)

def viewProduct(slug):
    product = get_object_or_404(Product, slug=slug)
    # print(product.image.url)
    items = Item.objects.filter(product_id=product.id, active=True).order_by('price')
    
    # print("INR {}".format(product.utils.currency_in_indian_format(n)))  # INR 12,00,000.00

    for item in items:
        item.price_locale = "₹{}".format(currency_in_indian_format(item.price))[:-3]

    return (product, items)
