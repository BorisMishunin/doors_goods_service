from doors_goods_service.serializers import  GoodsSerializer
from doors_goods_service.models import Goods, Countries, Values, Properties
from rest_framework import generics, viewsets
from rest_framework import filters


class GoodsList(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer



