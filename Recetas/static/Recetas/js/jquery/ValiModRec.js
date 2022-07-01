$(document).ready(function () {

    $("#formModRec").submit(function (e) {
           
        var nomRec = $("#nomreceta").val();
        var deta   =$("detalle").val();
        var ingre = $("#ingredientes").val();
        var prepa = $("#preparacion").val();

        let mensajeMostrar = "";
        let entrar = true;

        if(deta.length > 30){
            mensajeMostrar += "La longitud del detalle no puede contener mas de 1000 caracteres";
            entrar = false;
        }
   

        if(nomRec.length > 30){
            mensajeMostrar += "La longitud del nombre no puede contener mas de 50 caracteres";
            entrar = false;
        }

        if(ingre.length > 1000){
            mensajeMostrar += "La longitud de los ingredientes no puede contener mas de 1000 caracteres";
            entrar = false;
        }

        if(prepa.length > 2000){
            mensajeMostrar += "La longitud de la preparacion no puede contener mas de 2000 caracteres";
            entrar = false;
        }

        if (entrar) {
            $("#mensaje").html("Cargando...");
        }
        else {
            e.preventDefault();
            $("#mensaje").html(mensajeMostrar);
        }
    });
})
