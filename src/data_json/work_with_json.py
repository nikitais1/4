import json


class WorkWithJson:
    """Класс для работы с API"""

    @classmethod
    def save_json(cls, data, path):
        """Класс-метод для сохранения вакансий в JSON file"""
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls, path):
        """Класс-метод для чтения вакансий из JSON file"""
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
