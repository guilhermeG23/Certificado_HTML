<?php

function limpaSpaces($entrada) {
	return preg_replace("/\s+/", "_", $entrada);
}

$orientacao = $_POST["orientacao"];

$RC = $_POST["contador_responsavel"];
$CF = $_POST["contador_funcionario"];
$CC = $_POST["contador_curso"];

$treinamento = limpaSpaces($_POST["treinamento"]);
$DI = $_POST["data_inicial"];
$DF = $_POST["data_final"];
$DE = $_POST["data_emissao"];
$horas = $_POST["horas"];

$array_responsaveis = "";
for ($i = 0; $i != $RC; $i++) {
	$NR =  "nome_responsavel" . $i;
	$DR = "descricao_responsavel" . $i;
	if ($i == 0) {
		$array_responsaveis = limpaSpaces($_POST[$NR]) . "," . limpaSpaces($_POST[$DR]);
	} else {
		$array_responsaveis = $array_responsaveis . "," . limpaSpaces($_POST[$NR]) . "," . limpaSpaces($_POST[$DR]);
	}
}

$array_funcionarios = "";
for ($i = 0; $i != $CF; $i++) {
	$F =  "funcionario" . $i;
	if ($i == 0) {
		$array_funcionarios = limpaSpaces($_POST[$F]);
	} else {
		$array_funcionarios = $array_funcionarios . "," . limpaSpaces($_POST[$F]);
	}
}

$array_cursos = "";
for ($i = 0; $i != $CC; $i++) {
	$C =  "curso" . $i;
	#$array_cursos = limpaSpaces($_POST[$C]) . "," . $array_cursos;
	if ($i == 0) {
		$array_cursos = limpaSpaces($_POST[$C]);
	} else {
		$array_cursos = $array_cursos . "," . limpaSpaces($_POST[$C]);
	}
}

shell_exec("python3 teste.py $treinamento $DI $DF $horas $array_responsaveis $array_funcionarios $array_cursos $orientacao $DE");

#header("Location: index.php");
die();
