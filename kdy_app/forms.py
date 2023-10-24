from django import forms
from .models import Youtube
from .models import NaverBlog
from .models import UsersAppUser

class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = (
            'youtube_id',
            'youtube_title',
            'youtube_link',
            'youtube_image',
            'youtube_name',
            'youtube_views',
            'youtube_date',
        )

        labels = {
            'youtube_id':'youtube_id',
            'youtube_title':'제목',
            'youtube_link':'URL',
            'youtube_image':'이미지 링크',
            'youtube_channel_name':'채널명',
            'youtube_views':'조회수',
            'youtube_date':'업로드 날짜',
        }

class NaverBlogForm(forms.ModelForm):
    class Meta:
        model = NaverBlog
        fields = (
            'naver_blog_id',
            'naver_blog_title',
            'naver_blog_link',
            'naver_blog_image',
            'naver_blog_hashtag',
            'naver_bloger_name',
            'naver_blog_content_likeit_count',
            'naver_blog_content_date',
        )

        labels = {
            'naver_blog_id' : 'naver_blog_id',
            'naver_blog_title' : 'naver_blog_title',
            'naver_blog_link' : 'naver_blog_link',
            'naver_blog_image' : 'naver_blog_image',
            'naver_bloger_name' : 'naver_blog_hashtag',
            'naver_bloger_name' : 'naver_bloger_name',
            'naver_blog_content_likeit_count' : 'naver_blog_content_likeit_count',
            'naver_blog_content_date' : 'naver_blog_content_date',
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UsersAppUser
        fields = (
            'id',
            'password',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'user_name',
            'user_phone',
            'user_address',
            'preferred_region_no',
            'preferred_accommodation_type_no',
            'preferred_tour_theme_type_no',
            'profile_image'
        )

        labels = {
            'id':'id',
            'password':'password',
            'last_login':'last_login',
            'is_superuser':'is_superuser',
            'username':'username',
            'first_name':'first_name',
            'last_name':'last_name',
            'email':'email',
            'is_staff':'is_staff',
            'is_active':'is_active',
            'date_joined':'date_joined',
            'user_name':'user_name',
            'user_phone':'user_phone',
            'user_address':'user_address',
            'preferred_region_no':'preferred_region',
            'preferred_accommodation_type_no':'preferred_accommodation_type',
            'preferred_tour_theme_type_no':'preferred_tour_theme_type',
            'profile_image':'profile_image'            
        }


class ImageForm(forms.Form):
    image = forms.ImageField()


