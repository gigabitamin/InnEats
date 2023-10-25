# AI 백엔드 5차 세미 프로젝트 (231013-231026)
# TEAM def TROLL

<<<<<<< HEAD
hst
==============================================================

=======
develop부터 hotfix featherr 각자 수정하면서 올리시던 버전 전부 pull 해와서 임시취합후 오류 수정을 한 뒤 develop에 올립니다
각자 pull 하시고 빠지거나 충돌나는 부분 수정한 후 각자 본인 브런치에 올려주세요
일단 develop은 v0.5.0 유지 하겠습니다
오전에 확인 후 이상 없으면 main 에도 merge 해놓겠습니다

==============================================================

0.5.0 / kdy
회원가입 css 수정
my_page css 적용 완료
회원 정보 수정 추가
회원탈퇴 추가
로그인 사용자만 본인 정보 my_page 보이도록 수정
미로그인 사용자가 클릭할 경우 로그인 페이지로 자동 이동하도록 수정
hst sjh sms 각 멤버별 임시 취합버전 models, forms 등 기타 오류 수정 -> 정상 구동 확인

0.4.9 /
sms / acctraction_app 생성
>>>>>>> 585b53b5ab95385086c1bffc6ab4e07dcd82554d

0.4.8 / 
hst / search 앱 생성
kyj / 유투브 크롤링 데이터 db 업로드 완료 
kdy / kdy_app inneats_app forms models 유투브 fields 수정 
-> 유투브 클릭시 정상구동 #주의사항:kyj님꼐서 올려놓은 sql 명령문으로 유투브 테이블 만든 후 youtube db import 한 뒤에 유투브 페이지 들어갈 것
-> row가 895개로 데이터가 많아서 페이지 로딩시 오래걸리니 주의

0.4.7 / kdy / 
user 테이블에 선호 여행 지역, 선호 숙박 형태, 선호 여행 테마 추가
회원가입 form에 위의 3개 column 추가
마이 페이지 구현 (현재 user_id = '6' 고정)
slack에 올려놓은 kdy_user_table_etc_231024_1314.sql import 하신 후 마이페이지 접속


0.4.6 / kdy / 
user 테이블에 profile_image 컬럼 생성
setting.py 에 MEDIA_URL = '/media/' 미디어 경로 추가
kdy_app models.py user 테이블 수정
kdy_app forms.py 이미지 업로드 form 추가

0.4.5 / kdy
sjh_app 부트스트랩 충돌로 map 부트스트랩 css 파일 2개 주석 처리 -> 해결
accommodation_app 페이지에서 페이지 출력 오류 확인 -> merge 할때 기존 버전과 코드가 섞인 상태로 꼬인걸 발견하고 수정해서 해결

0.4.4 / sjh
sjh_app 지도 페이지 추가, 네비게이션에 sjh_app 추가

0.4.3 / kdy
갱신 확인용

0.4.2 / kdy
-- inneats_app models.py 추가 변경
-- kdy_app 블로그 페이지 추가
-- nav.html 블로그 링크 추가

0.4.1 / kdy 
-- 카카오톡 메세지 공유 기능 추가 (footer에 버튼 추가, kdy 폴더에 kakao_message.html 추가)
-- 카카오톡 디자인 가이드 static img 폴더에 다운받아서 추가
-- https://developers.kakao.com/tool/resource/login
-- web 경로 포함된 카카오 js 파일 js 폴더에 넣은 뒤 <HEAD>에 경로처리
-- base.html에 kakao_message.html include
-- inneats_project / urls.py 에서 accommodation_app 루트 수정
-- kdy_app 생성 (nav.html 에서 링크메뉴 추가)
-- 페이지별로 {% block title %} {{ keyword }}{% endblock %} 추가



v0.4.0 / 
-- accommodation 페이지 추가 -> accommodation_app 에서 담당(kyj) 
-- 카톡 상담하기 base.html에 추가 
-- 





-- v.0.3.1 여기까지 kdy 작업

v.0.3.1 / 
models.py, forms.py 추가 및 수정

v.0.3.0 /
index.html, base.html load 방식 변경

변경전
같은 페이지에서 비동기 방식으로 회원가입, 로그인

변경후
회원가입 로그인 시 users/sign_up2 새로운 페이지로 이동
회원가입, 로그인 login.css 추가 적용

페이지 하단 script 부분 base.html 에 옮긴 뒤 개별 페이지 script는 제거

