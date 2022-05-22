$(document).ready(function () {

    $("#formCreRec").submit(function (e) {
        e.preventDefault();   
        var img = $("#imagen").val();
        var nomRec = $("#nombreReceta").val();
        
        var ingre = $("#ingredientes").val();
        var prepa = $("#preparacion").val();

        let mensajeMostrar = "";
        let entrar = true;

        if(img.length > 70){
            mensajeMostrar += "La longitud de la url no puede contener mas de 70 caracteres";
            entrar = false;
        }

        if(nomRec.length > 50){
            mensajeMostrar += "La longitud del nombre no puede contener mas de 50 caracteres";
            entrar = false;
        }

        if(ingre.length > 200){
            mensajeMostrar += "La longitud de los ingredientes no puede contener mas de 50 caracteres";
            entrar = false;
        }

        if(prepa.length > 500){
            mensajeMostrar += "La longitud de la preparacion no puede contener mas de 500 caracteres";
            entrar = false;
        }

        if (entrar) {
            $("#mensaje").html("Receta registrada con exito");
        }
        else {
            $("#mensaje").html(mensajeMostrar);
        }



    });
})
