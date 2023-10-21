from django.db import models


class DailyHotel(models.Model):
    daily_hotel_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (daily_hotel_name, daily_hotel_address) found, that is not supported. The first column is selected.
    daily_hotel_address = models.CharField(max_length=255)
    daily_hotel_image_link = models.TextField(blank=True, null=True)
    daily_hotel_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    daily_hotel_link = models.TextField(blank=True, null=True)
    daily_hotel_date = models.DateField(blank=True, null=True)
    daily_hotel_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_hotel'
        unique_together = (('daily_hotel_name', 'daily_hotel_address'),)

class GoodChoice(models.Model):
    acc_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (acc_name, acc_address) found, that is not supported. The first column is selected.
    acc_address = models.CharField(max_length=255)
    acc_image_link = models.TextField(blank=True, null=True)
    acc_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    acc_link = models.TextField(blank=True, null=True)
    acc_date = models.DateField(blank=True, null=True)
    acc_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodchoice'
        unique_together = (('acc_name', 'acc_address'),)


class NaverBlog(models.Model):
    naver_blog_id = models.CharField(primary_key=True, max_length=10)
    naver_blog_title = models.CharField(max_length=200)
    naver_blog_link = models.TextField(blank=True, null=True)
    naver_blog_image = models.TextField(blank=True, null=True)
    naver_blog_hashtag = models.TextField(blank=True, null=True)
    naver_bloger_name = models.DateField(blank=True, null=True)
    naver_blog_content_likeit_count = models.IntegerField(blank=True, null=True)
    naver_blog_content_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_blog'


class NearAttraction(models.Model):
    place = models.OneToOneField('Place', models.DO_NOTHING, primary_key=True)  # The composite primary key (place_id, visitKorea_id) found, that is not supported. The first column is selected.
    visitKorea = models.ForeignKey('VisitKorea', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'near_attraction'
        unique_together = (('place', 'visitKorea'),)


class NearRestaurant(models.Model):
    place = models.OneToOneField('Place', models.DO_NOTHING, primary_key=True)  # The composite primary key (place_id, restaurant_id) found, that is not supported. The first column is selected.
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'near_restaurant'
        unique_together = (('place', 'restaurant'),)


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=200)
    place_address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'place'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_link = models.TextField(blank=True, null=True)
    restaurant_image = models.TextField(blank=True, null=True)
    restaurant_hashtag = models.TextField(blank=True, null=True)
    restaurant_shop_name = models.TextField(blank=True, null=True)
    restaurant_content_likeit_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    restaurant_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    restaurant_review_num_count = models.IntegerField(blank=True, null=True)
    restaurant_avg_price = models.IntegerField(blank=True, null=True)
    restaurant_shop_category = models.TextField(blank=True, null=True)
    restaurant_map_x = models.IntegerField(blank=True, null=True)
    restaurant_map_y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'

class Tripbtoz(models.Model):
    trip_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (trip_name, trip_address) found, that is not supported. The first column is selected.
    trip_address = models.CharField(max_length=255)
    trip_image_link = models.TextField(blank=True, null=True)
    trip_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    trip_link = models.TextField(blank=True, null=True)
    trip_date = models.DateField(blank=True, null=True)
    trip_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tripbtoz'
        unique_together = (('trip_name', 'trip_address'),)

# 2023-10-20 자료형 변경 - 김영재
class Visitkorea(models.Model):
    visitkorea_id = models.CharField(primary_key=True, max_length=20)   
    visitkorea_title = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_tel = models.CharField(max_length=50, blank=True, null=True)
    visitkorea_firstimage = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_address = models.CharField(max_length=255, blank=True, null=True)
    visitkorea_mapx = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    visitkorea_mapy = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    visitkorea_mlevel = models.IntegerField(blank=True, null=True)      
    visitkorea_overview = models.TextField(blank=True, null=True)       

    class Meta:
        managed = False
        db_table = 'visitkorea'


class Yanolja(models.Model):
    yanolja_name = models.CharField(primary_key=True, max_length=200)  # The composite primary key (yanolja_name, yanolja_address) found, that is not supported. The first column is selected.
    yanolja_address = models.CharField(max_length=255)
    yanolja_image_link = models.TextField(blank=True, null=True)
    yanolja_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    yanolja_link = models.TextField(blank=True, null=True)
    yanolja_date = models.DateField(blank=True, null=True)
    yanolja_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yanolja'
        unique_together = (('yanolja_name', 'yanolja_address'),)


class Youtube(models.Model):
    youtube_id = models.AutoField(primary_key=True)
    youtube_title = models.CharField(max_length=200)
    youtube_link = models.TextField(blank=True, null=True)
    youtube_image = models.TextField(blank=True, null=True)
    youtube_hashtag = models.TextField(blank=True, null=True)
    youtube_channel_name = models.DateField(blank=True, null=True)
    youtube_channel_count = models.IntegerField(blank=True, null=True)
    youtube_content_like_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    youtube_comment_like_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    youtube_content_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youtube'
