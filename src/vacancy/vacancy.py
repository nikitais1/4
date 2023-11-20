from abc import ABC, abstractmethod


class Vacancy(ABC):
    """Абстрактный класс для создания вакансии"""

    @abstractmethod
    def __repr__(self):
        pass


class VacancyHH(Vacancy):
    """Класс для создания вакансии HeadHunter"""

    def __init__(self, title, link, requirement, responsibility, salary_from, salary_to):
        self.title = title
        self.link = link
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f'Вакансия: {self.title}\n'
                f'Ссылка на вакансию: {self.link}\n'
                f'Требования: {self.requirement}\n'
                f'Ответственность: {self.responsibility}\n'
                f'Зарплата от: {self.salary_from}\n'
                f'Зарплата до: {self.salary_to}\n')


class VacancySJ(Vacancy):
    """Класс для создания вакансии SuperJob"""

    def __init__(self, title, link, description, salary_from, salary_to):
        self.title = title
        self.link = link
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __repr__(self):
        return (f'Вакансия: {self.title}\n'
                f'Ссылка на вакансию: {self.link}\n'
                f'Описание: {self.description}\n'
                f'Зарплата от: {self.salary_from}\n'
                f'Зарплата до: {self.salary_to}\n')