index.html 에서 nav 부분 nav.html로 분리해서 base.html % block 위에 위치시킴
{% include "nav.html" %}
{% block content %}  
{% endblock content %}

공통된 nav 환경을 유지하기 위해 새로운 페이지를 만들 경우 꼭 해당 페이지에서 Navbar 와 하단에 위치해있는 script 목록들을 제거한 뒤 
{% extends 'base.html' %} 
로 base.html 을 불러와 상속으로 해결할 것

bootstrap 원본에서 변경한 부분
nav.html 36라인 class="btn btn-primary px-3 d-none d-lg-flex 주석처리 후 옆에 회원가입, 로그인 div 박스 새로 삽입
회원가입 로그인 관련 css -> login.css

product_app 삭제

기타 html 파일 inneats_app templates 하위 폴더로 이동

이전 페이지 url 주소가 다음페이지로 넘어갈 때 중첩되는 문제
-> 위의 설명한 방식으로 해결 완료
-> nav 중첩시 js 에서 오류발생

최종적으로 각 페이지 구조는 아래와 같을 것

{% extends 'base.html' %}
{% load static %}
{% block content %}

    <div class="container-xxl bg-white p-0">
        <!-- Navbar Start -->
            제거된 Nav 자리
        <!-- Navbar End -->
    </div>

{% endblock content %}

각 페이지별로 정상구동 확인
단, http request 가 필요한 CONTACT 페이지 구글맵과 같은 기능은 127.0.0.1과 같은 로컬서버에서 동작 불가능






v0.2.0 /

models.py
프로젝트에서 구상한 전 테이블 models.py에 추가

forms.py
숙소정보 제공업체 4곳에 관한 모델링 완료
Goodchois -> Goodchoice 로 수정



v0.1.0 / 

django로 main page bootstrp 적용

nav에 로그인, 회원가입 추가 -> db에 user 테이블 정상작동

main page에서 메뉴링크 url.py view.py 에 전부 추가

수정중인 것 -> search 기능 추가

패키지 안에 수업때 배웠던 crud 연습용 product_app 추가되어 있으니 참고해서 만들 것

database / mysql 폴더안에 product.csv 들어있음, 아니면 본인들 db에 있는 product 테이블 사용




v0.0.2 /

변경사항 : project 패키지 경로명 변경 InnEats_project -> inneats_project

- 패키지 경로에 대문쟈가 포함되는건 안좋은 예라는 걸 알아서 경로 변경해서 새로 만듬
- pull 새로 할 것

- 데이터베이스 이름은 inneats_db -> 본인 IDE에서 유저 기능 테스트 용으로 migrate 진행시 db 이름 확인할 것
- "NAME": "inneats_db"

- users_app 폴더에 로그인 회원가입 model form 정보 포함되어 있음
- migrate 시 진행 순서는 users_app 개별앱 migrate -> 전체에 migrate

- python manage.py makemigrations users_app
- python manage.py migrate users_app

- python manage.py makemigrations
- python manage.py migrate











-------------------------------------------------

## 프로젝트 사이트명
InnEats

## 프로젝트 팀명
def TROLL


## 프로젝트 주제 및 개요

프로젝트 주제 
지역별 숙박업소를 중심으로 한 주변 여행 테마별 정보 제공

선정 배경
1. 수요 활성화
코로나 종식, 관광 수요가 증가 함으로 관광 사업의 활성화 예상
2. 시장의 니즈 파악
최근 여행 플랫폼들이 다양해지고 있지만, 숙박을 중심으로 한 종합적인 정보 제공은 부족한 상황

기대효과
1. 효율적인 정보 탐색 
사용자는 여러 웹사이트나 앱을 돌아다닐 필요 없이 한 플랫폼에서 숙박과 관련된 모든 정보를 얻을 수 있습니다.
2. 향상된 사용자 경험 
SNS 해시태그 기능, 여러 숙박업체의 비교 기능 등을 통해 사용자는 더욱 풍부하고 실시간적인 정보를 얻을 수 있습니다.
3. 사용자 맞춤 추천 
로그인 사용자의 정보를 바탕으로 선호도와 행동 패턴을 기반으로 한 맞춤 추천 기능으로, 사용자의 만족도를 높일 수 있습니다.
4. 확장성 
테마 투어, 지역 테마 등 다양한 확장 가능성을 통해 지속적으로 콘텐츠를 업데이트하며 사용자를 끌어들일 수 있습니다.




