const form = document.getElementById('form');
const password1Element = document.getElementById('password1');
const password2Element = document.getElementById('password2');
const messageContainer = document.querySelector('.message-container');
const message = document.getElementById('message');

let isValid = false; /*boolean to check whether form is valid*/
let passwordsMatch = false; /*boolean to check whether both passwords are the same*/
const validateForm = () => {
    /*using constraint API*/
    isValid = form.checkValidity();
    /*if it isn't valid, style the form for visual feedback*/
    if (!isValid)
    {
        message.textContent = 'Please fill out all fields.'
        message.style.color = 'red'
        messageContainer.style.borderColor = 'red'
        return;
    }
    if (password1Element.value === password2Element.value){
        passwordsMatch = true;
        password1Element.style.borderColor = 'green'
        password2Element.style.borderColor = 'green'
    } else {
        passwordsMatch = false;
        message.textContent = 'Make sure passwords match.'
        message.style.color = 'red'
        messageContainer.style.borderColor = 'red'
        password1Element.style.borderColor = 'red'
        password2Element.style.borderColor = 'red'
        return
    }
    /*If form is valid and passwords match*/
    if ( isValid && passwordsMatch){
        message.textContent = 'Successfully registered.'
        message.style.color = 'green'
        messageContainer.style.borderColor = 'green'
    }
}

const storeFormData = () => {
    const user = {
        name: form.name.value,
        phone: form.phone.value,
        email: form.email.value,
        website: form.website.value,
        password: form.password.value,
    }
    console.log(user)
}

const processFormData = (e) => {
    e.preventDefault();
    /*Validate form*/
    validateForm();
    /*Submit data if valid,*/
    if (isValid && passwordsMatch){
        storeFormData();
    }
}






/*Event Listeners*/
form.addEventListener('submit', processFormData)