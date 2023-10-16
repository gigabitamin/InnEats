
# AI 백엔드 5차 세미 프로젝트 (231013-231026)
# TEAM def TROLL

* push 전 pull 확인 요망

* db = inneats_db

* db 생성 sql 문 

DROP SCHEMA inneats_db; -- > 이미 존재한다면 지우고 시작
CREATE SCHEMA inneats_db;
use inneats_db;

==============================================================



v0.1.0
django로 main page bootstrp 적용

nav에 로그인, 회원가입 추가 -> db에 user 테이블 정상작동

main page에서 메뉴링크 url.py view.py 에 전부 추가

수정중인 것 -> search 기능 추가

패키지 안에 수업때 배웠던 crud 연습용 product_app 추가되어 있으니 참고해서 만들 것

<div><a href="{% url 'product_list' %}">상품 정보 조회</a></div>
<div><a href="{% url 'product_insert' %}">상품 등록</a></div>
<div><a href="{% url 'product_search_form3' %}">상품 검색</a></div>

database / mysql 폴더안에 product.csv 들어있음, 아니면 본인들 db에 있는 product 테이블 사용




v0.0.2
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
사이트명 : InnEats

# 모델링 구조

- -----필수조건---------
1. 크롤링
2. CRUD 데이터베이스 구축 활용

<크롤링>
크롤링 - 
1여기어때(송지현) 
2야놀자(서민석), 
3데일리호텔(강대연), 
4트립비(허성태), 
5비짓코리아(김영재)


<추가 덤>

1. SNS 크롤링 (허성태)
2. 유튜브 크롤링 (서민석)
3. 맛집-관광지 (송지현) -> 1차 db 구축한 뒤에 시작
4. 카톡 api로 메세지 전송 & 메일링 (강대연)
5. 챗봇 상담 기능 -> 오픈 AI 활용 삼당사 역할 (김영재)

<덤의 덤>

1. 출석체크 게시판 : 달력에 도장찍듯이, 날수 채우면 쿠폰 
2. 익명) 개인 일기장 -> 쓰레드 형식


* db는 이미 전부 구축이 되어있다고 간주
<프론트엔드에 출력 >
1. 여기어때, 2야놀자, 3데일리호텔, - 같은화면에 출력 - (김영재)
2. 맛집 관광지 + 지도 - (송지현) 
3. 비짓코리아 - (서민석)
4. SNS 유튜브 - (강대연)
5. 메인페이지-고객센터 - (허성태)


<구체적 모델링>
1. 숙박업소를 긁어온뒤 겹치는 것들 합쳐서
가격이 다르면 각각의 사이트별 가격
-> view 테이블 하나로 합쳐서 새로운 테이블

2. 네이버 카톡 맵 api 인증키 -> (숙박업소)주소 토대로 주변 지역 맛집 관광지 -> 새로운 페이지

3. 검색 기능추가, 리스트 페이지의 박스 정보, 내부 페이지 텍스트랑 이미지 크롤링

4. 상세페이지 각각 sns 유투브 리스트업

5. 메인페이지 - 검색 기능, 
/ 고객센터 : 게시글 템플릿 복붙 








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

로고제작 : canva (AI를 활용한 이미지 생성도 가능)

