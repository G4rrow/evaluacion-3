$(document).ready(function() {

    $(".btn-success").hover(
        function(){
            $(this).append(" <i class='fa-solid fa-cart-shopping'></i>");
        },function(){
            $(".fa-cart-shopping").remove();
        }
    );

    $(".precio").each(function (index, element) {
        var text = $(this).html().split("").reverse().join("");
        var nuevo_precio = '';
        var cont = 1;
        for (let i = 0; i < text.length; i++) {
            var numero = text[i]; 
            if(cont == 4){
                nuevo_precio += ('.'+numero);
                cont = 1;
            }else{
                nuevo_precio += (''+numero);
                cont ++;
            }
        }
        nuevo_precio += ('$');
        rever_precio = nuevo_precio.split("").reverse().join("");
        $(this).html(rever_precio);
    });
       
});