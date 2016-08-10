from django.contrib import admin

from web_api.models import Colors, Goods, GoodsColors, Countries, TypesOfGoods, Values, GoodsProperties, Properties


# Register your models here.

class GoodsInlines(admin.StackedInline):
    model = GoodsColors
    extra = 3

class GoodsPropertiesInlines(admin.StackedInline):
    model = GoodsProperties
    extra = 3

class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsInlines, GoodsPropertiesInlines]

class ColorsAdmin(admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name',)

class GoodsPropertiesAdmin(admin.ModelAdmin):
    ordering = ('good', )
    search_fields = ('good',)
    filter = ('good',)

admin.site.register(Colors, ColorsAdmin)
admin.site.register(GoodsColors)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Countries)
admin.site.register(TypesOfGoods)
admin.site.register(Values)
admin.site.register(GoodsProperties, GoodsPropertiesAdmin)
admin.site.register(Properties)