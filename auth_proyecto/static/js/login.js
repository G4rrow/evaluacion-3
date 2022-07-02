$(document).ready(function() {

    $("#form-login").validate({
        rules:{
            username:{
                required:true,
            },
            password:{
                required:true,
                minlength:3
            }
        },
        messages:{
            username:{
                required:"Debe ingresar un nombre de usuario",
            },
            password:{
                required:"Debe ingresar una contraseña",
                minlength:"Contraseña invalida!"
            }
        }

    });

});