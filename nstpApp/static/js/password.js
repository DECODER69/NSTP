function checkpassword() {
    let password = document.getElementById("password").value;
    let confirm = document.getElementById("confirm-password").value;


    console.log(password, confirm);
    let message = document.getElementById("message");

    if (password.length != 0) {
        if (password == confirm) {
            message.textContent = "";

            timeout();





        } else {
            message.textContent = "Password Don't Match";
            message.style.backgroundColor = "#ff4d4d";
        }
    }
}

function timeout() {
    let submit = document.querySelector('#sub-button');


    submit.addEventListener('click', () => {
        submit.innerText = 'Submitting...';

        setTimeout(() => {

            location.href = "../html/alpha.html";


        }, 3000);



    });
}