//Iniciando o contador
var incrementadorCurso = 1;

//CArregando o primeiro incremento no input invisivel
mandarcontadorCurso();

//Funcao para clonar_responsavel os campos em display: none
function duplicarCamposCurso(){

	//Clonaodo os campos
	var clone = document.getElementById('clonar_curso').cloneNode(true);
	var destino_curso = document.getElementById('destino_curso');
	destino_curso.appendChild(clone);
	clone.id = 'clonar_curso[' + incrementadorCurso + ']';
	
	//Criando os ids para os campos clonados
	document.getElementById('curso').id = "curso" + incrementadorCurso + "";
	
	//Alterando os responsavels dos campos
	document.getElementById("curso" + incrementadorCurso + "").name = "curso" + incrementadorCurso + "";
	
	//Required
	document.getElementById("curso" + incrementadorCurso + "").setAttribute('required', 'yes');
	
	//Incrementar
	incrementadorCurso++;

	//Ativar funcao
	mandarcontadorCurso();
}

//Atribuir valor ao contador hidden do registro de equipamento
function mandarcontadorCurso() {
	document.getElementById('contador_curso').value = incrementadorCurso;
}

//Remover campos -1
function removerCamposCurso(){
	if(incrementadorCurso > 1) {
		var node = document.getElementById('destino_curso');
		node.removeChild(node.childNodes[incrementadorCurso]);
		incrementadorCurso--;
		mandarcontadorCurso();
	}
}

//apagar todos os campos criado exceto o default
//Mesma coisa do que ta acima, mas com um for para 
function allremoverCamposCurso(){
	for(var t = 1; t < incrementadorCurso; incrementadorCurso--) {
		var node = document.getElementById('destino_curso');
		node.removeChild(node.childNodes[incrementadorCurso]);
		mandarcontadorCurso();
	}
	mandarcontadorCurso();
}
