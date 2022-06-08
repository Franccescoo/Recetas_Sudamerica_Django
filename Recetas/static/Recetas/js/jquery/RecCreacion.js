$(document).ready(function () {

    $("#formCreRec").submit(function (e) {
           
        var nomRec = $("#nombreReceta").val();
        
        var ingre = $("#ingredientes").val();
        var prepa = $("#preparacion").val();

        let mensajeMostrar = "";
        let entrar = true;

   

        if(nomRec.length > 30){
            mensajeMostrar += "La longitud del nombre no puede contener mas de 50 caracteres";
            entrar = false;
        }

        if(ingre.length > 1000){
            mensajeMostrar += "La longitud de los ingredientes no puede contener mas de 50 caracteres";
            entrar = false;
        }

        if(prepa.length > 2000){
            mensajeMostrar += "La longitud de la preparacion no puede contener mas de 500 caracteres";
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
