$(document).ready(function() {

    $("#form-login").validate({
        rules:{
            correo:{
                required:true,
                email:true
            },
            contraseña:{
                required:true,
                minlength:3
            }
        },
        messages:{
            correo:{
                required:"Debe ingresar un correo",
                email:"Debe ingresar un correo valido!"
            },
            contraseña:{
                required:"Debe ingresar una contraseña",
                minlength:"Contraseña invalida!"
            }
        }

    });

});