from django import forms
from .models import Youtube
from .models import NaverBlog
# ModelForm 클래스 상속 받음
class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = (
            'youtube_id',
            'youtube_title',
            'youtube_link',
            'youtube_image',
            'youtube_hashtag',
            'youtube_channel_name',
            'youtube_channel_count',
            'youtube_content_like_count',
            'youtube_comment_like_count',
            'youtube_content_date',
        )

        labels = {
            'youtube_ide':'youtube_id',
            'youtube_title':'youtube_title',
            'youtube_link':'youtube_link',
            'youtube_image':'youtube_image',
            'youtube_hashtag':'youtube_hashtag',
            'youtube_channel_name':'youtube_channel_name',
            'youtube_channel_count':'youtube_channel_count',
            'youtube_content_like_count':'youtube_content_like_count',
            'youtube_comment_like_count':'youtube_comment_like_count',
            'youtube_content_date':'youtube_content_date',
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


