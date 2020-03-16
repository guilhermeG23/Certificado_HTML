# Gerando certificado via HTML com Python3

### Requisitos para funcionar
* Python3
* wkhtmltopdf
* Apache
* PHP
* Permissionamento do diretorio com seus arquivos

### Pip
* pip install pdfkit

Para maiores duvidas, segue o link:
https://pypi.org/project/pdfkit/

### Testes
Esse programa foi desenvolvido num sistema linux Debian com python3.

### Funcionamento
* Usuário irá dar a entrada pela Pag Web principal
* Pag PHP irá receber essas entradas e irá configurar formatar os dados
* Após os filtros, o Python vai começar a receber as informações
* Com o Python recebendo as informações, ele irá gerar a pagina HTML
* Por fim o python irá gerar um PDF do HTML e retornar para a página inicial
