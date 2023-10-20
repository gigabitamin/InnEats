from django.shortcuts import render
from django.db.models import Q
from inneats_app.models import Visitkorea 

# Create your views here.
def accommodation(request,keyword):    
    print(keyword)    

    return render(request, 'accommodation_app/accommodation.html',{'keyword':keyword})


def accommodation_detail(request, keyword):    
    # print(keyword)    

    # 하위 주소를 토대로 관광지 리스트 쿼리 
    addr = "제주 서귀포시 안덕면"
    keywords = addr.split(" ")

    if len(keywords) > 2 :
        keyword = keywords[2]
    else:
        keyword = keywords[1]

    # print(keyword)
    # attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))[:3]

    # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
    #################################################################################
    # 키워드를 포함한 리스트
    keywords = ['용연구름다리', '화북포구', '아날로그감귤밭']  # 나머지 키워드들을 포함
    # 초기 쿼리 생성
    q_objects = Q(visitkorea_title__contains=keywords[0])
    # 나머지 키워드들을 OR 조건으로 추가
    for keyword in keywords[1:]:
        q_objects |= Q(visitkorea_title__contains=keyword)
    # 쿼리 실행
    attraction_list = Visitkorea.objects.filter(q_objects)
    #################################################################################
 
        
    return render(request, 'accommodation_app/accommodation_detail.html', {'attraction_list':attraction_list})