from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm
from django.db.models import Q 
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers

# Create your views here.

def product_index(request):
    return render(request, 'product_app/index.html')
# include 로 포함한 주소목록에서 index 충돌 -> 우선순위가 projcetex index가 아니라 product index로 잡힘 -> product view + url 같이 변경

# 전체 상품 정보 조회
def product_list(request):
    # DB에서 select한 결과 반환 (모든 상품 데이터 반환)
    # Product.objects.all() 사용
    products = Product.objects.all()
    return render(request, 'product_app/product_list.html', {'products':products})

# 상세 상품 조회
# 전달받은 prd_no에 해당되는 1개 상품 데이터 반환
def product_detail(request, prd_no):
    # prd_no 조건에 맞는 행 select
    # get_object_or_404() 사용
    product = get_object_or_404(Product, pk=prd_no)
    return render(request, 'product_app/product_detail.html', {'product':product})

# 상품 등록
def product_insert(request):
    # (1) 요청이 POST 인지 확인하고
    if request.method == "POST":
        # (2) 폼 데이터의 내용을 form 변수에 저장
        form = ProductForm(request.POST)
        # (3) Django의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # (4) form에 저장된 데이터를 아직 완전 저장하지 않고
            # (현재는 이 부분 없어도 됨 : 저장 지연)
            product = form.save(commit=False)
            # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
            # product....() 작업
            # (5) 여기에서 DB 저장 
            product.save()
            # (6) DB에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩) 
            # redirect() 사용
            return redirect('product_list')
    else:
        form = ProductForm()

    # (7) else : POST 요청이 아니라면 입력 폼 그대로 출력
    return render(request, 'product_app/product_form.html', {'form':form})
        
# 상품정보 수정
def product_update(request, prd_no):
    # (1) 전달받은 prd_no에 해당되는 상품 정보 가져와서
    product = get_object_or_404(Product, pk=prd_no)
    # (2) 요청이 POST 인지 확인하고 : 데이터 입력하고 서버로 전송
    if request.method == "POST":
        # (3) 가져온 product 데이터의 내용을 form 변수에 저장
        form = ProductForm(request.POST, instance=product)
        # (4) Django의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # (5) form에 저장된 데이터를 아직 완전 저장하지 않고
            # (현재는 이 부분 없어도 됨 : 저장 지연)
            product = form.save(commit=False)
            # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
            # product....() 작업
            # (6) 여기에서 DB 저장 
            product.save()
            # (7) DB에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩) 
            # redirect() 사용
            return redirect('product_list')
    else:
        form = ProductForm(instance=product) # 처음 폼 화면 출력
        # 폼에 prd_no에 해당되는 상품 데이터 출력

    # (8) else : POST 요청이 아니라면 입력 폼 그대로 출력
    return render(request, 'product_app/product_update.html', {'form':form})

# 상품 삭제
def product_delete(request, prd_no):
    # prd_no에 해당되는 상품 찾아와서
    product = get_object_or_404(Product, pk=prd_no)

    # 상품 데이터 삭제
    product.delete()

    # 상품 조회 화면으로 이동 (포워딩)
    return redirect('product_list')


# 검색창 열기
def product_search_form(request):
    return render(request, 'product_app/product_search_form.html')


# 검색 쿼리 수행
def product_search(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "prd_name":
            prd_list = Product.objects.filter(Q(prd_name__contains=keyword)) 
        else:
            prd_list = Product.objects.filter(Q(prd_maker__contains=keyword)) 

        return render(request, 'product_app/product_search_form.html', {'prd_list':prd_list})


def ajax_test(request):
    return render(request, 'product_app/ajax_test.html')

# Ajax 연습 : 데이터만 전송
def get_data(request):
    data = {'name' : '홍길동'}

    return JsonResponse(data)


# Ajax를 사용한 검색
# 검색창 열기
def product_search_form2(request):
    return render(request, 'product_app/product_search_form2.html')


# 검색 기능 수행하고 결과를 JsonResponse로 반환
def product_search2(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']

        print(type, keyword)

        if type == "prd_name":
            prd_list = Product.objects.filter(Q(prd_name__contains=keyword)) 
        else:
            prd_list = Product.objects.filter(Q(prd_maker__contains=keyword))

        # prd_list 쿼리 데이터 셋을 JSON 타입으로 변환
        prd_list_json = json.loads(serializers.serialize('json', prd_list, ensure_ascii=False))

        return JsonResponse({'reload_all':False, 'prd_list_json':prd_list_json})
    

    
# Ajax를 사용한 검색
# 검색창 열기
def product_search_form3(request):
    return render(request, 'product_app/product_search_form3.html')


# 검색 기능 수행하고 결과를 JsonResponse로 반환
def product_search3(request):
    try:
        if request.method == "POST":
            type = request.POST['type']
            keyword = request.POST['keyword']
            min_price = request.POST['min_price']
            max_price = request.POST['max_price']        

            print(type, keyword)

            if type == "prd_name" or type == "prd_maker":
                prd_list = Product.objects.filter(Q(prd_name__contains=keyword)) 
            elif type == "prd_price":                
                prd_list = Product.objects.filter(Q(prd_price__gte = min_price, prd_price__lte = max_price))
                
            # prd_list 쿼리 데이터 셋을 JSON 타입으로 변환
            prd_list_json = json.loads(serializers.serialize('json', prd_list, ensure_ascii=False))

            return render(request, 'product_app/product_search3_result.html', {'prd_list':prd_list})
    except:
        return HttpResponse("최소 최대 가격을 다시 입력하세요")