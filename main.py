from src.data_json.work_with_json import WorkWithJsonHH, WorkWithJsonSJ
from src.request.api import HH, SJ
from src.vacancy.vacancy import VacancySJ, VacancyHH

if __name__ == '__main__':
    search_query = input("Введите поисковый запрос: ").title().strip()
    if isinstance(search_query, str) and search_query.isalpha():
        hh = HH(search_query)
        sj = SJ(search_query)
        hh.get_vacancies()
        sj.get_vacancies()

        wwj_hh = WorkWithJsonHH()
        wwj_sj = WorkWithJsonSJ()
        vacancy_hh = wwj_hh.read_json()
        vacancy_sj = wwj_sj.read_json()
        # список со всеми вакансиями по ключевому слову
        vacancy_s = []
        for i in vacancy_hh:
            vacancy_s.append(
                VacancyHH(i['name'], i['apply_alternate_url'], i['snippet']['requirement'], i['snippet']['responsibility'], i['salary']['from'], i['salary']['to']))

        for i in vacancy_sj:
            vacancy_s.append(VacancySJ(i['profession'], i['link'], i['candidat'], i['payment_from'], i['payment_to']))

        for vacancy in vacancy_s:
            print(vacancy)
