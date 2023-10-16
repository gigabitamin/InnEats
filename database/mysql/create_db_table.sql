
-- django_db에 있는 product 테이블을 임시로 sldb1 데이터베이스로 이동했다가
CREATE TABLE product AS
SELECT * FROM django_db.product;

CREATE TABLE book AS
SELECT * FROM django_db.book;

CREATE TABLE publisher AS
SELECT * FROM django_db.publisher;

DROP SCHEMA django_db;
CREATE SCHEMA django_db;
use django_db;

DROP SCHEMA projectex_db;
CREATE SCHEMA projectex_db;
use projectex_db;

-- User 생성 / 마이그레이션 작업 끝내고 다시 원래대로 복사함
CREATE TABLE product AS
SELECT * FROM sqldb1.product;

CREATE TABLE book AS
SELECT * FROM sqldb1.book;

CREATE TABLE publisher AS
SELECT * FROM sqldb1.publisher;




