from django.contrib import admin
from doors_goods_service.models import Colors, Goods, Countries, TypesOfGoods, Values,  Properties
# Register your models here.


class ColorsAdmin(admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name',)

class GoodsPropertiesAdmin(admin.ModelAdmin):
    ordering = ('good', )
    search_fields = ('good',)
    filter = ('good',)

admin.site.register(Colors, ColorsAdmin)
admin.site.register(Goods)
admin.site.register(Countries)
admin.site.register(TypesOfGoods)
admin.site.register(Values)
admin.site.register(Properties)