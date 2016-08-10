from _json import make_encoder
from builtins import property

from django.db import models
from core import thumnails
import os


# Create your models here.

TYPES_OF_GOODS = ((0, 'Двери'), (1, 'Акссесуары'))

class TypesOfGoods(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'

    def __str__(self):
        return str(self.name)

class Countries(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return str(self.name)

class Goods(models.Model):
    article = models.CharField('Артикул',max_length=50)
    name = models.CharField('Название', max_length=150)
    desc = models.TextField('Описание',null=True, blank=True)
    type = models.ForeignKey(TypesOfGoods, verbose_name='Тип товара')
    foto = models.ImageField('Фото', upload_to='goods_foto')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s - %s' % (self.article, self.name)

    def save(self, force_insert=False, force_update=False, using=None):
        try:
            obj = Goods.objects.get(id=self.id)
            print(obj)
            if obj and (obj.foto.path != self.foto.path):
                thumnails.delete_thumbnail(obj.foto.path)
        except:
            pass

        super(Goods, self).save()
        thumnails.make_thumbnail(self.foto.path)

    @property
    def thumnail_img(self):
        img_url = self.foto.url
        thumnail_url = thumnails.getThumbnail(img_url, False)
        return thumnail_url if os.path.exists(thumnails.getThumbnail(self.foto.path)) else img_url

    def delete(self, using=None):
        try:
            obj = Goods.objects.get(id=self.id)
            thumnails.delete_thumbnail(obj.foto.path)
            obj.foto.delete()
        except (Goods.DoesNotExist, ValueError):
            pass
        super(Goods, self).delete()


class Colors(models.Model):
    name = models.CharField('Цвет', max_length=150)
    image = models.ImageField('Фото', upload_to='colors_foto')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):
        try:
            obj = Colors.objects.get(id=self.id)
            print(obj)
            if obj and (obj.image.path != self.image.path):
                thumnails.delete_thumbnail(obj.image.path)
        except:
            pass

        super(Colors, self).save()
        thumnails.make_thumbnail(self.image.path)

    def delete(self, using=None):
        try:
            obj = Colors.objects.get(id=self.id)
            thumnails.delete_thumbnail(obj.image.path)
            obj.image.delete()
        except (Colors.DoesNotExist, ValueError):
            pass
        super(Colors, self).delete()

class GoodsColors(models.Model):
    good = models.ForeignKey(Goods, verbose_name='Товар', related_name='goods_colors')
    color = models.ForeignKey(Colors, verbose_name='Цвет', null = True, blank = True)

    class Meta:
        verbose_name = 'Товар с цветом'
        verbose_name_plural = 'Товары с цветами'

    def __str__(self):
        return '%s - %s' % (str(self.good), self.color.name)

class Properties(models.Model):
    name = models.CharField('Имя', max_length=150)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ('name', )

    def __str__(self):
        return str(self.name)

class Values(models.Model):
    good_property = models.ForeignKey(Properties, verbose_name="Свойство", related_name="property_values")
    value = models.CharField('Значение', max_length=150)

    class Meta:
        verbose_name = 'Значения свойств'
        verbose_name_plural = 'Значение свойства'

    def __str__(self):
        return "%s - %s" % (str(self.good_property), self.value)

class GoodsProperties(models.Model):
    good = models.ForeignKey(Goods, verbose_name='Товар', related_name='goods_properties')
    value = models.ForeignKey(Values, verbose_name="Значение свойства", related_name='good_value')

    class Meta:
        verbose_name = 'Свойство товара'
        verbose_name_plural = 'Свойства товаров'
        ordering = ('value',)

    def __str__(self):
        return "%s - %s" % (str(self.good), self.value)

