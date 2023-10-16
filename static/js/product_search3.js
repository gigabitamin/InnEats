$(document).ready(function(){
    $('#prdSearchFrm3').on('submit', function(){

        // submit 이벤트 기본 기능 : 페이지 새로고침
        // 페이지 새로고침 되지 않도록
        event.preventDefault();

        // 폼에 입력한 값들을 쿼리 스트링 방식의 데이터로 변환
        // type=prd_name&keyword=자전거
        // serialize() 사용 : 쿼리 스트링 방식의 데이터로 변환
        let formData = $(this).serialize();

        $.ajax({
            type:"post",
            // url:"/product/search2/",
            url:"http://127.0.0.1:8000/product/search3/",
            data:formData,
            datatype:'json',
            success:function(result){
                $('#searchResultBox').html(result);
            },
            error:function(){
                // 오류 발생 시 수행되는 함수
                alert("오류 발생")
            },
            complete:function(){
                // 완료 되었을 때 수행된 함수
            }
        });
    });

});

