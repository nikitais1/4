import json
from abc import ABC, abstractmethod
from config import JSON_HH, JSON_SJ


class WorkWithJson(ABC):
    """Абстрактный класс для работы с API"""

    @classmethod
    @abstractmethod
    def save_json(cls, data):
        """Абстрактный класс-метод для сохранения вакансий в JSON file"""
        pass

    @classmethod
    @abstractmethod
    def read_json(cls):
        """Абстрактный класс-метод для чтения вакансий из JSON file"""
        pass


class WorkWithJsonHH(WorkWithJson):
    """Класс для работы с API HeadHunter"""
    path_hh = JSON_HH

    @classmethod
    def save_json(cls, data):
        """Класс-метод для сохранения HeadHunter вакансий в JSON file"""
        with open(cls.path_hh, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        """Класс-метод для чтения HeadHunter вакансий из JSON file"""
        with open(cls.path_hh, 'r', encoding='utf-8') as file:
            return json.load(file)


class WorkWithJsonSJ(WorkWithJson):
    """Класс для работы с API SuperJob"""
    path_sj = JSON_SJ

    @classmethod
    def save_json(cls, data):
        """Класс-метод для сохранения SuperJob вакансий в JSON file"""
        with open(cls.path_sj, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        """Класс-метод для чтения SuperJob вакансий из JSON file"""
        with open(cls.path_sj, 'r', encoding='utf-8') as file:
            return json.load(file)
