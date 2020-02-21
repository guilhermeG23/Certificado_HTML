<!DOCTYPE html>
<head>
	<link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="./css/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="./css/cssPessoal.css">
</head>
<body>
<!--Entrada de registros de notas em modal-->
<form action="cadastrar.php" method="POST" enctype="multipart/form-data">
<div class="moldura-certificados" id="registrar_computador" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	<div class="" role="document">
		<div class="modal-content">
			<div class="modal-body">
				<div class="container regular-altura">
					<div class="form-group">
						<input type="hidden" class="form-control" value="" id="contador_responsavel" name="contador_responsavel" maxlength="100" placeholder="" autocomplete="off"></td>
						<input type="hidden" class="form-control" value="" id="contador_funcionario" name="contador_funcionario" maxlength="100" placeholder="" autocomplete="off"></td>
						<input type="hidden" class="form-control" value="" id="contador_curso" name="contador_curso" maxlength="100" placeholder="" autocomplete="off"></td>
					
						<table class="table">
							<tr>
								<td><label class="col-form-label">Nome do arquivo: </label></td>
								<td colspan="6"><input type="text" class="form-control" value="" id="arquivo" name="arquivo" maxlength="100" placeholder="Ex: Nome do arquivo..." autocomplete="off" ></td>
							<tr>
								<td><label class="col-form-label">Orientacao do papel: </label></td>
								<td colspan="6">
									<select id="orientacao" name="orientacao">
										<option value="">...</option>
										<option value="0">Meia folha</option>
										<option value="1">A4</option>
									</select>
								</td>
							</tr>
							<tr>
								<td><label class="col-form-label">Treinamento: </label></td>
								<td colspan="6"><input type="text" class="form-control" value="" id="treinamento" name="treinamento" maxlength="100" placeholder="Ex: Treinamento..." autocomplete="off" ></td>
							</tr>
							<tr>
								<td><label class="col-form-label">Data emissao certificado: </label></td>
								<td colspan="6"><input type="text" class="form-control data" value="" id="data_emissao" name="data_emissao" placeholder="EX: dd/mm/yyyy" autocomplete="off"></td>
							</tr>
							<tr>
								<td><label class="col-form-label">Data inicio curso: </label></td>
								<td colspan="6"><input type="text" class="form-control data" value="" id="data_inicial" name="data_inicial" placeholder="EX: dd/mm/yyyy" autocomplete="off"></td>
							</tr>
							<tr>
								<td><label class="col-form-label">Data fim curso: </label></td>
								<td colspan="6"><input type="text" class="form-control data" value="" id="data_final" name="data_final" placeholder="EX: dd/mm/yyyy" autocomplete="off"></td>
							</tr>
							<tr>
								<td><label class="col-form-label">Horas: </label></td>
								<td colspan="2"><input type="text" class="form-control" value="" id="horas" name="horas" placeholder="EX: quantidade horas do curso/treinamento..." autocomplete="off" >		
							</tr>
						</table>
						<hr>
						<table id="destino_responsavel" class="table table-borderless">
							<tr>
								<td colspan="2"><label class="col-form-label">Responsavel: </label></td>
								<td colspan-"2"><label class="col-form-label">Descricao: </label></td>	
								<td colspan="1" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn btn-success" style="cursor: pointer;" onclick="duplicarCamposResponsavel();">Novo campo</button>
									<button type="button" class="btn btn-warning" style="cursor: pointer;" onclick="removerCamposResponsavel();">Apagar ultimo campo</button>
									<button type="button" class="btn btn-danger" style="cursor: pointer;" onclick="allremoverCamposResponsavel();">Delete todos os campos extras</button>
								</td>
							</tr>
							<tr>
								<td colspan="2"><input type="text" class="form-control" value="" id="nome_responsavel0" name="nome_responsavel0" maxlength="54" placeholder="Ex: responsavel pelo curso/treinamento" autocomplete="off"></td>
								<td colspan="3"><input type="text" class="form-control" value="" id="descricao_responsavel0" name="descricao_responsavel0" maxlength="100" placeholder="Ex: descricao do profissional" autocomplete="off" ></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_responsavel">
								<td colspan="2"><input type="text" class="form-control" value="" id="nome_responsavel" name="nome_responsavel0" maxlength="54" placeholder="Ex: responsavel pelo curso/treinamento" autocomplete="off"></td>
								<td colspan="3"><input type="text" class="form-control" value="" id="descricao_responsavel" name="descricao_responsavel0" maxlength="100" placeholder="Ex: descricao do profissional" autocomplete="off" ></td>
							</tr>
						</table>

						<table id="destino_funcionario" class="table table-borderless">
							<tr>
								<td colspan="4"><label class="col-form-label">Funcionario: </label></td>
								<td colspan="1" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn btn-success" style="cursor: pointer;" onclick="duplicarCamposFuncionario();">Novo campo</button>
									<button type="button" class="btn btn-warning" style="cursor: pointer;" onclick="removerCamposFuncionario();">Apagar ultimo campo</button>
									<button type="button" class="btn btn-danger" style="cursor: pointer;" onclick="allremoverCamposFuncionario();">Delete todos os campos extras</button>
								</td>
							</tr>
							<tr>
								<td colspan="5"><input type="text" class="form-control" value="" id="funcionario0" name="funcionario0" maxlength="54" placeholder="Ex: nome do funcionario" autocomplete="off"></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_funcionario">
								<td><input type="text" class="form-control" value="" id="funcionario" name="funcionario" maxlength="54" placeholder="Ex: nome do funcionario" autocomplete="off"></td>
							</tr>
						</table>

						<table id="destino_curso" class="table table-borderless">
							<tr>
								<td colspan="2"><label class="col-form-label">Curso: </label></td>
								<td colspan="3" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn btn-success" style="cursor: pointer;" onclick="duplicarCamposCurso();">Novo campo</button>
									<button type="button" class="btn btn-warning" style="cursor: pointer;" onclick="removerCamposCurso();">Apagar ultimo campo</button>
									<button type="button" class="btn btn-danger" style="cursor: pointer;" onclick="allremoverCamposCurso();">Delete todos os campos extras</button>
								</td>

							</tr>
							<tr>
								<td colspan="5"><input type="text" class="form-control" value="" id="curso0" name="curso0" maxlength="54" placeholder="Ex: tópicos do curso" autocomplete="off"></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_curso">
								<td><input type="text" class="form-control" value="" id="curso" name="curso" maxlength="54" placeholder="Ex: tópicos do curso" autocomplete="off"></td>
							</tr>
						</table>

					</div>
				</div>
				<div class="modal-footer">
					<button type="reset" class="btn btn-warning">Limpar</button>
					<button type="submit" class="btn btn-success">Registrar</button>
				</div>
			</div>
		</div>
	</div>
