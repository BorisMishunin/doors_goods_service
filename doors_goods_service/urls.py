# -*- coding: utf-8 -*-

"""teeest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from doors_goods_service.views import (
    GoodsList, TypesOfGoodsList
)


admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'/goods', GoodsList)
router.register(r'/goods_type', TypesOfGoodsList)


urlpatterns = [
    url(r'^resources', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')),

]

#urlpatterns = format_suffix_patterns(urlpatterns)

