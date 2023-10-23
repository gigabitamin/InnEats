
from django.urls import path
from . import views

urlpatterns = [
    path('youtube/list/<str:keyword>', views.youtube_list, name='youtube_list'),
    path('youtube/detail/<str:youtube_id>', views.youtube_detail, name='youtube_detail'),
    path('youtube/list/kdy/<str:keyword>', views.youtube_list_kdy, name='youtube_list_kdy'),
    path('youtube/detail/<str:keyword>', views.youtube_detail, name='youtube_detail'),
    path('youtube/all/lists/', views.youtube_all_lists, name='youtube_all_lists'),
    path('youtube/all/detail/<str:youtube_id>', views.youtube_all_detail, name='youtube_all_detail'),
    path('youtube/insert/', views.youtube_insert, name='youtube_insert'),
    path('youtube/update/<str:youtube_id>', views.youtube_update, name='youtube_update'),
    path('youtube/delete/<str:youtube_id>', views.youtube_delete, name='youtube_delete'),
    path('youtube/search/custom/form/', views.youtube_search_custom_form, name='youtube_search_custom_form'),
    path('youtube/search/custom/', views.youtube_search_custom, name='youtube_search_custom'),
    path('youtube/search/ajax/form', views.youtube_search_ajax_form, name='youtube_search_ajax_form'),
    path('youtube/search/ajax/', views.youtube_search_ajax, name='youtube_search_ajax'),

    path('naver_blog/list/<str:keyword>', views.naver_blog_list, name='naver_blog_list'),
    path('naver_blog/detail/<str:naver_blog_id>', views.naver_blog_detail, name='naver_blog_detail'),
    path('naver_blog/list/kdy/<str:keyword>', views.naver_blog_list_kdy, name='naver_blog_list_kdy'),
    path('naver_blog/detail/<str:keyword>', views.naver_blog_detail, name='naver_blog_detail'),
    path('naver_blog/all/lists/', views.naver_blog_all_lists, name='naver_blog_all_lists'),
    path('naver_blog/all/detail/<str:naver_blog_id>', views.naver_blog_all_detail, name='naver_blog_all_detail'),
    path('naver_blog/insert/', views.naver_blog_insert, name='naver_blog_insert'),
    path('naver_blog/update/<str:naver_blog_id>', views.naver_blog_update, name='naver_blog_update'),
    path('naver_blog/delete/<str:naver_blog_id>', views.naver_blog_delete, name='naver_blog_delete'),
    path('naver_blog/search/custom/form/', views.naver_blog_search_custom_form, name='naver_blog_search_custom_form'),
    path('naver_blog/search/custom/', views.naver_blog_search_custom, name='naver_blog_search_custom'),
    path('naver_blog/search/ajax/form', views.naver_blog_search_ajax_form, name='naver_blog_search_ajax_form'),
    path('naver_blog/search/ajax/', views.naver_blog_search_ajax, name='naver_blog_search_ajax'),


]

