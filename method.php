<?php
header("Access-Control-Allow-Origin: localhost");
header("Access-Control-Allow-Origin: me.apricityx.top");
header("Access-Control-Allow-Methods: GET");
header("Access-Control-Allow-Headers: *");
$q = $_GET["method"];
if ($q == "get_address") {
    $f = file("ip");
    echo $f[0];
}
if ($q == "get_last_connect_time") {
    $f = file("ip");
    echo $f[1];
}
if ($q == "set_ip") {
    $line_one = $_GET["ip"];
    $line_two = time();
    $f = fopen("ip", "w");
    fwrite($f, $line_one . "\n" . $line_two);
    fclose($f);
    echo "Success";
}
if ($q == "get_poem") {
    $f = file("random.txt");
    echo $f[rand(0, count($f) - 1)];
}