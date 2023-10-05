console.log("script loaded");
const name = document.getElementById("name");
const password = document.getElementById("password");

function loginValidation() {
    const nameValue = name.value; // Access the value of the name element
    const passwordValue = password.value; // Access the value of the password element

    if (nameValue === 'admin' && passwordValue === 'admin') {
        alert('Welcome admin');
    } else {
        alert('Invalid Credentials');
    }

    // Return false to prevent form submission (if needed)
    return false;
}

