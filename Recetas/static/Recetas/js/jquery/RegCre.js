$(document).ready(function () {

    $("#formRegi").submit(function (e) {
        
        var nomRec = $("#nomreceta").val();
        var deta   = $("#detalle").val();
        var ingre = $("#ingredientes").val();
        var prepa = $("#preparacion").val();
        

        let mensajeMostrar = "";
        let entrar = true;


        if(nomRec.length > 30){
            mensajeMostrar += "La longitud del nombre no puede contener mas de 30 caracteres<br>";
            entrar = false;
        }
        if (!deta == "") {

            if(deta.length > 1000){
                mensajeMostrar += "La longitud del detalle no puede contener mas de 1000 caracteres<br>";
                entrar = false;
            }
        }
        if (!ingre == "") {

            if(ingre.length > 1000){
                mensajeMostrar += "La longitud de los ingredientes no puede contener mas de 1000 caracteres<br>";                
                entrar = false;
            }
        }
        if (!prepa == "") {

            if(prepa.length > 2000){
                mensajeMostrar += "La longitud de la preparacion no puede contener mas de 2000 caracteres<br>";
                entrar = false;
            }
        }
        

        if (entrar) {
            $("#mensajeReg").html("Cargando...");
        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
            e.preventDefault();
        }
    });
})
