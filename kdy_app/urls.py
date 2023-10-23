
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






    # path('blog/list/<str:keyword>', views.blog_list, name='blog_list'),
    # path('blog/detail/<str:keyword>', views.blog_detail, name='blog_detail'),
]

