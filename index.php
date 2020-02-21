<!--Entrada de registros de notas em modal-->
<form action="cadastrar.php" method="POST" enctype="multipart/form-data">
<div class="fade bd-example-modal-lg" id="registrar_computador" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	<div class="modal-dialog modal-lg" role="document">
		<div class="modal-content">
			<div class="modal-body">
				<div class="container regular-altura">
					<div class="form-group">
						<input type="hidden" class="form-control" value="" id="contador_responsavel" name="contador_responsavel" maxlength="100" placeholder="" autocomplete="off"></td>
						<input type="hidden" class="form-control" value="" id="contador_funcionario" name="contador_funcionario" maxlength="100" placeholder="" autocomplete="off"></td>
						<input type="hidden" class="form-control" value="" id="contador_curso" name="contador_curso" maxlength="100" placeholder="" autocomplete="off"></td>
					
						<table class="table">
							<tr>
								<td><label class="col-form-label">Orientacao: </label></td>
								<td colspan="6"><input type="text" class="form-control" value="" id="orientacao" name="orientacao" maxlength="100" placeholder="" autocomplete="off" ></td>
							</tr>
							<tr>
								<td><label class="col-form-label">Treinamento: </label></td>
								<td colspan="6"><input type="text" class="form-control" value="" id="treinamento" name="treinamento" maxlength="100" placeholder="" autocomplete="off" ></td>
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
								<td colspan="2"><input type="text" class="form-control" value="" id="horas" name="horas" placeholder="EX: Empresa da nota" autocomplete="off" >		
							</tr>
						</table>

						<table id="destino_responsavel" class="table table-borderless">
							<tr>
								<td><label class="col-form-label">Campos para registro: </label></td>
								<td colspan="5" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn" style="cursor: pointer;" onclick="duplicarCamposResponsavel();">Add</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="removerCamposResponsavel();">Remove</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="allremoverCamposResponsavel();">Remove all clone</button>
								</td>
							</tr>
							<tr>
								<td><label class="col-form-label">Responsavel: </label></td>
								<td><label class="col-form-label">Descricao: </label></td>
							</tr>
							<tr>
								<td colspan="1"><input type="text" class="form-control" value="" id="nome_responsavel0" name="nome_responsavel0" maxlength="54" placeholder="Ex: Serial" autocomplete="off"></td>
								<td colspan="1"><input type="text" class="form-control" value="" id="descricao_responsavel0" name="descricao_responsavel0" maxlength="100" placeholder="Ex: descricao" autocomplete="off" ></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_responsavel">
								<td colspan="1"><input type="text" class="form-control" value="" id="nome_responsavel" name="nome" maxlength="54" placeholder="" autocomplete="off"></td>
								<td colspan="1"><input type="text" class="form-control" value="" id="descricao_responsavel" name="descricao_responsavel" maxlength="100" placeholder="" autocomplete="off" ></td>
							</tr>
						</table>

						<table id="destino_funcionario" class="table table-borderless">
							<tr>
								<td><label class="col-form-label">Campos para registro: </label></td>
								<td colspan="5" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn" style="cursor: pointer;" onclick="duplicarCamposFuncionario();">Add</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="removerCamposFuncionario();">Remove</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="allremoverCamposFuncionario();">Remove all clone</button>
								</td>
							</tr>
							<tr>
								<td><label class="col-form-label">Funcionario: </label></td>
							</tr>
							<tr>
								<td colspan="1"><input type="text" class="form-control" value="" id="funcionario0" name="funcionario0" maxlength="54" placeholder="Ex: Serial" autocomplete="off"></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_funcionario">
								<td><input type="text" class="form-control" value="" id="funcionario" name="funcionario" maxlength="54" placeholder="Ex: Serial" autocomplete="off"></td>
							</tr>
							</tr>
						</table>


						<table id="destino_curso" class="table table-borderless">
							<tr>
								<td><label class="col-form-label">Campos para registro: </label></td>
								<td colspan="5" class="alinhar-direita">
									<!--Botoes com js para criar e deletar campos-->
									<button type="button" class="btn" style="cursor: pointer;" onclick="duplicarCamposCurso();">Add</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="removerCamposCurso();">Remove</button>
									<button type="button" class="btn" style="cursor: pointer;" onclick="allremoverCamposCurso();">Remove all clone</button>
								</td>
							</tr>
							<tr>
								<td><label class="col-form-label">Curso: </label></td>
							</tr>
							<tr>
								<td colspan="1"><input type="text" class="form-control" value="" id="curso0" name="curso0" maxlength="54" placeholder="Ex: Serial" autocomplete="off"></td>
							</tr>
						</table>
						<table style="display: none;">
							<tr id="clonar_curso">
								<td><input type="text" class="form-control" value="" id="curso" name="curso" maxlength="54" placeholder="Ex: Serial" autocomplete="off"></td>
							</tr>
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
			<th>Arquivo</th>
			<th>Arquivo</th>
		</tr>
	</thead>
	<tbody>
		<?php
		$arquivos = glob("{*.pdf}", GLOB_BRACE);
		foreach($arquivos as $arquivo) echo "
		<tr>
			<th>{$arquivo}</th>
			<th>
				<a href='{$arquivo}' download>{$arquivo}</a>
			</th>
		</tr>";
		?>
	</tbody>
</table>

<script type="text/javascript" src="./js/js-geral-responsavel.js"></script>
<script type="text/javascript" src="./js/js-geral-funcionario.js"></script>
<script type="text/javascript" src="./js/js-geral-curso.js"></script>
