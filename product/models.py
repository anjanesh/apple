from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

class TypeOfComputer(models.TextChoices):
    MacBookPro = 'MBP', _('MacBook Pro')
    MacBookAir = 'MBA', _('MacBook Air')
    iMac = 'iMAC', _('iMac')
    iMacPro = 'iMACPRO', _('iMac Pro')
    MacMini = 'MINI', _('Mac Mini')
    MacPro = 'MACPRO', _('Mac Pro')
    iPhone = 'iPHONE', _('iPhone')
    iPadPro = 'iPADPRO', _('iPad Pro')
    iPadAir = 'iPADAIR', _('iPad Air')
    iPadMini = 'iPADMINI', _('iPad Mini')
    iPad = 'iPAD', _('iPad')
    watch = 'WATCH', _('watch')

# Create your models here.
class Product(models.Model):        

    type = models.CharField(
        max_length=10,
        choices=TypeOfComputer.choices,
        default=TypeOfComputer.MacBookPro,
    )
    
    title = models.CharField(max_length=250)
    description = models.TextField()    
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=10)
    storage = models.CharField(max_length=10)
    ram = models.CharField(max_length=10, blank=True)
    screen = models.CharField(max_length=10)    
    image = models.ImageField(upload_to='product/images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    # https://stackoverflow.com/a/11993818/126833
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class Reseller(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    logo = models.ImageField(upload_to='reseller/', blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=False)

    def __str__(self):
        return self.name

class ServiceCenter(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)        
    price = models.PositiveIntegerField(default=0)
    offers = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500, blank=True)
    last_updated = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-last_updated']

    def __str__(self):
        return self.product.title + ' - ' + self.reseller.name + ' : ' + str(self.price)


class Article(models.Model):

    product = models.CharField(
        max_length=10,
        choices=TypeOfComputer.choices,
        default=TypeOfComputer.MacBookPro,
        null=True, blank=True
    )    
    
    class TypeOfArticle(models.TextChoices):
        News = 'News', _('News')
        Rumour = 'Rumour', _('Rumour')
        Announcement = 'Announcement', _('Announcement')

    type = models.CharField(
        max_length=12,
        choices=TypeOfArticle.choices,
        default=TypeOfArticle.News,
    )

    title = models.CharField(max_length=250)
    summary = models.TextField(default='', null=True, blank=True)
    source = models.CharField(max_length=255, null=False, blank=False)
    source_url = models.URLField(max_length=255)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    # https://stackoverflow.com/a/11993818/126833
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
