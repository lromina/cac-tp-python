
function scrollArriba(){
    window.scrollTo({
        top: 0,
        behavior: "smooth" // lento
    })
}

document.getElementById('scrollToTopButton').addEventListener('click',scrollArriba)

window.onscroll = function(){
    var button = document.getElementById('scrollToTopButton');

    if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        button.style.display = "block"
    }else{
        button.style.display ="none"
    }

}

    // Guardamos los datos tomados desde el document en constantes
    const firstname = document.querySelector('#firstname');
    const lastname = document.querySelector('#lastname');
    const email = document.querySelector('#email');
    const password = document.querySelector('#password');
    const country = document.querySelector('#country');
    const errorName = document.querySelector('#error-name');
    const errorLastname = document.querySelector('#error-lastname');
    const errorEmail = document.querySelector('#error-email');
    const errorPassword= document.querySelector('#error-password');
    const formRegister = document.querySelector('#formRegister');

    // Si están todos los elementos cargados enviamos el submit, si no, error
    if (firstname && lastname && email && password && country) {
        if (formRegister) {
            formRegister.addEventListener('submit', validarFormulario);
        } else {
            console.log('Error: formRegister no encontrado');
        }
    } else {
        console.log('Error: elementos del formulario no encontrados');
    }

    function validarFormulario(event) {
        event.preventDefault(); // previene el envío automático del formulario

        let validator = true;
        //Validacion nombre
        if (firstname.value.trim() === '') {
            firstname.classList.add("error");
            errorName.textContent = "Error, debes cargar tu nombre";
            validator = false;
        } else {
            firstname.classList.remove("error");
            errorName.textContent = "";
        }

        //Validacion Apellido
        if (lastname.value.trim() === '') {
            lastname.classList.add("error");
            errorLastname.textContent = "Error, debes cargar tu Apellido";
            validator = false;
        } else {
            lastname.classList.remove("error");
            errorLastname.textContent = "";
        }

        //Validacion Email
        if (email.value.trim() === '') {
            email.classList.add("error");
            errorEmail.textContent = "Error, debes cargar tu Email";
            validator = false;
        } else {
            email.classList.remove("error");
            errorEmail.textContent = "";
        }

        //Validacion Contraseña
        if (password.value.trim() === '') {
            password.classList.add("error");
            errorPassword.textContent = "Error, debes cargar tu Contraseña";
            validator = false;
        } else {
            password.classList.remove("error");
            errorPassword.textContent = "";
        }

       

        if (validator) {
            // Si todo está bien, puedes enviar el formulario
            formRegister.submit();
            alert('Datos enviados Satisfactoriamente')
        }
    }