## 프로젝트 수행 방향 (주요 기능 설명)

### 요약
숙박장소에 관한 상세 정보 제공
숙박 업체 가격 비교
원하는 조건으로 숙박업소 검색 필터링
주변 관광 명소에 대한 상세 정보 제공
여행 목적지와 관련된 동영상 및 SNS 리뷰와 팁 제공
지도 맵을 활용한 주변 관광지, 맛집 등의 위치 및 상세 정보 제공

### 구현 기능 상세 설명
<숙박정보 제공사이트 크롤링 및 정보 활용>
1.웹 크롤링 기술 활용
여러 숙박정보 제공 사이트에서 필요한 정보를 자동으로 수집하기 위해 웹 크롤링 기술을 활용합니다
2.가격 비교 및 분석
크롤링한 데이터를 기반으로 숙박 요금을 비교하고, 미리 정한 기준에 따라 사용자에게 제공합니다
3.필터 및 정렬 기능
사용자가 원하는 조건에 따라 검색 결과를 필터링하고 정렬할 수 있는 기능을 구현하여 고객이 원하는 숙소를 선택할 수 있도록 합니다

<공공데이터와 API를 활용한 관광지 정보 수집 및 활용>
1. 공공데이터 활용
공공데이터를 활용해 다양한 지역별 관광지 정보를 수집하고,  숙박 장소를 중심으로 주변 관광 명소에 대한 상세한 정보를 사용자에게 제공하여 다양한 여행 플랜을 제시합니다
2. 네이버 검색 API 활용
네이버 검색 API를 이용하여 주변 관광지, 맛집 등에 대한 블로그 등에 관한 내용을 효율적으로 검색하여 정보를 수집하고, 공감수가 많은 글이나 최신 리뷰 등을 찾아 제공함으로 사용자가 성공적인 여행 플랜을 수립할 수 있도록 도움을 줍니다
3. 동영상 리뷰 제공 
유튜브 동영상을 크롤링하여 해당 지역의 관광지와 맛집에 관한 다양한 시각적 영상 리뷰를 제공합니다
4. 지도 API 활용
지도 API를 활용하여 숙박 장소를 중심으로 주변 맛집과 관광지 정보를 표시하고, 위치와 거리를 시각적으로 확인하여 사용자가 주변 정보를 쉽게 파악하고 목적지를 보다 쉽게 찾아 갈 수 있도록 도움을 줍니다.





## 데이터베이스 설계
### <주요 테이블 구조>
#### [기본 DB 테이블]
1. 숙박정보 제공사이트 테이블
공통: 숙소명, 주소, 이미지url, 별점, 숙소정보 url, 예약가능 일자, 예약가격
goodchice 여기요
yanolja 야놀자
daily_hotel 데일리 호텔 
tripbtoz 트립비토즈 

2. 기타 테이블
visitkorea : 관광지 정보 테이블 (대한민국 방방곡곡 사이트 크롤링 데이터)
restaurant : 맛집정보 데이터 테이블 (지도 API 연계)
naver_blog 네이버 블로그 검색결과 테이블
youtube : 유투브 검색결과 테이블

#### [기본 DB를 활용한 테이블 모델]
1. place :
숙박업소 정보제공 사이트(4개)의 DB를 활용하여 생성
place_name(숙박업소명), place_address(숙박업소 주소)만 존재 (중복제거)

2. near_attraction :
place, visitkorea 테이블을 활용하여 생성
visitkorea 테이블의 정보 중에서 place 테이블의 항목을 비교하여 위치정보(주소지 혹은 경도,위도)에 매칭되는되는 정보를 near_attraction 테이블에 저장

3. near_restaurant :
place, restaurant 테이블을 활용하여 생성
restaurant 테이블의 정보 중 place 테이블의 항목을 비교하여 위치 정보(주소지 혹은 경도,위도)에 매칭되는 정보를 near_restaurant 테이블에 저장



## UI 설계 화면 구성 (사이트 맵)
https://www.notion.so/b2bc5713c6844b969d706f51eb41507b?pvs=4

Main - Search, Login & Logout
    - About, Contact US
    - 숙박업소, 주변맛집
    - 유투브, 블로그
    - 관광지, 여행지도



<kdy>
크롤링 : 데일리호텔
DB활용 : 
SNS 유튜브 크롤링 데이터 활용해서 상세 출력 페이지
카톡 api로 메시지 전송 & 메일링

