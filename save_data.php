<?php
$data = file_get_contents('php://input');
$json_data = json_decode($data);


if ($data === null) {
    // JSON decoding failed
    echo "Error decoding JSON data\n";
    exit;
}

// Path to the text file where data will be written
$txt_file = 'data.txt';

// Open the text file for writing
$file_handle = fopen($txt_file, 'w');

if ($file_handle === false) {
    // Failed to open the file
    echo "Error opening file\n";
    exit;
}

fwrite($file_handle, $data);


// Close the file handle
fclose($file_handle);
?>
