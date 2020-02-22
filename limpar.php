<?php
$arquivo = $_GET['arquivo'];
shell_exec("rm -rf $arquivo");
header("Location: ./index.php");
die();
