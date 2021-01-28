from django.urls import reverse
from rest_framework.test import APITestCase

from site_parser.models import Article


class ArticlesApiTestCase(APITestCase):

    """

        Тестирует работу API
         1)limit
         2)offset
         3)ordered

    """
    def setUp(self):

        """ Создает тестовые данные """

        [Article.objects.create(title=f"post:{i}", url=f"url {i}") for i in range(20)]

    def test_get_200_OK(self):

        """ Проверяет подключение к API """

        url = reverse('posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_data_default_settings(self):

        """ Проверяет количество отображаемых постов без заданных параметров """

        url = reverse('posts')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 5)

    def test_get_limit_0(self):

        """ Проверяет работоспособность limit """

        url = reverse('posts')
        response = self.client.get(url, {'limit': 2})
        self.assertEqual(len(response.data), 2)

    def test_get_limit_1(self):

        """ В случае если постов меньше чем limit возвращает все посты"""

        url = reverse('posts')
        response = self.client.get(url, {'limit': 25})
        self.assertEqual(len(response.data), 20)

    def test_get_offset(self):

        """ Проверяет работоспособность offset """

        url = reverse('posts')
        response = self.client.get(url, {'offset': 1})
        self.assertEqual(response.data[0]['id'], 2)

    def test_get_limit_offset(self):

        """ Проверяет одновременное использование limit и offset """

        url = reverse('posts')
        response = self.client.get(url, {'limit': 1, 'offset': 5})
        self.assertEqual(response.data[0]['id'], 6)

    def test_get_ordering_title(self):

        """ Проверяет сортировку по полю title """

        url = reverse('posts')
        Article.objects.create(title='a', url='url')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.data[0]['title'], 'a')

    def test_get_ordering_title_minus(self):

        """ Проверяет сортировку по убыванию title """

        url = reverse('posts')
        response = self.client.get(url, {'ordering': '-title'})
        self.assertNotEqual(response.data[0]['title'], 'a')

    def test_get_limit_minus_or_zero(self):

        """ При значениях меньше либо равно нуля использует стандартное значение limit """

        url = reverse('posts')
        response = self.client.get(url, {'limit': 0})
        self.assertEqual(len(response.data), 5)

    def test_get_ordering_not_exist(self):

        """ Тестирует сортировку по не существующим полям. Должен возвращать стандартные значения """

        url = reverse('posts')
        response = self.client.get(url, {'ordering': '177013'})
        self.assertEqual(len(response.data), 5)

    # def test_get_search_id_0(self):
    #
    #     """ Проверяет работоспособность поиска """
    #
    #     url = reverse('posts')
    #     response = self.client.get(url, {'id': 5})
    #     self.assertEqual(response.data[0]['id'], 5)

    # def test_get_search_id_1(self):
    #
    #     """ Проверяет работоспособность поиска """
    #
    #     url = reverse('posts')
    #     response = self.client.get(url, {'id': 555})
    #     # self.assertEqual(len(response.data), 0)
    #
    # def test_get_search_title(self):
    #
    #     """ Проверяет работоспособность поиска """
    #
    #     url = reverse('posts')
    #     response = self.client.get(url, {'title': 'post:4'})
    #     self.assertEqual(response.data[0]['id'], 5)
