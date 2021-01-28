from django.db import models


class Article(models.Model):

    """ Модель спарсенных статей """

    title = models.CharField('название', max_length=255, unique=True)
    url = models.CharField('ссылка', max_length=2000)
    created = models.DateTimeField('создано', auto_now=True)

    def __str__(self):
        return f'Статья: {self.title}'

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'статьи'

