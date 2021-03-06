# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from doors_goods_service.models import Goods, TypesOfGoods, Properties
from rest_framework import serializers
import json

class WritableJSONField(serializers.Field):
    def to_representation(self, obj):
        return json.loads(obj)

    def to_internal_value(self, data):
        return json.dumps(data)

class GoodsSerializer(serializers.ModelSerializer):
    info = WritableJSONField(required=False)
    class Meta:
        model = Goods
        partial=True
        fields = "__all__"

class TypesOfGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesOfGoods
        partial=True
        fields = "__all__"


