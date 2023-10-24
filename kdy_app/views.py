from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.shortcuts import get_object_or_404, render, redirect
from .models import NaverBlog
from .models import Youtube
from django.db.models import Q
from .forms import YoutubeForm
from .forms import NaverBlogForm
from .forms import ImageForm
from .forms import UserInfoForm
from .models import UsersAppUser
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required


def my_page_delete_move(request, id):
    user_info = get_object_or_404(UsersAppUser, pk=id)        
    return render(request, 'kdy_app/my_page_delete_confirm.html', {'user_info':user_info})

@login_required
def my_page_delete(request):
    if request.method == "POST":
        user = request.user  # 현재 로그인한 사용자
        user.delete()  # 사용자 정보 삭제
        return redirect('index')  # 탈퇴 후 리디렉션할 URL
    return render(request, 'kdy_app/my_page_delete_confirm.html')



class MyPageDeleteView(DeleteView):
    model = UsersAppUser
    success_url = 'index'  # 회원 탈퇴 후 리디렉션할 URL

    # 'my_page_delete_confirm.html' 템플릿을 사용하도록 설정
    template_name = 'kdy_app/my_page_delete_confirm.html'


def sign_up_upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            ImageForm.objects.create(image=image)
            return redirect('users_app/sign_up2.html')
    else:
        form = ImageForm()
    return render(request, 'users_app/sign_up2.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            ImageForm.objects.create(image=image)
            return redirect('kdy_app/my_page.html')
    else:
        form = ImageForm()
    return render(request, 'kdy_app/my_page.html', {'form': form})



@login_required
def my_page(request):
    user_info = request.user  # 현재 로그인한 사용자
    return render(request, 'kdy_app/my_page.html', {'user_info': user_info})


# @login_required
# def my_page(request):
#     user_info = request.user  # 현재 로그인한 사용자
#     if user_info.is_authenticated and user_info.id == id:
#         return render(request, 'kdy_app/my_page.html', {'user_info': user_info})
#     else:
#         # 로그인하지 않은 사용자나 다른 사용자의 마이페이지에 접근하려는 경우 리디렉션
#         return redirect('sign_in')  

def my_page_update(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('my_page', user_info.id)
    else:
        user_form = UserInfoForm(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

# def my_page_delete(id):
#     user_info = get_object_or_404(UsersAppUser, pk=id)
#     user_info.delete()
#     print('탈퇴가 완료되었습니다')
#     return redirect('index')

def jeju_accom_type(request):
    return render(request, 'kdy_app/jeju_accom_type.html')


def naver_blog_list(request, keyword):
    naver_blog_data = NaverBlog.objects.filter(naver_blog_title__icontains=keyword)
    naver_blog_list = NaverBlog.objects.all()
    
    naver_blog_list = NaverBlog.objects.all()[0:30]
    if len(naver_blog_data) > 1:
        naver_blog_data = naver_blog_data[0]
    else:
        naver_blog_data = naver_blog_list[0]

    grouped_naver_blog_list = [naver_blog_list[i:i+3] for i in range(0, len(naver_blog_list), 3)]
    
    return render(request, 'kdy_app/naver_blog_list.html', {'naver_blog_data':naver_blog_data, 'naver_blog_list':naver_blog_list, 'grouped_naver_blog_list': grouped_naver_blog_list, 'keyword':keyword})

def naver_blog_detail(request, naver_blog_id):
    NaverBlog = get_object_or_404(NaverBlog, pk=naver_blog_id)
    return render(request, 'kdy_app/naver_blog_detail.html', {'NaverBlog':NaverBlog})

def naver_blog_list_kdy(request,keyword):
    return render(request, 'kdy_app/naver_blog_list_kdy.html',{'keyword':keyword})

def naver_blog_all_lists(request):
    naver_blog_all_lists = NaverBlog.objects.all()
    return render(request, 'kdy_app/naver_blog_all_lists.html', {'naver_blog_all_lists':naver_blog_all_lists})

def naver_blog_all_detail(request, naver_blog_id):
    NaverBlog = get_object_or_404(NaverBlog, pk=naver_blog_id)
    return render(request, 'kdy_app/naver_blog_all_detail.html', {'NaverBlog':NaverBlog})

def naver_blog_insert(request):    
    if request.method == "POST":        
        form = NaverBlogForm(request.POST)        
        if form.is_valid():
            NaverBlog = form.save(commit=False)            
            NaverBlog.save()
            return redirect('naver_blog_all_lists')
    else:
        form = NaverBlogForm()
    
    return render(request, 'kdy_app/naver_blog_all_insert.html', {'form':form})
        
def naver_blog_update(request, naver_blog_id):  
    NaverBlog = get_object_or_404(NaverBlog, pk=naver_blog_id)    
    if request.method == "POST":        
        form = NaverBlogForm(request.POST, instance=NaverBlog)        
        if form.is_valid(): # 저장 지연
            NaverBlog = form.save(commit=False)
            NaverBlog.save() # 저장
            return redirect('naver_blog_all_lists')
    else:
        form = NaverBlogForm(instance=NaverBlog)        
    
    return render(request, 'kdy_app/naver_blog_all_update.html', {'form':form})

def naver_blog_delete(naver_blog_id):
    NaverBlog = get_object_or_404(NaverBlog, pk=naver_blog_id)    
    NaverBlog.delete()
    return redirect('naver_blog_list')

def naver_blog_search_custom_form(request):
    return render(request, 'kdy_app/naver_blog_search_custom.html')

def naver_blog_search_custom(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "naver_blog_title":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_title__contains=keyword)) 
        elif type == "naver_blog_channel_name":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_channel_name__contains=keyword))
        elif type == "naver_blog_hashtag":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_hashtag__contains=keyword))
        else: 
            pass

        return render(request, 'kdy_app/naver_blog_search_custom.html', {'naver_blog_list':naver_blog_list})

