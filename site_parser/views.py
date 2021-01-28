import logging

from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from site_parser.models import Article
from .pagination import ArticlesPagination
from .serializers import ArticleSerializer

logger = logging.getLogger(__name__)


class ArticlesList(ListAPIView):

    """ ListAPIView для модели Article"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'title', 'created']
    pagination_class = ArticlesPagination

    def get(self, request, *args, **kwargs):
        logger.info('Предоставление API (ArticleList)')
        return self.list(request, *args, **kwargs)
