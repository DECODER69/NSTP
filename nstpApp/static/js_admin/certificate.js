const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const nameInput = document.getElementById('name');
const downloadBtn = document.getElementById('download-btn');

const image = new Image()
image.src = 'certificate.png'
image.onload = function() {
    drawImage();
}

function drawImage() {
    // ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
    ctx.font = '40px monotype corsiva'

    ctx.fillText(nameInput.value, 50, 230);
}

nameInput.addEventListener('input', function() {
    drawImage()
})

downloadBtn.addEventListener('click', function() {
    downloadBtn.href = canvas.toDataURL('image/JPEG', 1.0);
    var pdf = new jsPDF();

    pdf.addImage(imgData, 'JPEG', 0, 0);
    pdf.save("download.pdf");

    downloadBtn.download = 'Certificate - ' + nameInput.value
});



function tableSearch() {
    let input, filter, table, tr, td, txtValue;

    //Intialising Variables
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }

}