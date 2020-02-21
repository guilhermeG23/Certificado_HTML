//Iniciando o contador
var incrementadorResponsavel = 1;

//CArregando o primeiro incremento no input invisivel
mandarcontadorResponsavel();

//Funcao para clonar_responsavel os campos em display: none
function duplicarCamposResponsavel(){

	//Seguranca de somente 3 responsaveis
	if (document.getElementById('contador_responsavel').value > 2) {
		return true;
	}
	
	//Clonaodo os campos
	var clone = document.getElementById('clonar_responsavel').cloneNode(true);
	var destino_responsavel = document.getElementById('destino_responsavel');
	destino_responsavel.appendChild(clone);
	clone.id = 'clonar_responsavel[' + incrementadorResponsavel + ']';
	
	//Criando os ids para os campos clonados
	document.getElementById('nome_responsavel').id = "nome_responsavel" + incrementadorResponsavel + "";
	document.getElementById('descricao_responsavel').id = "descricao_responsavel" + incrementadorResponsavel + "";
	
	//Alterando os nome_responsavels dos campos
	document.getElementById("nome_responsavel" + incrementadorResponsavel + "").name = "nome_responsavel" + incrementadorResponsavel + "";
	document.getElementById("descricao_responsavel" + incrementadorResponsavel + "").name = "descricao_responsavel" + incrementadorResponsavel + "";
	
	//Incrementar
	incrementadorResponsavel++;

	//Ativar funcao
	mandarcontadorResponsavel();
}

//Atribuir valor ao contador hidden do registro de equipamento
function mandarcontadorResponsavel() {
	document.getElementById('contador_responsavel').value = incrementadorResponsavel;
}

//Remover campos -1
function removerCamposResponsavel(){
	if(incrementadorResponsavel > 1) {
		var node = document.getElementById('destino_responsavel');
		node.removeChild(node.childNodes[incrementadorResponsavel]);
		incrementadorResponsavel--;
		mandarcontadorResponsavel();
	}
}

//apagar todos os campos criado exceto o default
//Mesma coisa do que ta acima, mas com um for para 
function allremoverCamposResponsavel(){
	for(var t = 1; t < incrementadorResponsavel; incrementadorResponsavel--) {
		var node = document.getElementById('destino_responsavel');
		node.removeChild(node.childNodes[incrementadorResponsavel]);
		mandarcontadorResponsavel();
	}
	mandarcontadorResponsavel();
}
