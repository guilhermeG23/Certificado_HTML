import pdfkit

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
    'orientation': 'landscape'
}

array = ['certificado.html', 'descricao.html']

pdfkit.from_file(array, 'teste1.pdf', options=options)
