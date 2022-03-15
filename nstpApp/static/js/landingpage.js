var a = true;


function loads() {
    console.log("saqui");
    let y = document.querySelector('.loadm');
    let z = document.querySelector('.latestx');
    var x = document.getElementById("card-deck1");
    if (a) {
        x.style.display = "block";
        y.innerHTML = "SHOW LESS";
        z.style.height = 1500 + 'px';
        console.log("saqui2");
        a = false;


    } else {
        x.style.display = "none";
        z.style.height = "120vh";
        y.innerHTML = "SHOW MORE";
        console.log("saqui3");
        a = true;
    }
}