"""

Тесты работоспособности парсера

"""


from django.test import TestCase
from site_parser.parse_and_write_to_db import parse, get_html


class ParserTestCase(TestCase):

    """ Тестирует работу парсера """

    def test_get_html(self):

        """ Если тест падает то скорее всего заблокирован IP """

        data = get_html('https://news.ycombinator.com/')
        self.assertNotEqual(data, None)

    def test_parser(self):

        """ Метод тестирует парсер """

        parsed_data = parse()
        self.assertEqual(len(parsed_data), 30)
