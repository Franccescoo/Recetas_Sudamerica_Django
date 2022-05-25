$(document).ready(function () {

    $("#formRegi").submit(function (e) {
        var nombre = $("#nomUser").val();
        var ape = $("#apeUser").val();
        var nick = $("#nickUserName").val();
        var mail = $("#email")
        var pass1 = $("#password1").val();
        var pass2 = $("#password2").val();
        var UltimoDigito = nick.charAt(nick.length - 1);
        var UltimoDigiPass1 = pass1.charAt(pass1.length - 1);
        var UltimoDigiPass2 = pass2.charAt(pass2.length - 1);

        let mensajeMostrar = "";
        let entrar = true;


        if (!esMayuscula(nombre.charAt(0))) {
            mensajeMostrar += "La primera letra del nombre debe ser mayúscula<br>";
            entrar = false;
        }

        if (nombre.length > 50) {
            mensajeMostrar += "El nombre puede contener un máximo de 50 caracteres<br>";
            entrar = false;
        }


        if (!ape == "") {

            if (!esMayuscula(ape.charAt(0))) {
                mensajeMostrar += "La primera letra del apellido debe ser mayúscula<br>";
                entrar = false;
            }
            if (ape.length > 50) {
                mensajeMostrar += "El apellido puede contener un máximo de 50 caracteres<br>";
                entrar = false;
            }
        }

        var UltimoDigito = nick.charAt(nick.length - 1);
        if (isNaN(UltimoDigito)) {
            mensajeMostrar += "El último dígito del nombre de usuario debe ser un número<br>";
            entrar = false;
        }

        if (nick.length < 4 || nick.length > 60) {
            mensajeMostrar += "El nombre de usuario debe tener entre 4 y 60 caracteres<br>";
            entrar = false;
        }

        if (mail.length > 70) {
            mensajeMostrar += "El correo no puede contener mas de 70 dígitos<br>";
            entrar = false;
        }

        if ((pass1.length > 60 || pass1.length < 4) || (pass2.length > 60 || pass2.length < 4)) {
            mensajeMostrar += "La contraseñas debe tener entre 4 y 60 caracteres<br>";
            entrar = false;
        }

        if (!esMayuscula(pass1.charAt(0)) || !esMayuscula(pass2.charAt(0))) {
            mensajeMostrar += "La primera letra de la contraseña debe ser mayúscula<br>";
            entrar = false;
        }

        if ((isNaN(UltimoDigiPass1)) || (isNaN(UltimoDigiPass2))) {
            mensajeMostrar += "El último dígito de la contraseña debe ser un número<br>";
            entrar = false;
        }


        if (pass1 != pass2) {
            mensajeMostrar += "Las contraseñas no coinciden<br>";
            entrar = false;
        }



        if (entrar) {
            $("#mensajeReg").html("Registro exitoso");


        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
        }

    });
})

function esMayuscula(letra) {
    return letra == letra.toUpperCase();
};