def naver_blog_search_ajax_form(request):
    return render(request, 'kdy_app/naver_blog_search_ajax.html')

def naver_blog_search_ajax(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "naver_blog_title":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_title__contains=keyword)) 
        elif type == "naver_blog_channel_name":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_channel_name__contains=keyword))
        elif type == "naver_blog_hashtag":
            naver_blog_list = NaverBlog.objects.filter(Q(naver_blog_hashtag__contains=keyword))
        else: 
            pass

        naver_blog_list_json = json.loads(serializers.serialize('json', naver_blog_list, ensure_ascii=False))

        return JsonResponse({'reload_all':False, 'naver_blog_list_json':naver_blog_list_json})
    


def youtube_list(request, keyword):
    # keyword 가 포함된 youtube_title을 db에서 검색한 뒤 해당 row가 존재하면 불러와서 youtube_data 에 저장, 
    # 리스트 일 시 첫행만 반환, 해당 조건으로 검색해서 결과값이 없을 시 all_list 에서 첫 행 반환 
    # 알고리즘으로 추천 리스트 테이블을 따로 만들어 둔 뒤에 그 테이블에서 첫 행을 반환시켜서 해당 keyword와 관련된 '오늘의 추천 유투브' 라는 식으로 출력할 것
    # 추천 리스트는 view나 instance 로 만들어도 되고 해당 테이블 정렬 순서는 알고리즘 상 가장 첫 행이 가장 추천 가치가 높도록 
    # 객관적 수치(조회수 댓글 수 좋아요 수 등) 을 비교해서 정렬 될 수 있도록 짤 것
    # 해당 절차를 다른 컨텐츠 페이지에 동일하게 적용

    youtube_data = Youtube.objects.filter(youtube_title__icontains=keyword)
    youtube_list = Youtube.objects.all()

    # 추천영상 알고리즘에 포함
    if len(youtube_data) > 1:
        youtube_data = youtube_data[0]
    else:
        youtube_data = youtube_list[0]

    # 3개씩 묶어서 출력 -> for 문 출력시 css 문제로 1개씩 출력할경우 1개별로 행이 달라지는 문제가 발생, 3개씩 미리 구성후 한 행에 3개씩 출력
    grouped_youtube_list = [youtube_list[i:i+3] for i in range(0, len(youtube_list), 3)]
    # if len(youtube_list) % 3 == 0:
    #     print()

    # for i in grouped_youtube_list
    # grouped_youtube_list[0]
    # grouped_youtube_list[1]
    # grouped_youtube_list[2]
    
    return render(request, 'kdy_app/youtube_list.html', {'youtube_data':youtube_data, 'youtube_list':youtube_list, 'grouped_youtube_list': grouped_youtube_list, 'keyword':keyword})

