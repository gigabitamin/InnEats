
import os
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect

# 데이터베이스 필터링 관련
from django.db.models import Q
from .models import NaverBlog
from .models import Youtube
from .forms import YoutubeForm
from .forms import NaverBlogForm

# 메일링
from django.dispatch import receiver
from django.core.mail import send_mail
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈

# 이미지 업로드
from .forms import ImageForm

# 로그인 관련
from imaplib import _Authenticator
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from users_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

# 커스텀 유저 폼 마이페이지 관련
from .models import UsersAppUser
from .forms import UserInfoForm
from .forms import UserInfoForm_username
from .forms import UserInfoForm_email
from .forms import UserInfoForm_password
from .forms import UserInfoForm_user_name
from .forms import UserInfoForm_user_phone
from .forms import UserInfoForm_user_address
from .forms import UserInfoForm_preferred_accommodation_type_no
from .forms import UserInfoForm_preferred_tour_theme_type_no
from .forms import UserInfoForm_preferred_region_no




# 로그인시 해당 유저 이메일로 자동 메일 발송
def send_mail(to_email, inneats_user_id):
    # py 파일명이 email 일 경우 에러나니 변경할 것
    # 해당 기능 전체를 함수화해서 사용할 것, Class modeul로 빼는 것도 고려
    # def sendEmail (from_email, to_email, from_email_password, inneats_user_id): 

    # Gmail 계정에서 IMAP 설정
    # https://mail.google.com/mail/u/0/#settings/fwdandpop
    # 해당 설정에서 IMAP 을 사용상태로 open 해줘야 타클라이언트에서 gmail 전송 사용가능
    # https://myaccount.google.com/security
    # app_password = '본인 app password' # 2차 로그인을 하는 계정일 시 구글 보안설정에서 app 패스워드 설정 후 입력 필요

    # 발송자 정보
    from_email = '@gmail.com' # 보낼 계정
    from_email_password = ''

    # 수신자 정보
    to_email = '@gmail.com' # 수신할 계정 # 여러명에게 보낼 땐 [] 로 리스트 처리
    inneats_user_id = inneats_user_id

    # 보낼 내용
    now = datetime.now()
    send_subject = f'{inneats_user_id}님께서 {now}에 InnEats에 로그인 하셨습니다' # 제목
    text = f"\
        안녕하세요 {inneats_user_id}님\n\
        InnEats에 오신 것을 환영합니다"
    html = f"<html><body><h1>{now}</h1><p>{text}</p></body></html>"

    # 서버와 연결
    smtp_server = 'smtp.gmail.com' # gmail smtp 주소
    smtp_port = 465  # gmail smtp 포트번호
    server = smtplib.SMTP_SSL(smtp_server, smtp_port) # SMTP 객체
    
    # 로그인
    server.login(from_email, from_email_password)
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart("alternative")
    msg["Subject"] = send_subject
    msg["From"] = from_email
    msg["To"] = to_email

    # 메일 본문 _email내용
    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")
    msg.attach(text_part)
    msg.attach(html_part)
    
    # 이미지 파일 추가
    # image_path = "{% static 'img/logo/inneats/InnEats_logo_temp.png' %}" --> load static 실행 안됨, 절대 결로 or 상대 경로 처리
    # image_path = "C:\djangoWorkspace/InnEats_logo_temp.png"
    # image_path = "../../../static/img/logo/inneats/InnEats_logo_temp.png"
    
    image_path = os.path.join(settings.STATIC_ROOT, 'img/kdy/logo/inneats/InnEats_logo_temp.png')
    
    # 'rb' read binary, 2진 데이터로 처리 -> 이미지 로딩 가능
    with open(image_path, 'rb') as file: 
        img = MIMEImage(file.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_path)
        msg.attach(img)
    
    # 받는 메일 유효성 검사 거친 후 메일 전송
    # 올바른 형식으로 보내는지 정규식 검사
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    try:
        if re.match(reg, to_email):
            server.sendmail(from_email, to_email, msg.as_string())
            print("정상적으로 메일이 발송되었습니다")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오")
    except Exception as e:
        print("error", e)
    
    # smtp 서버 연결 해제
    server.quit()

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    # 사용자 정보에서 이메일 주소 가져오기
    user_email = user.email
    inneats_user_id = user.username
    # 이메일 보내기
    send_mail(user_email, inneats_user_id)



