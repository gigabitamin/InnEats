$(document).ready(function(){
    $('#prdSearchFrm2').on('submit', function(){

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
            url:"http://127.0.0.1:8000/product/search2/",
            data:formData,
            datatype:'json',
            success:function(result){
                console.log(result)
                console.log(result.prd_list_json)

                let prd_list = result.prd_list_json;

                //반환된 결과를 searchResultBox <div>에 테이블 형태로 출력 (삽입)
                // div 태그에 삽입 : append()
                // 실행할 때마다 append() 이전 결과 뒤에 계속 append 됨
                // 다 삭제한 후 append 수행
                $('#searchResultBox').empty()

                // 테이블 태그 문자열로 생성
                const str = `
                    <table id="prd_list">
                    <tr>
                        <th>상품번호</th>
                        <th>상품명</th>
                        <th>가격</th>
                        <th>제조회사</th>
                        <th>색상</th>
                        <th>카테고리번호</th>
                    </tr>
                `

                $('#searchResultBox').append(str);

                // 데이터 추출해서 append 
                if(prd_list.length == 0){
                    $('#prd_list').append('<tr align="center"><td colspan="6">조건에 해당하는 결과가 없습니다</td></tr>')
                } else {
                    for(let i=0; i<prd_list.length; i++){
                        $('#prd_list').append('<tr><td>' +
                            prd_list[i].pk + '</td><td>' +
                            prd_list[i].fields.prd_name + '</td><td>' +
                            prd_list[i].fields.prd_price + '</td><td>' +
                            prd_list[i].fields.prd_maker + '</td><td>' +
                            prd_list[i].fields.prd_color + '</td><td>' +
                            prd_list[i].fields.ctg_no + '</td></tr>');                        
                    }
                }

                $('#prd_list').append('</table>');
            },
            error:function(){
                // 오류 발생 시 수행되는 함수
                alert("오류 발생")
            },
            complete:function(){
                // 완료 되었을 때 수행된 함수
            }
        });

    })
});