# -*- coding: utf-8 -*-

from _json import make_encoder

from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.postgres.fields import ArrayField
from utils import thumnails
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
    article = models.CharField('Артикул', max_length=50)
    name = models.CharField('Название', max_length=150)
    desc = models.TextField('Описание', null=True, blank=True)
    type = models.ForeignKey(TypesOfGoods, verbose_name='Тип товара')
    foto = JSONField('Фото', default={})
    properties = JSONField('Свойства товара', default={})
    colors = ArrayField(models.IntegerField(), verbose_name='Цвета', default=[])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return '%s - %s' % (self.article, self.name)



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


class Properties(models.Model):
    name = models.CharField('Имя', max_length=150)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ('name',)

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


