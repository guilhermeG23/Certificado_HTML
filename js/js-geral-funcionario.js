//Iniciando o contador
var incrementadorFuncionario = 1;

//CArregando o primeiro incremento no input invisivel
mandarcontadorFuncionario();

//Funcao para clonar_responsavel os campos em display: none
function duplicarCamposFuncionario(){

	//Clonaodo os campos
	var clone = document.getElementById('clonar_funcionario').cloneNode(true);
	var destino_funcionario = document.getElementById('destino_funcionario');
	destino_funcionario.appendChild(clone);
	clone.id = 'clonar_funcionario[' + incrementadorFuncionario + ']';
	
	//Criando os ids para os campos clonados
	document.getElementById('funcionario').id = "funcionario" + incrementadorFuncionario + "";
	
	//Alterando os responsavels dos campos
	document.getElementById("funcionario" + incrementadorFuncionario + "").name = "funcionario" + incrementadorFuncionario + "";
	
	//Incrementar
	incrementadorFuncionario++;

	//Ativar funcao
	mandarcontadorFuncionario();
}

//Atribuir valor ao contador hidden do registro de equipamento
function mandarcontadorFuncionario() {
	document.getElementById('contador_funcionario').value = incrementadorFuncionario;
}

//Remover campos -1
function removerCamposFuncionario(){
	if(incrementadorFuncionario > 1) {
		var node = document.getElementById('destino_funcionario');
		node.removeChild(node.childNodes[incrementadorFuncionario]);
		incrementadorFuncionario--;
		mandarcontadorFuncionario();
	}
}

//apagar todos os campos criado exceto o default
//Mesma coisa do que ta acima, mas com um for para 
function allremoverCamposFuncionario(){
	for(var t = 1; t < incrementadorFuncionario; incrementadorFuncionario--) {
		var node = document.getElementById('destino_funcionario');
		node.removeChild(node.childNodes[incrementadorFuncionario]);
		mandarcontadorFuncionario();
	}
	mandarcontadorFuncionario();
}
