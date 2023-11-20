from abc import ABC, abstractmethod
import requests
from config import URL_HH, URL_SJ
from src.data_json.work_with_json import WorkWithJsonHH, WorkWithJsonSJ


class API(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HH(API):
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
        response = requests.get(url=self.url, params=self.params)
        return WorkWithJsonHH.save_json(response.json()['items'])


class SJ(API):
    def __init__(self, keyword, page=1):
        self.url = URL_SJ
        self.params = {
            'keywords': keyword,
            'page': page
        }

    def get_vacancies(self):
        headers = {
            'X-Api-App-Id': 'v3.r.137945941.84cf2d532b12bd08bc320ce6ba2255cd6619e46d.3bb52fb483728decee19b2fa04e5c37d231d47fd'
        }
        response = requests.get(url=self.url, params=self.params, headers=headers)
        return WorkWithJsonSJ.save_json(response.json()['objects'])
