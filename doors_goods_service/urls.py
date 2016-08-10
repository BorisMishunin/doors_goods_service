
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from web_api import views

urlpatterns = [
    url(r'^load_goods/$', 'web.views.loadGoods'),
    url(r'^goods/$', views.GoodsList.as_view()),
    url(r'^goods/(?P<pk>[0-9]+)$', views.GoodsDetail.as_view()),
    url(r'^goods_colors/$', views.GoodsColorsList.as_view()),
    url(r'^goods_colors/(?P<pk>[0-9]+)/$', views.GoodsColorDetail.as_view()),
    url(r'^actions/$', views.ActionsList.as_view()),
    url(r'^countries/$', views.CountriesList.as_view()),
    url(r'^goods_properties/$', views.GoodsPropertiesList.as_view()),
    url(r'^properties/$', views.PropertiesList.as_view()),
    url(r'^values/$', views.ValuesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)