$(document).ready(function(){
    $("#form1").submit(function(e){
        e.preventDefault();
        var nomb = $("#nom").val();
        let mensajesMostrar = "";
        let entrar = false;

        if(nomb.trim().length < 1 || nomb.trim().length > 10){
            mensajesMostrar += "La longitud no es correcta<br>";
            entrar = true;
        }

        var letra = nomb.charAt(0);
        if(!esMayuscula(letra)){
            mensajesMostrar += "La primera letra es minúscula<br>";
            entrar = true;
        }

        if(entrar){
            $("#mensaje").html(mensajesMostrar);
        }
        else{
            $("#mensaje").html("Formulario Enviado");
        }

    });

    function esMayuscula(letra){
        return letra == letra.toUpperCase();
    }    
});
