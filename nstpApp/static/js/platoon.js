function joining() {
    var joinbtn = document.querySelector('.btns');
    joinbtn.addEventListener('click', () => {
        joinbtn.innerText = 'Joining Class...';

        setTimeout(() => {

            location.href = "../html/alpha.html";


        }, 3000);



    })

}