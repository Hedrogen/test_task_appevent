"""

    В этом модуле хранится код, отвечающий за парсинг и запись данных в БД

"""

import logging
import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError
from fake_useragent import UserAgent

from site_parser.models import Article

logger = logging.getLogger(__name__)


def get_html(link):

    """ Возвращает html. """

    response = requests.get(link, headers={'User-Agent': UserAgent().chrome})
    if response.status_code == 200:
        logger.info('Получение HTML: 200 OK')
        content = response.text
        return content
    logger.error('Ошибка получения html. Код ошибки: %s', response.status_code)
    return None


def get_soup(link):

    """ Получает soup (bs4) по ссылке. """

    return BeautifulSoup(get_html(link), 'lxml')


def parse():

    """
    Парсит сайт https://news.ycombinator.com/' и
    возвращает список, содержащий кортежи.
    Кортежи хранят информацию о спарсенных статьях.
    """

    logger.info('Старт парсинга')
    url = 'https://news.ycombinator.com/'
    soup = get_soup(url)
    logger.info('Перевод в soup')
    tr_blocks = soup.find_all('tr', {'class': 'athing'})

    values = []

    for block in tr_blocks:
        storylink = block.find('a', {'class': 'storylink'})
        href = storylink['href']
        title = storylink.text
        values.append((title, href))
    write_to_db(values)
    return values


def write_to_db(data):

    """ Записывает данные в базу данных """

    logger.info('Запись данных в БД')

    for tuple_ in data:
        try:
            article = Article.objects.create(title=tuple_[0], url=tuple_[1])
            logger.info('Создание поста в БД: ID = %s', article.id)
        except IntegrityError:
            logger.debug('Пост существует: title=%s', tuple_[0])
            pass
        except (KeyError, Exception) as error:
            logger.error('Ошибка при записе данных в БД: %s', error)
            pass
