<!doctype html>
<html lang="zh_CN">
<head>
    <title>My First PHP Page</title>
</head>
<body>
<p id="PC_ID">Loading...</p>
<p id="PC_IP"></p>
<?php
    echo "Hello World!";
?>

</body>
<script>
    function update_add() {
        console.log("update");
        let text_container = document.getElementById("PC_ID");
        let xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () { //回调函数
            //若请求成功
            if (xmlhttp.readyState === 4 && xmlhttp.status === 200) text_container.innerHTML = xmlhttp.responseText;
        }
        xmlhttp.open("GET", "method.php?method=get_address", true);
        xmlhttp.send();
    }

    setInterval(update_add, 1000);
</script>

</html>
