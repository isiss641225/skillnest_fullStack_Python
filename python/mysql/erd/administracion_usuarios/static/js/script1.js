function iniciarSesion(){

    alert("Inicio de sesión exitoso");

}

function registrarUsuario(){

    let nombre = document.getElementById("nombreRegistro").value;

    let correo = document.getElementById("correoRegistro").value;

    if(nombre == "" || correo == ""){

        alert("Complete los campos");

    }

    else{

        alert("Usuario registrado correctamente");

    }

}