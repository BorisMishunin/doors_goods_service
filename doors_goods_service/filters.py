# -*- coding: utf-8 -*-

import django_filters
from models import Goods

def get_filter_func(field, lookup_expr='contains'):
    def json_field_method(self, queryset, value):
        if value:
            lookup = '__'.join([field, lookup_expr])
            return queryset.filter(**{lookup: value})
        return queryset

    return json_field_method



class GoodsFilter(django_filters.FilterSet):

    info_contains = django_filters.MethodFilter()
    colors_overlap = django_filters.MethodFilter()

    filter_info_contains = get_filter_func('info')
    filter_colors_overlap = get_filter_func('colors', lookup_expr='overlap')

    class Meta:
        model = Goods
        fields = ['type', 'info_contains', 'colors_overlap']
