from pathlib import Path

URL_HH = "https://api.hh.ru/vacancies"
JSON_HH = Path(Path(__file__).parent, 'src/cache_json', 'cache_hh.json')
JSON_SJ = Path(Path(__file__).parent, 'src/cache_json', 'cache_sj.json')

URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