# 세션 처리 문제
# @receiver(user_logged_in, dispatch_uid="set_session")
# def set_session(sender, request, user, **kwargs):
#     user_info = user
#     request.session['id'] = user_info.id
#     return HttpResponse("Session data set.")

# @receiver(user_logged_in, dispatch_uid="get_session")
# def get_session(sender, request, user, **kwargs):
#     user_id = request.session.get('id')  # 세션에서 데이터 읽기
#     return HttpResponse(f"User ID: {user_id}")

# @receiver(user_logged_in, dispatch_uid="get_session")
# def login_view(sender, request, user, **kwargs):
#     if request.method == 'POST':
#         username = request.POST['username']
#         user = _Authenticator(request, username=username, password='password')
#         if user:
#             login(request, user)
#             # 클라이언트 측 로컬 스토리지에 로그인 정보 저장
#             response = JsonResponse({'message': '로그인 성공'})
#             response.set_cookie('user', username, max_age=settings.SESSION_COOKIE_AGE) # 3일
#             return response
#         else:
#             return JsonResponse({'message': '로그인 실패'})






# 유저 선호도에 따른 필터링 결과 출력

# @login_required
def naver_blog_list_user(request):
    user_info = request.user  # 현재 로그인한 사용자
    preferred_region_no = get_user_preferred_region(user_info.username) # 테마 타입이 일치하는 유저 정보 

    if preferred_region_no:
        naver_blog_data = NaverBlog.objects.filter(naver_blog_title__icontains=preferred_region_no)
    else:
        naver_blog_data = None

    naver_blog_list = Youtube.objects.all()
    # 추천영상 알고리즘에 포함
    if len(naver_blog_data) > 1:
        naver_blog_data1 = naver_blog_data[0]
    else:
        naver_blog_data1 = naver_blog_list[0]
    grouped_naver_blog_list = [naver_blog_list[i:i+3] for i in range(0, len(naver_blog_list), 3)]
    return render(request, 'kdy_app/naver_blog_list.html', {'naver_blog_data1':naver_blog_data1, 'naver_blog_data':naver_blog_data, 'naver_blog_list':naver_blog_list, 'grouped_naver_blog_list': grouped_naver_blog_list})


# 유저 로그인 시 해당 유저가 설정한 선호 지역 숙소 테마 등을 키워드로 필터링해서 출력
@login_required
def youtube_list_user(request):
    user_info = request.user  # 현재 로그인한 사용자
    preferred_region_no = get_user_preferred_region(user_info.username) # 테마 타입이 일치하는 유저 정보 

    if preferred_region_no:        
        youtube_data = Youtube.objects.filter(youtube_title__icontains=preferred_region_no)
    else:
        youtube_data = None

    youtube_list = Youtube.objects.all()
    # 추천영상 알고리즘에 포함
    if len(youtube_data) > 1:
        youtube_data1 = youtube_data[0]
    else:
        youtube_data1 = youtube_list[0]
    grouped_youtube_list = [youtube_list[i:i+3] for i in range(0, len(youtube_list), 3)]
    return render(request, 'kdy_app/youtube_list.html', {'youtube_data1':youtube_data1, 'youtube_data':youtube_data, 'youtube_list':youtube_list, 'grouped_youtube_list': grouped_youtube_list})



# 선호 지역을 받아오는 함수

def get_user_preferred_region(username):
    try:
        user_profile = UsersAppUser.objects.get(username=username)

        return user_profile.preferred_region_no.preferred_region
    except UsersAppUser.DoesNotExist:
        return None

