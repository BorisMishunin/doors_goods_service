# -*- coding: utf-8 -*-

from doors_goods_service.serializers import  GoodsSerializer
from doors_goods_service.models import Goods, Countries, Values, Properties
from rest_framework import generics, viewsets, VERSION
from rest_framework.decorators import list_route
from rest_framework.response import Response
#from rest_framework import filters

from filters import GoodsFilter


class GoodsList(viewsets.ModelViewSet):

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_class = GoodsFilter

    @list_route(methods=['get'])
    def get_ads(self, request, pk=None):
        with open('/home/boris/develop/dev0/goors_buildout/var/log/teeeeeeeeeest', 'a') as f:
            f.write(str(VERSION) + '\n')
        market_items = Goods.objects.all()[0].info
        data = market_items
        return Response(data)




