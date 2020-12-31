<?php 
/* attempt Mariadb server connection. */
$link = mysqli_connect("localhost", "eyh", "horizon", "eyh");

// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}


// User inputs with security
$first_name = mysqli_real_escape_string($link, $_REQUEST['first_name']);
$last_name = mysqli_real_escape_string($link, $_REQUEST['last_name']);
$email = mysqli_real_escape_string($link, $_REQUEST['email']);
$inputAddress = mysqli_real_escape_string($link, $_REQUEST['inputAddress']);
$inputAddress2 = mysqli_real_escape_string($link, $_REQUEST['inputAddress2']);
$inputCity = mysqli_real_escape_string($link, $_REQUEST['inputCity']);
$inputState = mysqli_real_escape_string($link, $_REQUEST['inputState']);
$inputZip = mysqli_real_escape_string($link, $_REQUEST['inputZip']);


//Attempt inset execution
$sql = "INSERT INTO student (fist_name, last_name, email, inputAddress, inputAddress2, inputCity, inputState, inputZip) VALUES ('$first_name', '$last_name', '$email', '$inputAddress', '$inputAddress2', '$inputCity', '$inputState', '$inputZip')";
if(mysqli_query($link, $sql)){
    echo "Records added successfully.";
} else{ 
    echo "ERROR: Could not connect to database $sql. " .
    mysqli_error($link);   
}


//Close database connection
mysqli_close($link);
?>