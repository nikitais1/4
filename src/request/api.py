from abc import ABC, abstractmethod
import requests
from config import URL_HH, URL_SJ, HEADERS_SJ
from src.data_json.work_with_json import WorkWithJsonHH, WorkWithJsonSJ


class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для получения вакансий по API"""
        pass


class HH(API):
    """Класс для работы с API HeadHunter"""

    def __init__(self, keyword, area=113):
        self.keyword = keyword
        self.area = area
        self.url = URL_HH
        self.params = {
            "text": keyword,
            "area": self.area,
            "per_page": 100,
            "only_with_salary": True
        }

    def get_vacancies(self):
        """Метод для получения вакансий HeadHunter по API"""
        response = requests.get(url=self.url, params=self.params)
        return WorkWithJsonHH.save_json(response.json()['items'])


class SJ(API):
    """Класс для работы с API SuperJob"""

    def __init__(self, keyword, page=1):
        self.url = URL_SJ
        self.params = {
            'keywords': keyword,
            'page': page
        }

    def get_vacancies(self):
        """Метод для получения вакансий SuperJob по API"""
        headers = {
            'X-Api-App-Id': HEADERS_SJ
        }
        response = requests.get(url=self.url, params=self.params, headers=headers)
        return WorkWithJsonSJ.save_json(response.json()['objects'])
