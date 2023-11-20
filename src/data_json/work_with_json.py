import json
from config import JSON_HH, JSON_SJ


class WorkWithJsonHH:
    path_hh = JSON_HH

    @classmethod
    def save_json(cls, data):
        with open(cls.path_hh, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        with open(cls.path_hh, 'r', encoding='utf-8') as file:
            return json.load(file)


class WorkWithJsonSJ:
    path_sj = JSON_SJ

    @classmethod
    def save_json(cls, data):
        with open(cls.path_sj, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        with open(cls.path_sj, 'r', encoding='utf-8') as file:
            return json.load(file)
