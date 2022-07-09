"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from product import views

urlpatterns = [
    path('backend/', admin.site.urls),
    
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),    
    
    path('mac/air/', views.viewAllMacs, kwargs = { 'type': 'air' }, name = 'viewAllMacAir'),
    path('mac/pro/', views.viewAllMacs, kwargs = { 'type': 'pro' }, name = 'viewAllMacPro'),
    path('mac', views.viewAllMacs, name = 'viewAllMacs'),
    path('mac/<slug:slug>/', views.viewMac, name = 'viewMac'),    

    path('iphone/<slug:slug>/', views.viewiPhone, name = 'viewiPhone'),
    path('iphone', views.viewAlliPhones, name = 'viewAlliPhones'),
    
    path('ipad/<slug:slug>/', views.viewiPad, name = 'viewiPad'),
    path('ipad', views.viewAlliPads, name = 'viewAlliPads'),

    path('watch/<slug:slug>/', views.viewWatch, name = 'viewWatch'),
    path('watch', views.viewAllWatches, name = 'viewAllWatches'),

    path('reseller/<slug:slug>/', views.viewReseller, name = 'viewReseller'),
    path('resellers', views.viewResellers, name = 'viewResellers'),
    
    path('service', views.viewService, name = 'viewService'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)