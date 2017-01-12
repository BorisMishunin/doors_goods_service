# -*- coding: utf-8 -*-

from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100