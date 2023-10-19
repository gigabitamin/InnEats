-- inneats_db 생성
DROP SCHEMA inneats_db;
CREATE SCHEMA inneats_db;
use inneats_db;

CREATE TABLE product AS
SELECT * FROM django_db.product;

-- django_db 생성
DROP SCHEMA django_db;
CREATE SCHEMA django_db;
use django_db;


-- projectex_db 생성
DROP SCHEMA projectex_db;
CREATE SCHEMA projectex_db;
use projectex_db;

-- django_db에 있는 product 테이블을 임시로 sldb1 데이터베이스로 이동했다가
CREATE TABLE product AS
SELECT * FROM django_db.product;

CREATE TABLE book AS
SELECT * FROM django_db.book;

CREATE TABLE publisher AS
SELECT * FROM django_db.publisher;

-- User 생성 / 마이그레이션 작업 끝내고 다시 원래대로 복사함
CREATE TABLE product AS
SELECT * FROM sqldb1.product;

CREATE TABLE book AS
SELECT * FROM sqldb1.book;

CREATE TABLE publisher AS
SELECT * FROM sqldb1.publisher;

-- inneats_db 생성
DROP SCHEMA inneats_db;
CREATE SCHEMA inneats_db;
use inneats_db;


 -- NULL 가능(예약 취소시)
CREATE TABLE goodchoice (
    acc_name VARCHAR(200) NOT NULL,
    acc_address VARCHAR(255) NOT NULL,
    acc_image_link TEXT,
    acc_rating DECIMAL(3,1),
    acc_link TEXT,
    acc_date date,
    acc_price int,
    PRIMARY KEY (acc_name, acc_address)
);

CREATE TABLE yanolja (
    yanolja_name VARCHAR(200) NOT NULL,
    yanolja_address VARCHAR(255) NOT NULL,
    yanolja_image_link TEXT,
    yanolja_rating DECIMAL(3,1),
    yanolja_link TEXT,
    yanolja_date date,
    yanolja_price int,
    PRIMARY KEY (yanolja_name, yanolja_address)
);

CREATE TABLE daily_hotel (
    daily_hotel_name VARCHAR(200) NOT NULL,
    daily_hotel_address VARCHAR(255) NOT NULL,
    daily_hotel_image_link TEXT,
    daily_hotel_rating DECIMAL(3,1),
    daily_hotel_link TEXT,
    daily_hotel_date date,
    daily_hotel_price int,
    PRIMARY KEY (daily_hotel_name, daily_hotel_address)
);

CREATE TABLE tripbtoz (
    trip_name VARCHAR(200) NOT NULL,
    trip_address VARCHAR(255) NOT NULL,
    trip_image_link TEXT,
    trip_rating DECIMAL(3,1),
    trip_link TEXT,
    trip_date date,
    trip_price int,
    PRIMARY KEY (trip_name, trip_address)
);


-- search_query=제주 -> select 변수처리?

CREATE TABLE youtube (
	youtube_id int not null auto_increment,
    youtube_title VARCHAR(200) NOT NULL,
	youtube_link TEXT,
    youtube_image text,
    youtube_hashtag TEXT,
    youtube_channel_name date,
    youtube_channel_count int,
    youtube_content_like_count DECIMAL(3,1),
    youtube_comment_like_count DECIMAL(3,1),
    youtube_content_date date,
    PRIMARY KEY (youtube_id)    
);

CREATE TABLE naver_blog (
	naver_blog_id varchar(10) not null,
    naver_blog_title VARCHAR(200) NOT NULL,
	naver_blog_link TEXT,
    naver_blog_image text,
    naver_blog_hashtag TEXT,
    naver_bloger_name date,
    naver_blog_content_likeit_count int, -- 공감수
    naver_blog_content_date date,
    PRIMARY KEY (naver_blog_id)    
);


CREATE TABLE restaurant (
	restaurant_id int not null auto_increment,
	restaurant_link TEXT,
    restaurant_image text,
    restaurant_hashtag TEXT,
    restaurant_shop_name text,
    restaurant_content_likeit_count DECIMAL(3,1), -- 공감수
    restaurant_rating DECIMAL(3,1),
    restaurant_review_num_count int,
    restaurant_avg_price int,
    restaurant_shop_category text,
    restaurant_map_x int,
    restaurant_map_y int,    
    PRIMARY KEY (restaurant_id)
);


-- visitkorea - 관광지 정보
-- -------------------------------------
CREATE TABLE visitkorea  (
visitkorea_id varchar(20) NOT NULL,
visitkorea_title varchar(50),
visitkorea_tel varchar(20) null,
visitkorea_firstimage varchar(100),
visitkorea_address varchar(50),
visitkorea_mapx float, -- 위치 정보 크롤링 가능? 확인 요망
visitkorea_mapy float,
visitkorea_mlevel int,
visitkorea_overview longtext,
PRIMARY KEY (visitkorea_id)
);


CREATE TABLE place (
    place_id int not null auto_increment,
    place_name VARCHAR(200) NOT NULL,
    place_address VARCHAR(255) NOT NULL,
    PRIMARY KEY (place_id)
);

INSERT INTO place (place_name, place_address)
SELECT daily_hotel_name, daily_hotel_address FROM daily_hotel
UNION
SELECT yanolja_name, yanolja_address FROM yanolja
UNION
SELECT acc_name, acc_address FROM goodchoice
UNION
SELECT trip_name, trip_address FROM tripbtoz;

CREATE TABLE near_restaurant (
    place_id int not null,
    restaurant_id int not null,    
    PRIMARY KEY (place_id, restaurant_id),
	FOREIGN KEY (place_id) REFERENCES place(place_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id)    
);

CREATE TABLE near_attraction (
    place_id int not null,
    visitkorea_id varchar(20) not null,
    PRIMARY KEY (place_id, visitkorea_id),
	FOREIGN KEY (place_id) REFERENCES place(place_id),
    FOREIGN KEY (visitkorea_id) REFERENCES visitkorea(visitkorea_id)
);











