from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from site_parser.models import Article
from site_parser.parse_and_write_to_db import parse


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    """
    Панель администратора для модели Article.
    change_list_template, get_urls и start_parsing
    используются для возможности производить парсинг
    с административной панели.
    """

    list_display = ('id', 'title', 'created')
    change_list_template = "admin/model_change_list.html"  # шаблон для кнопки парсинга

    def get_urls(self):

        """ Создание url-а по которому будет начинаться парсинг """

        urls = super().get_urls()
        my_urls = [
            path('parsing/', self.start_parsing),
        ]
        return my_urls + urls

    def start_parsing(self, request):

        """ Метод для старта парсинга """

        parse()
        return HttpResponseRedirect("../")
