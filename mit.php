<?php

include "connect.php";
$id = $_POST['id'];
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];



$cek_data=mysqli_query($conn,"SELECT * FROM mit WHERE id='$id'");
$cek = mysqli_num_rows($cek_data);

if ($cek > 0) {
    echo "error chong";
} else {
    $input = mysqli_query($conn, "INSERT INTO mit (id, firstname, lastname) VALUES ('$id', '$firstname', '$lastname')");
    if ($input) {
        echo "sheesh1";
    } else {
        echo "sheesh2";
    }
}

?>