<kyj>
크롤링 : 비짓코리아 - 방방곡에서 api를 제공해 주어 해당 데이터를 다운
DB활용 : 
1.여기어때, 2.야놀자, 3.데일리호텔, 4.트립비토즈 - 같은 화면에 출력 
챗봇 상담 기능 -> 오픈 AI 활용 상담사 역할

<sms>
크롤링 : 야놀자, 유투브
DB활용 : 비짓코리아 방방곡곡 크롤링한 데이터에 검색 기능추가, 리스트 페이지의 박스 정보, 내부 페이지 텍스트랑 이미지 크롤링

<sjh>
크롤링 : 여기어때 
DB활용 : 지도 api 활용 -> (숙박업소)주소 토대로 주변 지역 맛집 관광지를 지도를 활용해 시각적 표현

<hst>
크롤링 : 트립비, 네이버 블로그
DB활용 :
메인페이지 검색 기능 구현
고객센터 : 게시글 템플릿

<덤. 역할배정 미정> 
1. 출석체크 게시판 : 달력에 도장찍듯이, 날수 채우면 쿠폰 -> 사이트에서 활용
2. 익명 개인 일기장 -> 쓰레드 형식<프론트엔드에 출력 
3. 사이트 내 자체 평가점수 알고리즘




## <팀 일정 목록>
주제 선정(16일 오전)
전체 시안 개요 완성(16일 오전)
전체 레이아웃 구상(16일 오전)
부트스트랩 선정 및 기본페이지에 적용 테스트(16 오후)
모델링 설계 구상 (16일)
크롤링 방식 테스트 (16일)
최종 모델링별 페이지 기능 멤버별로 분배(16일)

개별 모델링 구상 점검(17일 오후)
개별 크롤링 시행오류 점검 (17일 오후)
기획안 제출본 최종 작성(17일 오후)

기획안 제출(18일)

개별 디자인 완성도 점검 (19일 오후)

자체 발표 중간(20일 오후)

프로젝트 중간 취합 점검(23일 오후)

자체 발표 최종(25일 오후) -> 최종 취합

세미 프로젝트 조별 발표(26일)


## 팀규칙 
<기타 규칙>
모르면 물어보기
자리를 비울땐 미리 말하기

<깃허브 규칙>
1. main branch(버전 관리 및 최종 업데이트 용, 팀장만 권한)
2. develop 브런치(개발용 브런치 수정 및 상시 업데이트)

<네이밍 규칙>
1. 기본적으로 카멜 표기법 
- 단어는 그대로 연결하되 이어지는 단어의 첫글자는 대문자 
   ex) defTroll
2. 단어는 최대한 풀로 쓰고 축약어 지양

<회의 일정>
1. 정기 회의시간 : 수업 중 오후
2. 점검 용 자체발표 : 20일, 25일




## 기술 스택 및 툴

### <사용 언어>

- HTML, CSS, Javscript, jquery, Python, MYSQL, django

### <작업 환경>

- vscode
- jupyter notebook

### <협업 툴>

- github : 팀원간 작업 수행물 공유 & 버젼 관리 및 rollback 용 데이터 백업
- zoom : 수업 중 소회의실 사용
- whaleon (ZOOM대신, 시간무제한) : BUT, 캠 필요 x, 필요시 디스코드로 대체
- discord : 음성채팅, 화면공유 가능, 간단한 전달사항은 슬랙으로 대체
- slack : 팀 소통 기본 메신져 (ZOOM 채팅은 휘발성), 코드 업로드 & 리뷰
- notion : 프로젝트 일정 및 공지 가이드 & 선택자, 변수명 등에 관한 네이밍 규칙 사전 & 각 팀원별 개발상황
- miro : 실시간 온라인 공유 메모지 화이트보드
- 구글문서 : 실시간 팀원들과 문서공유 후 참여 회의록 작성


### <기타 프로젝트 진행에 도움이 된 사이트>

로고제작 : 
- canva (AI를 활용한 이미지 생성도 가능)
- 부트스트랩 : 
- [Bootstrap 시작하기 · Bootstrap v5.3 (getbootstrap.kr)](https://getbootstrap.kr/docs/5.3/getting-started/introduction/)
- [LayoutIt! - Interface Builder for CSS Grid and Bootstrap](https://www.layoutit.com/)
- [Free Bootstrap Themes, Templates, Snippets, and Guides - Start Bootstrap](https://startbootstrap.com/)
- [draw.io (diagrams.net)](https://app.diagrams.net/)
