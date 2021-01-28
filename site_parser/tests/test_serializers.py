from django.test import TestCase
from site_parser.serializers import ArticleSerializer
from site_parser.models import Article


class ArticleSerializerTestCase(TestCase):

    """ Тестирует сериализатор ArticleSerializer """

    def test_serializer(self):

        post_0 = Article.objects.create(title='post#0', url="url0")
        post_1 = Article.objects.create(title='post#1', url="url1")

        data = ArticleSerializer([post_0, post_1], many=True).data

        excepted_data = [
            {
                'id': post_0.id,
                'title': 'post#0',
                'url': 'url0',
                'created': post_0.created.isoformat().replace('+00:00', 'Z'),
            },
            {
                'id': post_1.id,
                'title': 'post#1',
                'url': 'url1',
                'created': post_1.created.isoformat().replace('+00:00', 'Z'),
            }
        ]
        self.assertEqual(excepted_data, data)