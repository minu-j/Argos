import requests
import json

print(
    '###########################################################\n'
    '#                  create movie database                  #\n'
    '###########################################################\n'
    ' * Please input page under 500\n'
    ' * 1 PAGE = 20 MOVIES\n'
)
while True:
    page_num = int(input('PAGE: '))
    if 0 < page_num < 501:
        break
    else:
        print('ERROR : Please input page under 500\n')
print(page_num)
TMDB_API_KEY = input('TMDB API KEY: ')

# DB
db_1 = []
db_2 = []
success = 0
fail = 0


def get_data():
    global success, fail

    # API요청 URL
    base_url = 'https://api.themoviedb.org/3/'    

    # 전체 장르 DB
    genres_url = base_url + 'genre/movie/list?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
    print('장르 데이터 수신 성공')
    
    genres = requests.get(genres_url).json()
    for genre in genres['genres']:

        genre_data = {
            "model": "movies.genre",
            "pk": genre['id'],
            "fields": {
            'name': genre['name'],
        }
        }
        db_1.append(genre_data)


    # 전체 OTT 서비스 DB
    providers_url = base_url + 'watch/providers/movie?language=ko-KR&watch_region=KR&api_key=' + TMDB_API_KEY
    print('OTT 데이터 수신 성공')

    providers = requests.get(providers_url).json()
    for provider in providers['results']:

        provider_data = {
            "model": "movies.provider",
            "pk": provider['provider_id'],
            "fields": {
            'name': provider['provider_name'],
            'logo_path': provider['logo_path'],
            'display_priority': provider['display_priority'],
        }
        }
        db_1.append(provider_data)


    # 영화 데이터를 불러오면서 개별 영화에 해당하는 배우, 감독, 키워드 데이터도 같이 가져오기
    movie_popular_url = base_url + 'movie/popular?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
    print('영화 데이터 수신을 시작합니다.')
    
    for page in range(1, page_num + 1):
        
        movies = requests.get(movie_popular_url + '&page=' + str(page)).json()
        for movie in movies['results']:
            progress = ((success + fail) / (page_num * 20)) * 100
            print(f'total {success + fail} success{success} / fail{fail} ({progress}%)\r')
            
            # 해당 영화의 id값 지정
            movie_id = movie['id']

            # 중요한 데이터가 없는 영화는 필터링하기
            if movie['title'] == "" or movie['original_title'] == "" or movie['overview'] == "" or movie['release_date'] == "" or movie['popularity'] == 0 or movie['vote_average'] == 0 or movie['poster_path'] == "" or movie['backdrop_path'] == "" or movie['poster_path'] == 'null' or movie['backdrop_path'] == 'null': # 필터링
                # print('중요 데이터 누락')
                fail += 1
                continue
            
            # 디테일 - genre, runtime, status, tagline
            movie_details_url = base_url + 'movie/' + str(movie_id) + '?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
            movie_details = requests.get(movie_details_url).json()

            # 장르
            genres = []
            for genre in movie_details["genres"]:
                genres.append(genre["id"])
            if genres == []:
                # print('장르 데이터 누락')
                fail += 1
                continue
            
            # 런타임
            runtime = movie_details["runtime"]
            if genres == 0:
                # print('런타임 데이터 누락')
                fail += 1
                continue

            # 상태
            status = movie_details["status"]
            if status == 0:
                # print('상태 데이터 누락')
                fail += 1
                continue

            # 슬로건
            tagline = movie_details["tagline"]
            if tagline == 0:
                # print('슬로건 데이터 누락')
                fail += 1
                continue

            # 크레딧 - 배우, 감독의 id, name, popularity, profile_path, character
            movie_credits_url = base_url + 'movie/' + str(movie_id) + '/credits?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
            movie_credit = requests.get(movie_credits_url).json()
            
            credit_flag = True # 배우, 감독 정보가 없는 영화일 경우 필터링하기

            # 배우 : 캐스팅 순위 상위 3명의 배우 정보만 가져오기
            actors = []
            actor_datas = []

            for actor in movie_credit["cast"][:5]:

                actor_id = actor["id"]
                actors.append(actor_id)

                actor_name = actor["name"]
                actor_popularity = actor["popularity"]
                actor_profile_path = actor["profile_path"]

                if actor_name == "" or actor_popularity == 0 or actor_profile_path == None: # 필터링
                    credit_flag = False
                    break
                
                # 배우 DB
                actor_data = {
                    "model": "movies.actor",
                    "pk": actor_id,
                    "fields": {
                        'name': actor_name,
                        'popularity': actor_popularity,
                        'profile_path': actor_profile_path,
                    }
                }
                actor_datas.append(actor_data)

            if not credit_flag or actors == []:
                # print('배우 정보 누락')
                fail += 1
                continue
            else:
                db_1.extend(actor_datas)


            # 감독
            directors = []
            director_datas = []

            for crew in movie_credit["crew"]:
                if crew["job"] == 'Director':
                    director_id = crew["id"]
                    directors.append(director_id)

                    director_name = crew["name"]
                    director_popularity = crew["popularity"]
                    director_profile_path = crew["profile_path"]

                    if director_name == "" or director_popularity == 0 or director_profile_path == None: # 필터링
                        credit_flag = False
                        break

                    # 감독 DB
                    director_data = {
                        "model": "movies.director",
                        "pk": director_id,
                        "fields": {
                            'name': director_name,
                            'popularity': director_popularity,
                            'profile_path': director_profile_path,
                        }
                    }
                    director_datas.append(director_data)
        
            if not credit_flag or directors == []:
                # print('감독 정보 누락')
                fail += 1
                continue
            else:
                db_1.extend(director_datas)


            # 키워드 - id, name
            movie_keywords_url = base_url + 'movie/' + str(movie_id) + '/keywords?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
            movie_keyword = requests.get(movie_keywords_url).json()

            if movie_keyword["keywords"] == []: # 키워드 없는 영화 필터링
                continue
            else:
                keywords = []
                for keyword in movie_keyword["keywords"]:
                    keyword_id = keyword["id"]
                    keywords.append(keyword_id)
                    
                    keyword_name = keyword["name"]

                    keyword_data = {
                        "model": "movies.keyword",
                        "pk": keyword_id,
                        "fields": {
                            'name': keyword_name
                        }
                    }
                    db_1.append(keyword_data)


            # 유튜브 예고편 - key, type
            movie_videos_url = base_url + 'movie/' + str(movie_id) + '/videos?language=ko-KR&region=KR&api_key=' + TMDB_API_KEY
            movie_videos = requests.get(movie_videos_url).json()
            
            if movie_videos['results'] == []:
                # print('예고편 데이터 누락')
                fail += 1
                continue
            else:
                videos = []
                for video in movie_videos['results']:

                    video_id = video['id']
                    video_name = video['name']
                    video_key = video['key']
                    video_type = video['type']

                    if video_id == "" or video_name == "" or video_key == "" or video_type == "":
                        continue
                    else:
                        videos.append(video_id)
                        video_data = {
                            "model": "movies.video",
                            "pk": video['id'],
                            "fields": {
                                'name': video['name'],
                                'key': video['key'],
                                'video_type': video['type'],
                            }
                        }
                        db_1.append(video_data)
                        
            # 공급사 - flatrate-provider_id
            movie_providers_url = base_url + 'movie/' + str(movie_id) + '/watch/providers?language=ko-KR&watch_region=KR&api_key=' + TMDB_API_KEY
            movie_providers = requests.get(movie_providers_url).json()

            providers = []
            if movie_providers['results'] == []:
                pass
            else:
                if "KR" in movie_providers["results"]:
                    if "flatrate" in movie_providers["results"]["KR"]:
                        for provider in movie_providers['results']["KR"]["flatrate"]:
                            providers.append(provider["provider_id"])

            movie_data = {
                "model": "movies.movie",
                "pk": movie['id'],
                "fields": {
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'overview': movie['overview'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    
                    'runtime': runtime,
                    'status': status,
                    'tagline': tagline,

                    'genres': genres,
                    'actors': actors,
                    'directors': directors,
                    'keywords': keywords,
                    'videos': videos,
                    'providers': providers,
                    }
            }
           
            db_2.append(movie_data)
            success += 1


    # json 파일 생성
    with open("db_1.json", "w", encoding="utf-8") as w:
        json.dump(db_1, w, indent=2, ensure_ascii=False)
        
    with open("db_2.json", "w", encoding="utf-8") as w:
        json.dump(db_2, w, indent=2, ensure_ascii=False)
        
    print(
        '###########################################################\n\n'
        'done.\n\n'
        '$ python manage.py loaddata db_1.json\n\n'
        '$ python manage.py loaddata db_2.json\n'
    )

get_data()