def youtube_detail(request, youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)
    return render(request, 'kdy_app/youtube_detail.html', {'youtube':youtube})

def youtube_list_kdy(request,keyword):
    return render(request, 'kdy_app/youtube_list_kdy.html',{'keyword':keyword})

def youtube_all_lists(request):
    youtube_all_lists = Youtube.objects.all()
    return render(request, 'kdy_app/youtube_all_lists.html', {'youtube_all_lists':youtube_all_lists})

def youtube_all_detail(request, youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)
    return render(request, 'kdy_app/youtube_all_detail.html', {'youtube':youtube})

# 등록
def youtube_insert(request):    
    if request.method == "POST":        
        form = YoutubeForm(request.POST)
        # 데이터 유효성 확인
        if form.is_valid():
            youtube = form.save(commit=False)            
            youtube.save()
            return redirect('youtube_all_lists')
    else:
        form = YoutubeForm()
    
    return render(request, 'kdy_app/youtube_all_insert.html', {'form':form})
        
# 수정
def youtube_update(request, youtube_id):  
    youtube = get_object_or_404(Youtube, pk=youtube_id)    
    if request.method == "POST":        
        form = YoutubeForm(request.POST, instance=youtube)        
        if form.is_valid(): # 저장 지연
            youtube = form.save(commit=False)
            youtube.save() # 저장
            return redirect('youtube_all_lists')
    else:
        form = YoutubeForm(instance=youtube)
        # 폼에 youtube_id 에 해당되는 상품 데이터 출력
    
    return render(request, 'kdy_app/youtube_all_update.html', {'form':form})

# 삭제
def youtube_delete(youtube_id):
    youtube = get_object_or_404(Youtube, pk=youtube_id)    
    youtube.delete()
    return redirect('youtube_list')

# 검색창 열기
def youtube_search_custom_form(request):
    return render(request, 'kdy_app/youtube_search_custom.html')

