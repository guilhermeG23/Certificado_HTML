<?php

function limpaSpaces($entrada) {
	return preg_replace("/\s+/", "_", $entrada);
}

function tratamentoDatas($entrada) {
	return preg_replace('/[^0-9]/', '', $entrada);
}

function arrumaPalavra($entrada) {
	return preg_replace("/[^a-zA-Z0-9á-úÁ-Ú]\s/", "_", $entrada);
}

$orientacao = $_POST["orientacao"];

$treinamento = limpaSpaces($_POST["treinamento"]);
$RC = $_POST["contador_responsavel"];
$CF = $_POST["contador_funcionario"];
$CC = $_POST["contador_curso"];

$DI = tratamentoDatas($_POST["data_inicial"]);
$DF = tratamentoDatas($_POST["data_final"]);
$DE = tratamentoDatas($_POST["data_emissao"]);
$horas = $_POST["horas"];

if ($DF === "") {
	$DF = 0;
}

$array_responsaveis = "";
for ($i = 0; $i != $RC; $i++) {
	$NR = "nome_responsavel" . $i;
	$DR = "descricao_responsavel" . $i;
	if ($i == 0) {
		$array_responsaveis = limpaSpaces(arrumaPalavra($_POST[$NR])) . "," . limpaSpaces(arrumaPalavra($_POST[$DR]));
	} else {
		$array_responsaveis = $array_responsaveis . "," . limpaSpaces(arrumaPalavra($_POST[$NR])) . "," . limpaSpaces(arrumaPalavra($_POST[$DR]));
	}
}

$array_funcionarios = "";
for ($i = 0; $i != $CF; $i++) {
	$F =  "funcionario" . $i;
	if ($i == 0) {
		$array_funcionarios = limpaSpaces(arrumaPalavra($_POST[$F]));
	} else {
		$array_funcionarios = $array_funcionarios . "," . converter(limpaSpaces(arrumaPalavra($_POST[$F])));
	}
}

$array_cursos = "";
for ($i = 0; $i != $CC; $i++) {
	$C =  "curso" . $i;
	if ($i == 0) {
		$array_cursos = limpaSpaces(arrumaPalavra($_POST[$C]));
	} else {
		$array_cursos = $array_cursos . "," . limpaSpaces(arrumaPalavra($_POST[$C]));
	}
}

$arquivo = arrumaPalavra(limpaSpaces($_POST['arquivo'])) . ".pdf";

if ($orientacao == "0") {
	shell_exec("PYTHONIOENCODING=utf-8 python3 certificadoMeio.py $treinamento $DE $DI $DF $horas $array_responsaveis $array_funcionarios $array_cursos");
	shell_exec("cp -r pdf_tmp_9842389429.pdf $arquivo");
} elseif ($orientacao == "1") {
	shell_exec("PYTHONIOENCODING=utf-8 python3 certificadoA4.py $treinamento $DE $DI $DF $horas $array_responsaveis $array_funcionarios $array_cursos");
	shell_exec("cp -r rotate_tmp_2398487239.pdf $arquivo");
}

header("Location: index.php");
die();
