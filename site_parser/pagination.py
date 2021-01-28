from rest_framework.pagination import LimitOffsetPagination, _positive_int
from rest_framework.response import Response


class ArticlesPagination(LimitOffsetPagination):

    """ Пагинатор для модели Article """

    default_limit = 5

    def get_paginated_response(self, data):
        response = Response(data)
        return response
