$(document).ready(function() {

    $("#form-contacto").validate({
        rules:{
            nombre:{
                required:true,
                minlength: 2
            },
            apellido:{
                required:true,
                minlength: 2
            },
            emailinput:{
                required:true,
                email:true
            },
            asunto:{
                required:true,
                
            },
            descripcion:{
                required:true,
                
            }
        },
        messages:{
            nombre:{
                required:"Debe ingresar su nombre",
                minlength:"Debe tener como minimo 2 caracteres"
            },
            apellido:{
                required:"Debe ingresar su apellido",
                minlength:"Debe tener como minimo 2 caracteres"
            },
            emailinput:{
                required:"Ingrese su correo",
                email:"Debe ingresar un correo valido"
            },
            asunto:{
                required:"Por favor ingrese un asunto",
                
            },
            descripcion:{
                required:"Por favor ingresa un comentario",
                
            },            
        }

    });

});