$(document).ready(function() {

    $(".btn-success").hover(
        function(){
            $(this).append(" <i class='fa-solid fa-cart-shopping'></i>");
        },function(){
            $(".fa-cart-shopping").remove();
        }
    );
       
});