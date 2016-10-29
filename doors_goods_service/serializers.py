# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from doors_goods_service.models import Goods, Countries, Values, Properties
from rest_framework import serializers



class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        #fields = ['type', 'name', 'properties']




