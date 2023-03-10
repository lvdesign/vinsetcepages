"""vinsetcepages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap # new sitemap
from django.contrib.sitemaps.views import sitemap # new sitemap
from django.urls import path,include
from django.views.generic.base import TemplateView # new

from django.conf import settings
from django.conf.urls.static import static

from vins.models import Vin # sitemap
info_dict = {
    'queryset': Vin.objects.all(),
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),  # new
    path('accounts/', include('django.contrib.auth.urls')),
    ]

urlpatterns += [
    path('vins/', include('vins.urls', namespace='vins')),
    path('', include('pages.urls')),
]

urlpatterns += [
     path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns +=[
    path('sitemap.xml', sitemap,  # new
        {'sitemaps' : {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name = 'django.contrib.sitemaps.views.sitemap'),
]

urlpatterns +=[
    path('basicSW-vin.js', TemplateView.as_view(template_name='basicSW-vin.js', content_type='application/javascript'),
    name='basicSW-vin.js',
    ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)