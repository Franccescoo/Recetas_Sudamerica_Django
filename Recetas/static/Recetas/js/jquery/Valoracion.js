$(document).ready(function () {

    $("#formValo").submit(function (e) {
        
        var nombre = $("#nomComentario1").val();
        var mensaje = $("#Mensaje1").val();    
        var mail = $("#emailComentario1").val(); 

        let mensajeMostrar = "";
        let entrar = true;


        if (nombre.length > 30) {
            mensajeMostrar += "El nombre puede contener un máximo de 30 caracteres<br>";
            entrar = false;
        }

        if (mail.length > 30) {
            mensajeMostrar += "El correo no puede contener mas de 30 caracteres<br>";
            entrar = false;
        }


        if (mensaje.length > 1000) {
            mensajeMostrar += "El mensaje no puede contener mas de 1000 caracteres<br>";
            entrar = false;
        }

        if (entrar) {
            $("#mensajeReg").html("");
        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
            e.preventDefault();
        }
    });
})
