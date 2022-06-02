$(document).ready(function () {

    $("#log").submit(function (e) {
        
        var nomb = $("#nomUser").val();
        var pass = $("#pass").val();
    
        let mensajeMostrar = "";
        let entrar = false;
        let aceptado = "Iniciar sesión";
        $("#iniUser").html("");
        $("#iniAdmin").html("");
    
        if (nomb == "user" && pass == "user"){
            mensajeMostrar += "Cuenta Encontrada<br>";
            entrar = true;
        }
        else if (nomb == "admin" && pass == "admin"){
            mensajeMostrar += "Cuenta Encontrada<br>";
            entrar = true;
        }
        if(entrar){
            $("#mensajeLog").html(mensajeMostrar);
            
            if(nomb == "user"){
                $("#iniUser").html(aceptado);
            }
            else if(nomb == "admin"){
                $("#iniAdmin").html(aceptado);
            }

        }
        else{
            $("#mensajeLog").html("Usuario y/o contraseña incorrectos");
        }

    });
})