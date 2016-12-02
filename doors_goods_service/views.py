# -*- coding: utf-8 -*-

from doors_goods_service.serializers import  GoodsSerializer, TypesOfGoodsSerializer
from doors_goods_service.models import Goods, TypesOfGoods, Properties
from rest_framework import viewsets

from filters import GoodsFilter


class GoodsList(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_class = GoodsFilter

class TypesOfGoodsList(viewsets.ModelViewSet):
    queryset = TypesOfGoods.objects.all()
    serializer_class = TypesOfGoodsSerializer




