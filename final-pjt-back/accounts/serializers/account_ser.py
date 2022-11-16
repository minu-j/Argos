from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer
from movies.models import Genre, Movie

User = get_user_model()

# 회원가입 : 재정의/url, views를 거치지 않고 조회됨
# 현재 기본 필드 : 이름, 이메일, 패스워드
# 추가 필드 : 지역, 성별, 생년월일
class AccountSignUpSerializer(RegisterSerializer):
    
    region = serializers.CharField(max_length=100)
    sex = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()

    class Meta:
        model = User
        # fields = ('region', 'sex', 'birth_date', )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['region'] = self.validated_data.get('region', '')
        data['sex'] = self.validated_data.get('sex', '')
        data['birth_date'] = self.validated_data.get('birth_date', '')

        return data

# 프로필 정보 조회 및 수정 : 재정의/url, views를 거치지 않고 조회됨
class ProfileSerializer(UserDetailsSerializer):

    class GerneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id',)
    
    hate_genres = GerneSerializer(many=True, read_only=True)
    followers = UserSerializer(many=True)

    class Meta:
        model = User
        # 이 부분에 정의되는 부분만 수정 가능('followings : 팔로워')
        fields = ('id' , 'followers', 'username', 'profile', 'region', 'sex', 'birth_date', 'followings', 'hate_genres', )

# 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회
class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)
    

    # 좋아요 한 영화 목록
    like_movies = MovieSerializer(many=True)
    # 위시리스트에 담은 영화 목록
    wish_moives = MovieSerializer(many=True)
    # 평가한 영화 목록
    user_rated_movie = MovieSerializer(many=True)

    class Meta:
        model = User
        # 사용자 id, 평가한 영화 목록, 좋아요한 영화 목록, 위시리스트에 담은 영화 목록
        fields = ('id', 'user_rated_movie', 'like_movies','wish_moives',)


# # 팔로우 등록 및 해제 : 팔로우 수까지
# class FollowSerializer(serializers.ModelSerializer):

#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('id', 'username',)

#     followings = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'followings',)

# # 상대방 프로필 조회 
# class UserProfileSerializer(UserDetailsSerializer):

#     class GerneSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Genre
#             fields = ('id', 'name',)
            
#     hate_genres = GerneSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ('id' ,'username', 'profile', 'region', 'birth_date', 'sex', 'birth_date', 'followings', 'hate_genres', )