</div>
</form>

<table class="table">
	<thead class="thead-dark">
		<tr>
			<th>Nome do arquivo</th>
			<th>PDF</th>
		</tr>
	</thead>
	<tbody>
		<?php
		$arquivos = glob("{*.pdf}", GLOB_BRACE);
		foreach($arquivos as $arquivo) {
			if ($arquivo == "pdf.pdf" || $arquivo == "saida.pdf") {
				continue;
			} else {
				echo "<tr>
					<th>{$arquivo}</th>
					<th><a href='{$arquivo}' download>{$arquivo}</a></th>
				</tr>";
			}
		} 
		?>
	</tbody>
</table>
</body>
<script type="text/javascript" src="../js/jquery-3.3.1.slim.min.js"></script>
<script type="text/javascript" src="../js/jquery-1.12.4.js"></script>
<script type="text/javascript" src="../js/datapicker.js"></script>
<script type="text/javascript" src="../js/bootstrap.min.js"></script>
<script type="text/javascript" src="../js/popper.min.js"></script>
<script type="text/javascript" src="../js/jquery.mask.js"></script>	
<script type="text/javascript" src="../js/jquery-ui.js"></script>	

<script type="text/javascript" src="./js/js-geral-responsavel.js"></script>
<script type="text/javascript" src="./js/js-geral-funcionario.js"></script>
<script type="text/javascript" src="./js/js-geral-curso.js"></script>
