from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_index, name='product_index'), # index 명 변경
    path('product/list/', views.product_list, name='product_list'),
    # http://127.0.0.1:8000/product/list/ : 주소출에 표시
    path('product/detail/<str:prd_no>/', views.product_detail, name='product_detail'),
    # <str:prd_no> : 매개변수 
    path('product/insert/', views.product_insert, name='product_insert'),
    path('product/update/<str:prd_no>/', views.product_update, name='product_update'),
    path('product/delete/<str:prd_no>/', views.product_delete, name='product_delete'),

    path('product/search_form/', views.product_search_form, name='product_search_form'),
    path('product/search/', views.product_search, name='product_search'),

    path('product/ajax_test/', views.ajax_test, name='ajax_test'),
    path('product/get_data/', views.get_data, name='get_data'),

    path('product/search_form2/', views.product_search_form2, name='product_search_form2'),
    path('product/search2/', views.product_search2, name='product_search2'),

    path('product/search_form3/', views.product_search_form3, name='product_search_form3'),
    path('product/search3/', views.product_search3, name='product_search3'),
]