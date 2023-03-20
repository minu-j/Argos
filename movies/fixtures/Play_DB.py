import json

# DB
db_3 = []

def get_data():
    global db_3

    data = [
    {
      "title": "톰과 제리(Tom and Jerry) ",
      "movies": [
              {
            "title": "천국의 고양이 (Heavenly Puss)",
            "youtube_id": "_tbufE5zmvM"
          },
              {
            "title": "작은 꽥꽥이 (Little Quacker)",
            "youtube_id": "ahEkLHjFHQA"
          },
        {
            "title": "제리와 서커스 사자 (Jerry And The Lion)",
            "youtube_id": "s0uIrKruVsE"
          },
        {
            "title": "생쥐 우주에 가다 (Mouse into Space)",
            "youtube_id": "qBMICHNKYC8"
          },
        {
            "title": "빈털터리 야유회 (Down and Outing)",
            "youtube_id": "EbLoK59HWAU"
          },
        {
            "title": "아빠가 최고야 (Tops with Pops)",
            "youtube_id": "TqhYaTtspOs"
          },
        {
            "title": "아가 밥 먹이기 (Feedin the Kiddie",
            "youtube_id": "Qx_lrB4h_wg"
          },
        {
            "title": "톰의 사진 판정 (Toms Photo Finish)",
            "youtube_id": "Gh7YwxqOiOU"
          },
        {
            "title": "덫에서 우뚝 서 있기 (Tall In The Trap)",
            "youtube_id": "u2pEfFO9zV0"
          },
        {
            "title": "아기 돌보기 (Tot Watchers)",
            "youtube_id": "xXmFemg9Kms"
          }
          ]
    },
     {
      "title": "장르 영화의 완성, 알프레드 히치콕",
      "movies": [
        {
            "title": "북북서로 진로를 돌려라 (North By Northwest) - 1부",
            "youtube_id": "3JxxVXllEaQ"
        },
        {
            "title": "북북서로 진로를 돌려라 (North By Northwest) - 2부",
            "youtube_id": "f__uHwu9Urw"
        },
        {
            "title": "다이얼 M을 돌려라 (Dial M for Murder) - 1부",
            "youtube_id": "3Uat4qEBDVI"
        },
        {
            "title": "다이얼 M을 돌려라 (Dial M for Murder) - 2부",
            "youtube_id": "5w-WZp451m4"
        },
        {
            "title": "열차 안의 낮선 자들 (Strangers On A Train) - 1부",
            "youtube_id": "fL7f7z_1004"
        },
        {
            "title": "열차 안의 낮선 자들 (Strangers On A Train) - 2부",
            "youtube_id": "47-ODMwAEC8"
        },
        {
            "title": "이창 (Rear Window) - 1부",
            "youtube_id": "WYa1tCYLy5E"
        },
        {
            "title": "이창 (Rear Window) - 2부",
            "youtube_id": "c1rersT4JuY"
        },
        {
            "title": "현기증 (Vertigo) - 1부",
            "youtube_id": "NRvsK0330vI"
        },
        {
            "title": "현기증 (Vertigo) - 2부",
            "youtube_id": "FDzE5RUSmGg"
        },
        {
            "title": "로프 (Rope) - 1부",
            "youtube_id": "iuTgdNWhNA8"
        },
        {
            "title": "로프 (Rope) - 2부",
            "youtube_id": "4zyd5xvwxIc"
        },
        ]
        },
        {
      "title": "[2X9HD] 구교환 X 이옥섭",
      "movies": [
              {
            "title": "왜 독립영화 감독들은 DVD를 주지 않는가? (Where is my DVD?, 2013)",
            "youtube_id": "j9QzZ5hwDhA"
        },
        {
            "title": "플라이 투 더 스카이 (FLY TO THE SKY, 2015)",
            "youtube_id": "7y-eps3O-Ko"
          },
        {
            "title": "천우희 & 이주영 girls on top (걸스온탑, 2017)",
            "youtube_id": "3sa_Ko9sHvg"
          },
        {
            "title": "구교환 & 이옥섭 로미오 : 눈을 가진 죄 (ROMEO, 2019)",
            "youtube_id": "UAXaxqroUwo"
          },
        {
            "title": "전소니 X 황소윤 X 이옥섭 탈출 :Send me out",
            "youtube_id": "EyLzOZZuNHA"
          },
        {
            "title": "김향기 & 비스포크 & 가리비 &이옥섭 〈너를 위해 문을 열어 놓을게〉",
            "youtube_id": "koT2zYZIbIM"
          },
        {
            "title": "메구X구교환X김다빈 러브빌런 (LOVE VILLAIN,2022)",
            "youtube_id": "Jz2NR3KYN3c"
          },
        {
            "title": "사람냄새 이효리 (Super Star LeeHyori,2022)",
            "youtube_id": "f9uLhQ1paW8"
          },
          ]
        },
    {
      "title": "월트 디즈니 명화 (Walt Disney)",
      "movies": [
        {
            "title": "피노키오 (Pinnocchio) - 1부",
            "youtube_id": "1GIwRL1btEM"
          },
        {
            "title": "피노키오 (Pinnocchio) - 2부",
            "youtube_id": "YCr-4JmRvwY"
          },
              {
            "title": "피터팬 (Peter Pan) - 1부",
            "youtube_id": "e5RnSIVdTFI"
          },
        {
            "title": "피터팬 (Peter Pan) - 2부",
            "youtube_id": "8TEAhFRRrSo"
          },
        {
            "title": "백설공주와 일곱 난쟁이 (Snow White And The Seven Dwarfs) - 1부",
            "youtube_id": "mzly-017KLk"
          },
        {
            "title": "백설공주와 일곱 난쟁이 (Snow White And The Seven Dwarfs) - 2부",
            "youtube_id": "WDzpuPkLHhg"
          },
        {
            "title": "동물농장 (Animal Farm) - 1부",
            "youtube_id": "bh8KQxW7fL0"
          },
        {
            "title": "동물농장 (Animal Farm) - 2부",
            "youtube_id": "lw4dO5Y2rRk"
          },
        {
            "title": "걸리버 여행기 (Gullivers Travels) - 1부",
            "youtube_id": "E8IcUl-s-Zk"
          },
        {
            "title": "걸리버 여행기 (Gullivers Travels) - 2부",
            "youtube_id": "y7l_NMa__jM"
          },
              {
            "title": "리럭턴트 드래곤 (The Reluctant Dragon)",
            "youtube_id": "Ja0rmNCWRH0"
          }
          ]
    },
    {
      "title": "시대를 초월하는 고전 명작 Timeless Films",
      "movies": [
                      {
            "title": "시민 케인 (Citizen Kene) - 1부",
            "youtube_id": "e9HybvMcGL8"
        },
              {
            "title": "시민 케인 (Citizen Kene) - 2부",
            "youtube_id": "FejcNO2F2_4"
        },
        {
            "title": "티파니에서 아침을(Breakfast at tiffany's) - 1부",
            "youtube_id": "uSic55nGLec"
          },
        {
            "title": "티파니에서 아침을(Breakfast at tiffany's) - 2부",
            "youtube_id": "Gqb5pAMKZsw"
          },
        {
            "title": "사랑은 비를 타고 (Singin' in the Rain) - 1부",
            "youtube_id": "675sqFEJz1k"
          },
        {
            "title": "사랑은 비를 타고 (Singin' in the Rain) - 2부",
            "youtube_id": "iS44jQCTTqQ"
          },
              {
            "title": "레베카 - 1부",
            "youtube_id": "Oe_z0qktJks"
        },
        {
            "title": "레베카 - 2부",
            "youtube_id": "TZyN6whXO9M"
          },
        {
            "title": "지상에서 영원으로 (From Here To Eternity) - 1부",
            "youtube_id": "ZJXYHDWn0Es"
          },
        {
            "title": "지상에서 영원으로 (From Here To Eternity) - 2부",
            "youtube_id": "y0PH68JQkEA"
          },
        {
            "title": "누구를 위하여 종은 울리나 (For Whom the Bell Tolls) - 1부",
            "youtube_id": "T2aRQu3G-yI"
          },
        {
            "title": "누구를 위하여 종은 울리나 (For Whom the Bell Tolls) - 2부",
            "youtube_id": "GiKm-OKu508"
          },
        {
            "title": "카사블랑카 (Casablanca) - 1부",
            "youtube_id": "_AmVA48lpmA"
          },
        {
            "title": "카사블랑카 (Casablanca) - 2부",
            "youtube_id": "ntl2-W1Oi8I"
          },
          ]
    },
   {
      "title": "도날드 덕 (Donald Duck)",
      "movies": [
              {
            "title": "경찰관이 된 도날드 (Officer Duck)",
            "youtube_id": "hmg4p0VcPLs"
          },
              {
            "title": "골프경기 (Donald's Golf Game)",
            "youtube_id": "OE2St0_tmgU"
          },
        {
            "title": "공사장의 일꾼 (The Riveter)",
            "youtube_id": "PbWW65fn-PU"
          },
        {
            "title": "기차를 사수하자 (Out of Scale)",
            "youtube_id": "sR2s8uGg0IU"
          },
        {
            "title": "꿀 도둑 (Beezy Bear)",
            "youtube_id": "Uc7Vpcvzhpk"
          },
        {
            "title": "신사 도날드 (Don Donald)",
            "youtube_id": "aSN4wxVaHvE"
          },
        {
            "title": "도날드의 펭귄 (Donald's Penguin)",
            "youtube_id": "wnDo8ExWVpc"
          },
        {
            "title": "보이스카우트 (Good Scouts)",
            "youtube_id": "nQ5O2YkN4ZE"
          },
        {
            "title": "하키 챔피언 (The Hockey Champ)",
            "youtube_id": "bLXhRAsj1Jo"
          },
        {
            "title": "도날드의 범죄 (Donald's Crime)",
            "youtube_id": "8LzD8rZKlss"
          }
          ]
    },
     {
      "title": "한국 영상자료원이 디지털 복원한 한국 고전 명작",
      "movies": [
        {
            "title": "오발탄 (1961)",
            "youtube_id": "LfxIfK8ThFc"
          },
        {
            "title": "서편제 (1993)",
            "youtube_id": "sdjwD4jW4XY"
          },
        {
            "title": "바보들의 행진 (1975)",
            "youtube_id": "4PvzT5WnNrA"
          },
        {
            "title": "홍길동 (1967)",
            "youtube_id": "wcXignso3pk"
        },
        {
            "title": "우리들의 일그러진 영웅 (1992)",
            "youtube_id": "De0ZkC1mCxc"
          },
        {
            "title": "카인의 후예 (1968)",
            "youtube_id": "o3XIl5V3XJI"
          },
        {
            "title": "길소뜸 (1985)",
            "youtube_id": "UtDHc881l34"
          },
        {
            "title": "콩쥐 팥쥐 (1978)",
            "youtube_id": "toDMRs8tKIs"
          },
              {
            "title": "마음의 고향 (1949)",
            "youtube_id": "Jw4WFDq-uUg"
        },
          ]
        },
    {
      "title": "미키 마우스 (Mickey Mouse)",
      "movies": [
              {
            "title": "미키와 아기 코끼리 (Mickey's Elephant)",
            "youtube_id": "pAkE0mK1_ds"
          },
              {
            "title": "공연은 즐거워 (Mickey's Amateur)",
            "youtube_id": "FgOqolFDgSI"
          },
        {
            "title": "자동차 대소동 (Mickey's Trailer)",
            "youtube_id": "EOjAoCv_olc"
          },
        {
            "title": "뒤죽박죽 폴로 경기 (Mickey's Polo Team)",
            "youtube_id": "7GBZtuxJWtg"
          },
        {
            "title": "마술사 미키 (Magician Mickey)",
            "youtube_id": "CHItQn2Afio"
          },
        {
            "title": "미키의 방주 (Boat Builders)",
            "youtube_id": "zlwlWzA7zfk"
          },
        {
            "title": "산양 사냥 대소동 (Moose Hunters)",
            "youtube_id": "B9yk8xbNieY"
          },
        {
            "title": "스케이트는 즐거워 (On Ice)",
            "youtube_id": "b7lLi-hFQDc"
          },
        {
            "title": "이상한 나라의 미키 (Thru the Mirror)",
            "youtube_id": "oatZiGAgAAg"
          },
        {
            "title": "회오리 바람은 싫어 (The Little Whirlwind)",
            "youtube_id": "N_FKR6ac9tM"
          }
          ]
    },
    
   
         {
      "title": "꼬마 유령 캐스퍼 (Casper And The Angels)",
      "movies": [
              {
            "title": "화살 소동 (Boos and Arrows)",
            "youtube_id": "MZ8l3xiUAm8"
          },
              {
            "title": "귀여운 아기 고양이들 (Puss N'Boos)",
            "youtube_id": "d6Vupo4zMCc"
          },
        {
            "title": "경주 우승자 모레스 (Boo Ribbon Winner)",
            "youtube_id": "pgW0S7C01dw"
          },
        {
            "title": "그림자 놀이 (Ground Hog Play)",
            "youtube_id": "8JhTQZYivxU"
          },
        {
            "title": "모두 모두를 겁주자 (A Haunting We Will Go)",
            "youtube_id": "b8MbIWP7ULI"
          },
        {
            "title": "보안관 캐스퍼 (Boos and Saddles)",
            "youtube_id": "AYEaZKBjb3I"
          },
        {
            "title": "깊고 깊은 바다 (The Deep Boo Sea)",
            "youtube_id": "wcbPBIQYJRQ"
          },
        {
            "title": "서커스단원 캐스퍼 (Casper Comes To Clown)",
            "youtube_id": "coEH_0C69CU"
          },
        {
            "title": "용감한 망아지 스펑키 (Boo Kind To Animals)",
            "youtube_id": "J63fedUda_Y"
          },
        {
            "title": "울지마라 아가야 (Boo Hoo Baby)",
            "youtube_id": "GFfTwPonMVQ"
          }
          ]
    },
    ]

    count = 1

    for index, i in enumerate(data):
        
        print(index + 1, i["title"])
        playlist = {
            "model": "movies.playlist",
            "pk": index + 1,
            "fields": {
                "title": i["title"]
                }
        },
        db_3.extend(playlist)

        for j in i["movies"]:
            print(j)

            playlist = {
                "model": "movies.playmovie",
                "pk": count,
                "fields": {
                    "title": j["title"],
                    "key": j["youtube_id"],
                    "playlist": index + 1
                    }
            },
            db_3.extend(playlist)
            print(playlist)
            count += 1


    # json 파일 생성
    with open("db_3.json", "w", encoding="utf-8") as w:
        json.dump(db_3, w, indent=2, ensure_ascii=False)

get_data()