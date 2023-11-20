from pathlib import Path

URL_HH = 'https://api.hh.ru/vacancies'
URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
HEADERS_SJ = 'v3.r.137945941.84cf2d532b12bd08bc320ce6ba2255cd6619e46d.3bb52fb483728decee19b2fa04e5c37d231d47fd'

JSON_HH = Path(Path(__file__).parent, 'src/cache_json', 'cache_hh.json')
JSON_SJ = Path(Path(__file__).parent, 'src/cache_json', 'cache_sj.json')