# 검색 쿼리 수행
def youtube_search_custom(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "youtube_title":
            youtube_list = Youtube.objects.filter(Q(youtube_title__contains=keyword)) 
        elif type == "youtube_channel_name":
            youtube_list = Youtube.objects.filter(Q(youtube_channel_name__contains=keyword))
        elif type == "youtube_hashtag":
            youtube_list = Youtube.objects.filter(Q(youtube_hashtag__contains=keyword))
        else: 
            pass

        return render(request, 'kdy_app/youtube_search_custom.html', {'youtube_list':youtube_list})

def youtube_search_ajax_form(request):
    return render(request, 'kdy_app/youtube_search_ajax.html')

def youtube_search_ajax(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "youtube_title":
            youtube_list = Youtube.objects.filter(Q(youtube_title__contains=keyword)) 
        elif type == "youtube_channel_name":
            youtube_list = Youtube.objects.filter(Q(youtube_channel_name__contains=keyword))
        elif type == "youtube_hashtag":
            youtube_list = Youtube.objects.filter(Q(youtube_hashtag__contains=keyword))
        else: 
            pass
        
        # youtube_list 쿼리 데이터 셋을 JSON 타입으로 변환
        youtube_list_json = json.loads(serializers.serialize('json', youtube_list, ensure_ascii=False))

        return JsonResponse({'reload_all':False, 'youtube_list_json':youtube_list_json})
    















# def book_search(request):
#     if request.method == "POST":
#         type = request.POST['type']
#         keyword = request.POST['keyword']

#         print(type, keyword)

#         if type == "bookname":
#             book_list = Book.objects.filter(Q(bookname__contains=keyword))
#         elif type == "bookauthor":
#             book_list = Book.objects.filter(Q(bookauthor__contains=keyword))
#         elif type == "pubname":
#             book_list = Book.objects.filter(Q(pubno__pubname__contains=keyword))
#         # elif type == "bookstock":
#         #     book_list = Book.objects.filter(Q(bookstock=keyword))
#         elif type == "bookprice":
#             book_list = Book.objects.filter(Q(bookprice=keyword))        
#         elif type == "bookprice":
#             price_range = keyword.split("-")  # 가격 범위 (-) 기준으로 분리
#             if len(price_range) == 2:
#                 min_price, max_price = price_range
#                 book_list = Book.objects.filter(Q(bookprice__gte = min_price, bookprice__lte = max_price))       
#         else:
#             return render(request, 'book_app/book_search_form.html')
        
#         return render(request, 'book_app/book_search_form.html', {'book_list':book_list})
    
#     else: # GET
#         return render(request, 'book_app/book_search_form.html')

# def book_search_form2(request):
#     return render(request, 'book_app/book_search_form2.html')

# # 검색 기능 수행하고 결과를 JsonResponse로 반환
# def book_search2(request):
#     if request.method == "POST":
#         # if 문으로 type or keyword 골라서 받기 구현
#         type = request.POST['type']
#         keyword = request.POST['keyword']
#         print(type, keyword)

#         if type == "bookname":
#             book_list = Book.objects.filter(Q(bookname__contains=keyword))
#         elif type == "bookauthor":
#             book_list = Book.objects.filter(Q(bookauthor__contains=keyword))
#         elif type == "pubname":
#             book_list = Book.objects.filter(Q(pubno__pubname__contains=keyword))
#         # elif type == "bookstock":
#         #     book_list = Book.objects.filter(Q(bookstock=keyword))
#         # elif type == "bookprice":
#         #     book_list = Book.objects.filter(Q(bookprice=keyword))              
#         elif type == "bookprice":
#             price_range = int(keyword.split("-"))  # 가격 범위 (-) 기준으로 분리
#             try:
#                 if len(price_range) == 2:
#                     min_price, max_price = price_range
#                     book_list = Book.objects.filter(Q(bookprice__gte = min_price, bookprice__lte = max_price))
#                 else:
#                     print("가격은 [ 최소-최대 ] 형식으로 숫자만 입력하세요")
#             except:
#                 print('올바른 형식으로 입력하세요')
                               
#         else:
#             print("검색조건을 선택하세요")

#         book_list_json = json.loads(serializers.serialize('json', book_list, ensure_ascii=False))

#         return JsonResponse({'reload_all':False, 'book_list_json':book_list_json})





















# def youtube_detail(request,keyword):    
#     # print(keyword)    

#     # 하위 주소를 토대로 관광지 리스트 쿼리 
#     addr = "제주 서귀포시 안덕면"
#     keywords = addr.split(" ")

#     if len(keywords) > 2 :
#         keyword = keywords[2]
#     else:
#         keyword = keywords[1]

#     # print(keyword)
#     # attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))[:3]
#     # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
#     #################################################################################
#     # 키워드를 포함한 리스트
#     keywords = ['용연구름다리', '화북포구', '아날로그감귤밭']  # 나머지 키워드들을 포함
#     # 초기 쿼리 생성
#     q_objects = Q(youtube_title__contains=keywords[0])
#     # 나머지 키워드들을 OR 조건으로 추가
#     for keyword in keywords[1:]:
#         q_objects |= Q(youtube_title__contains=keyword)
#     # 쿼리 실행
#     attraction_list = Youtube.objects.filter(q_objects)
#     #################################################################################
#     return render(request, 'kdy_app/youtube_detail.html', {'attraction_list':attraction_list}, keyword) 
  

# def naver_blog_list(request,keyword):
#     print(keyword)
#     return render(request, 'kdy_app/naver_blog_list.html',{'keyword':keyword}, {'youtube_title': youtube_title}) 


# def naver_blog_detail(request,keyword):
#     # 하위 주소를 토대로 관광지 리스트 쿼리 
#     addr = "제주 서귀포시 안덕면"
#     keywords = addr.split(" ")

#     if len(keywords) > 2 :
#         keyword = keywords[2]
#     else:
#         keyword = keywords[1]

#     # print(keyword)
#     # attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))[:3]

#     # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
#     #################################################################################
#     # 키워드를 포함한 리스트
#     keywords = ['용연구름다리', '화북포구', '아날로그감귤밭']  # 나머지 키워드들을 포함
#     # 초기 쿼리 생성
#     q_objects = Q(naver_blog_title__contains=keywords[0])
#     # 나머지 키워드들을 OR 조건으로 추가
#     for keyword in keywords[1:]:
#         q_objects |= Q(naver_blog_title__contains=keyword)
#     # 쿼리 실행
#     attraction_list = NaverBlog.objects.filter(q_objects)
#     #################################################################################
     
#     return render(request, 'kdy_app/naver_blog_detail.html', {'attraction_list':attraction_list})
