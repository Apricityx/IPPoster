<?php
$q = $_GET["method"];
if ($q == "get_address") {
    $f = fopen("ip", "r");
    $ip = fread($f, filesize("ip"));
    fclose($f);
    echo $ip;
}
if ($q == "set_ip") {
    $f = fopen("ip", "w");
    fwrite($f, $_GET["ip"]);
    fclose($f);
    echo "SUCCESS";
}
?>