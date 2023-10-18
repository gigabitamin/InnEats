from django import forms
from .models import DailyHotel
from .models import Yanolja
from .models import GoodChoice
from .models import Tripbtoz
from .models import Youtube

# ModelForm 클래스 상속 받음
class DailyHotelForm(forms.ModelForm):
    class Meta:

        # 데일리 호텔
        # PRIMARY KEY (daily_hotel_name, daily_hotel_address)        
        model = DailyHotel
        fields = (
            'daily_hotel_name',
            'daily_hotel_address',
            'daily_hotel_image',
            'daily_hotel_rating',
            'daily_hotel_link',
            'daily_hotel_date',
            'daily_hotel_price'
        )

        labels = {
            'daily_hotel_name' : '숙소 이름',
            'daily_hotel_address' : '주소',
            'daily_hotel_image' : '이미지 url',
            'daily_hotel_rating' : '별점',
            'daily_hotel_link' : '숙소 url',
            'daily_hotel_date' : '예약 가능 날짜',
            'daily_hotel_price' : '예약 가격'
        }

class YanoljaForm(forms.ModelForm):
    class Meta:

        # 야놀자
        # PRIMARY KEY (yanolja_name, yanolja_address)        
        model = Yanolja
        fields = (
            'yanolja_name',
            'yanolja_address',
            'yanolja_image',
            'yanolja_rating',
            'yanolja_link',
            'yanolja_date',
            'yanolja_price'
        )

        labels = {
            'yanolja_name' : '숙소 이름',
            'yanolja_address' : '주소',
            'yanolja_image' : '이미지 url',
            'yanolja_rating' : '별점',
            'yanolja_link' : '숙소 url',
            'yanolja_date' : '예약 가능 날짜',
            'yanolja_price' : '예약 가격'
        }


class GoodChoiceForm(forms.ModelForm):
    class Meta:

        # 여기어때
        # PRIMARY KEY (goodchoice_name, goodchoice_address)        
        model = GoodChoice
        fields = (
            'goodchoice_name',
            'goodchoice_address',
            'goodchoice_image',
            'goodchoice_rating',
            'goodchoice_link',
            'goodchoice_date',
            'goodchoice_price'
        )

        labels = {
            'goodchoice_name' : '숙소 이름',
            'goodchoice_address' : '주소',
            'goodchoice_image' : '이미지 url',
            'goodchoice_rating' : '별점',
            'goodchoice_link' : '숙소 url',
            'goodchoice_date' : '예약 가능 날짜',
            'goodchoice_price' : '예약 가격'
        }

class TripbtozForm(forms.ModelForm):
    class Meta:

        # 트립비토즈
        # PRIMARY KEY (trip_name, trip_address)        
        model = Tripbtoz
        fields = (
            'trip_name',
            'trip_address',
            'trip_image',
            'trip_rating',
            'trip_link',
            'trip_date',
            'trip_price'
        )

        labels = {
            'trip_name' : '숙소 이름',
            'trip_address' : '주소',
            'trip_image' : '이미지 url',
            'trip_rating' : '별점',
            'trip_link' : '숙소 url',
            'trip_date' : '예약 가능 날짜',
            'trip_price' : '예약 가격'
        }


class Youtube(forms.ModelForm):
    class Meta:

        # 유투브
        # PRIMARY KEY (youtube_id)        
        model = Youtube
        fields = (
            'youtube_id'
            'youtube_title'
            'youtube_link'
            'youtube_image'
            'youtube_hashtag'
            'youtube_channel_name'
            'youtube_channel_count'
            'youtube_comment_count'
            'youtube_content_date'
        )

        labels = {
            'youtube_id' : '유투브 no',
            'youtube_title' : '유투브 제목',
            'youtube_link' : '유투브 url',
            'youtube_image' : '유투브 이미지 url',
            'youtube_hashtag' : '유투브 해시태그',
            'youtube_channel_name' : '유투브 채널 이름',
            'youtube_channel_count' : '유투브 채널 조회수',
            'youtube_comment_count' : '유투브 댓글 좋아요 수',
            'youtube_content_date' : '유투브 영상 업로드 날짜'
        }        


