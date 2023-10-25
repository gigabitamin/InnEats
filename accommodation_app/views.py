from django.shortcuts import render
from django.db.models import Q
from inneats_app.models import Visitkorea
from inneats_app.models import Youtube
from inneats_app.models import Accommodation

# Create your views here.
def accommodation(request,keyword):    
    # print(keyword)    
    # 우도면
    # q_objects = Q(visitkorea_title__contains=keyword)

    accommodation_list = Accommodation.objects.filter(Q(address__contains=keyword))
    return render(request, 'accommodation_app/accommodation.html',{'keyword':keyword, 'accommodation_list':accommodation_list})


def accommodation_detail(request, accommodation_id):     

    # 하위 주소를 토대로 관광지 리스트 쿼리 
    # addr = "제주 서귀포시 안덕면"
    accommodation = Accommodation.objects.get(Q(id=accommodation_id))
    keywords = accommodation.address.split(" ")

    if len(keywords) > 2 :
        keyword = keywords[2]
    else:
        keyword = keywords[1]

    attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))

    if len(attraction_list) == 0:
        attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keywords[1]))



    # youtube_list = Youtube.objects.filter(Q(visitkorea_address__contains=keywords))

    # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
    #################################################################################
    # 키워드를 포함한 리스트
    keywords = [attr.visitkorea_title for attr in attraction_list]  # 나머지 키워드들을 포함
    # 초기 쿼리 생성

    # for keyword in keywords:
    #     print(keyword)
    
    q_objects = Q(youtube_title__contains=keywords[0])
    # 나머지 키워드들을 OR 조건으로 추가
    for keyword in keywords[1:]:
        q_objects |= Q(youtube_title__contains=keyword)
    # 쿼리 실행
    youtube_list = Youtube.objects.filter(q_objects)
    #################################################################################

    attraction_list = attraction_list[:3]
    youtube_list = youtube_list[:3] 
    
    return render(request, 'accommodation_app/accommodation_detail.html', {'attraction_list':attraction_list ,'accommodation':accommodation, 'youtube_list':youtube_list})