# 선호 숙소 형태를 받아오는 함수
def get_user_preferred_accommodation_type(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.preferred_accommodation_type_no.preferred_accommodation_type
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None

# 선호 테마를 받아오는 함수
def get_user_preferred_tour_theme_type(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.preferred_tour_theme_type_no.preferred_tour_theme_type
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None

# 유저 테이블에 저장된 해당 유저의 주소정보를 받아오는 함수
def get_user_address(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UsersAppUser.objects.get(user=user)
        return user_profile.user_address
    except User.DoesNotExist:
        return None
    except UsersAppUser.DoesNotExist:
        return None


# 로그인한 유저가 회원가입시 지정한 테마 타입을 키워드로 반환
@login_required
def youtube_user_preferred_tour_theme_type(request):
    user_info = request.user # 로그인 유저 정보 저장
    preferred_tour_theme_type_no = get_user_preferred_region(user_info.id) # 테마 타입이 일치하는 유저 정보 

    if preferred_tour_theme_type_no:
        # 'preferred_tour_theme_type_no' 변수의 'preferred_tour_theme_type' 값이 'Youtube' 모델의 'youtube_title' 필드에 포함되는 비디오를 검색
        youtube_user_preferred_tour_theme_type = Youtube.objects.filter(youtube_title__icontains=preferred_tour_theme_type_no.preferred_tour_theme_type)
    else:
        youtube_user_preferred_tour_theme_type = None        

    return render(request, 'your_app/youtube_list.html', {'youtube_user_preferred_tour_theme_type': youtube_user_preferred_tour_theme_type})

@login_required
def youtube_user_address_login(request):
    user_info = request.user
    return render(request, 'kdy_app/youtube_list.html', {'user_info': user_info})

@login_required
def youtube_user_address(request):
    user_info = request.user
    user_address = get_user_address(user_info.id)

    if user_address:        
        youtube_user_address = Youtube.objects.filter(address=user_address)
    else:        
        youtube_user_address = None

    return render(request, 'your_app/youtube_list.html', {'youtube_user_address': youtube_user_address})








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
            return redirect('index')
    else:
        user_form = UserInfoForm(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})


def my_page_update_username(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_username(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_username(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})


def my_page_update_email(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_email(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_email(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

def my_page_update_password(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_password(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_password(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

def my_page_update_user_name(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_user_name(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_user_name(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

def my_page_update_user_phone(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_user_phone(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_user_phone(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

def my_page_update_user_address(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_user_address(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_user_address(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})



def my_page_update_preferred_region_no(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_preferred_region_no(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_preferred_region_no(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})



def my_page_update_preferred_accommodation_type_no(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_preferred_accommodation_type_no(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_preferred_accommodation_type_no(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

def my_page_update_preferred_tour_theme_type_no(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm_preferred_tour_theme_type_no(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('index')
    else:
        user_form = UserInfoForm_preferred_tour_theme_type_no(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update.html', {'user_form':user_form, 'user_info':user_info})

















def my_page_update_custom(request, id):  
    user_info = get_object_or_404(UsersAppUser, pk=id)    
    if request.method == "POST":
        user_form = UserInfoForm(request.POST, instance=user_info)
        if user_form.is_valid():
            user_info = user_form.save(commit=False)
            user_info.save()
            return redirect('my_page', user_info.id)
    else:
        user_form = UserInfoForm(instance=user_info)
    
    return render(request, 'kdy_app/my_page_update_custom.html', {'user_form':user_form, 'user_info':user_info})


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
        naver_blog_data1 = naver_blog_data[0]
    else:
        naver_blog_data1 = naver_blog_list[0]

    grouped_naver_blog_list = [naver_blog_list[i:i+3] for i in range(0, len(naver_blog_list), 3)]
    
    return render(request, 'kdy_app/naver_blog_list.html', {'naver_blog_data1':naver_blog_data1, 'naver_blog_data':naver_blog_data,'naver_blog_list':naver_blog_list, 'grouped_naver_blog_list': grouped_naver_blog_list, 'keyword':keyword})

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
        youtube_data1 = youtube_data[0]
    else:
        youtube_data1 = youtube_list[0]
    grouped_youtube_list = [youtube_list[i:i+3] for i in range(0, len(youtube_list), 3)]
    return render(request, 'kdy_app/youtube_list.html', {'youtube_data1':youtube_data1, 'youtube_data':youtube_data, 'youtube_list':youtube_list, 'grouped_youtube_list': grouped_youtube_list, 'keyword':keyword})

    # 3개씩 묶어서 출력 -> for 문 출력시 css 문제로 1개씩 출력할경우 1개별로 행이 달라지는 문제가 발생, 3개씩 미리 구성후 한 행에 3개씩 출력
    # if len(youtube_list) % 3 == 0:
    #     print()
    # for i in grouped_youtube_list
    # grouped_youtube_list[0]
    # grouped_youtube_list[1]
    # grouped_youtube_list[2]
    
    
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
    





