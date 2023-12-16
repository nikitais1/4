from src.data_json.work_with_json import WorkWithJson
from src.request.api import HH, SJ
from src.vacancy.vacancy import VacancySJ, VacancyHH
from config import JSON_HH, JSON_SJ


def filter_by_salary(salary_key, vacancies_for_search):
    """Метод принимает список вакансий и возвращает новый список по минимальной зарплате"""
    tmp_vacancy_list = []
    for item in vacancies_for_search:
        is_condition1 = int(item.salary_from) > salary_key
        if is_condition1:
            tmp_vacancy_list.append(item)
    return tmp_vacancy_list


def filter_by_strings(keys, vacancies_for_search):
    """Метод принимает список вакансий и возвращает новый список по ключевому слову"""
    tmp_vacancy_list = []
    for item in vacancies_for_search:
        if set(keys) & set(item.title.split()):
            tmp_vacancy_list.append(item)
    return tmp_vacancy_list


def user_interaction():
    """Метод-диалог с пользователем"""
    print('Добро пожаловать в ПарсерВакансер!\nДавайте подберем для вас вакансии')
    search_query = input("Введите поисковый запрос: ").title().strip()
    if isinstance(search_query, str) and search_query.isalpha():
        HH(search_query).get_vacancies()
        SJ(search_query).get_vacancies()

        vacancy_hh = WorkWithJson.read_json(JSON_HH)
        vacancy_sj = WorkWithJson.read_json(JSON_SJ)
        vacancy_s = []
        for i in vacancy_hh:
            salary_to = '-'
            if i['salary']['to']:
                salary_to = i['salary']['to']
            salary_from = 0
            if i['salary']['from']:
                salary_from = i['salary']['from']
            vacancy_s.append(
                VacancyHH(i['name'], i['apply_alternate_url'], i['snippet']['requirement'],
                          i['snippet']['responsibility'], salary_from, salary_to))

        for i in vacancy_sj:
            salary_to = '-'
            if i['payment_to']:
                salary_to = i['payment_to']
            salary_from = 0
            if i['payment_from']:
                salary_from = i['payment_from']
            vacancy_s.append(VacancySJ(i['profession'], i['link'], i['candidat'], salary_from, salary_to))

        while True:
            key_salary = int(input("Введите минимальную заработную плату: "))
            if isinstance(key_salary, int):
                vac = filter_by_salary(key_salary, vacancy_s)
            if not vac:
                print("Нет вакансий, соответствующих заданным критериям.")
                break

            result = int(input("1 - Показать вакансии\n2 - Ввести дополнительное ключевое слово в названии вакансии\n"))
            if result == 1:
                print(vac)
                break
            elif result == 2:
                key_world = str(input("Введите дополнительное ключевое слово в названии вакансии: ").title().strip())

            vac2 = filter_by_strings((key_world,), vac)
            if not vac2:
                print("Нет вакансий, соответствующих заданным критериям.")
                break
            print(vac2)
