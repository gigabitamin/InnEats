
$(document).ready(function(){
    // moveToTop 이미지 클릭시 Top으로 이동
    $('#moveToTop').on('click', function(){
        $('html, body').animate({scrollTop:0}, 500);
    })
});
