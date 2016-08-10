from rest_framework import serializers

from sales.models import Actions
from web_api.models import GoodsColors, Goods, Countries, GoodsProperties, Values, Properties


class ValuesSerializer(serializers.ModelSerializer):
    good_property = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Values
        fields = '__all__'

class PropertiesSerializer(serializers.ModelSerializer):
    property_values = ValuesSerializer(many=True)
    class Meta:
        model = Properties
        fields = '__all__'

class GoodsPropertiesSerializer(serializers.ModelSerializer):
    property = serializers.ReadOnlyField(source='value.good_property.name')
    value = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='value'
     )
    class Meta:
        model = GoodsProperties
        fields = '__all__'

class GoodsColorsSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = GoodsColors
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    goods_colors = GoodsColorsSerializer(many=True)
    goods_properties = GoodsPropertiesSerializer(many=True)
    thumnail_foto = serializers.CharField(source='thumnail_img')
    class Meta:
        model = Goods
        fields = '__all__'

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
