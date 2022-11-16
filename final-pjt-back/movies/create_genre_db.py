from asyncio.windows_events import NULL
from contextlib import nullcontext
from pprint import pprint
import requests
import json

TMDB_API_KEY = '51790401a4babecb78bc0eca24db117c' # 정민우

def get_genre():

    # 최종 dump 데이터
    database = []

    # API요청 URL
    base_url = 'https://api.themoviedb.org/3/'

    gerne_url = base_url + 'genre/movie/list?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
    
    # 요청한 데이터를 json형태로 변환하여 변수 genres에 저장
    genres = requests.get(gerne_url).json()
    for genre in genres['genres']:
        
        fields = {
            'name': genre['name'],
        }

        data = {
            "model": "movies.genre",
            "pk": genre['id'],
            "fields": fields
        }

        database.append(data)
    pprint(database)

    # json 파일 생성
    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(database, w, indent=2, ensure_ascii=False)

get_genre()