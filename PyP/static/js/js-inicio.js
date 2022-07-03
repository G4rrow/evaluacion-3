$(document).ready(function() {

    $(".btn-success").hover(
        function(){
            $(this).append(" <i class='fa-solid fa-cart-shopping'></i>");
        },function(){
            $(".fa-cart-shopping").remove();
        }
    );

    $(".carousel-item").each(function (indexInArray) { 
        console.log(indexInArray);
         if(indexInArray == 0){
            $(this).addClass('active');
            console.log(valueOfElement);
         }
    });
       
});