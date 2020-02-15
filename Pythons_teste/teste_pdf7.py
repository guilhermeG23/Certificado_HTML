import pdfkit

#Necessário instalar programa -> wkhtmltopdf






"""
t0 = int(input("Certificado 0 ou 1: "))

t11 = int(input("Quantidade de nomes: "))
t12 = t11

t1 = []

while t11 != 0:
    entrada = input("Nome: ")
    t1.append(entrada)
    t11 -= 1

t2 = input("Descrição: ")
t3 = input("Data: ")
t4 = input("Horas: ")
t5 = input("Assinatura 1: ")
t6 = input("Assinatura descricao: ")
t7 = input("Assinatura 2: ")
t8 = input("Assinatura descricao: ")
t9 = input("Assinatura 3: ")
t10 = input("Assinatura descricao: ")

arquivo = open("teste.html", "w", encoding='utf-8')

css = 'css.css'

arquivo.write("<!DOCTYPE html><html><head><meta http-equiv='Content-type' content='text/html; charset=utf-8'/><meta name='pdfkit-page-size' content='Legal'/><meta name='pdfkit-orientation' content='Landscape'/></head><body>")

while t12 != 0:
    arquivo.write("<table class='moldura'><tr class='bloco-grande'><th class='bloco'><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'><img class='imagem' src='./ramenzoni.png'/></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'></tr><tr class='bloco-grande'><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco' colspan='3'><p class='titulo'>Certificado</p><p class='titulo texto-nome'>")
    arquivo.write(t1[t12-1])                                        
    arquivo.write("</p></th><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th></tr><tr class='bloco-grande'><td colspan='5'><p class='texto descricao'>E com satisfacao que confiro-lhe o certificado, por sua participacao no treinamento de ")
    arquivo.write(t2)
    arquivo.write(" realizado ")
    arquivo.write(t3) 
    arquivo.write(" com carga horaria de ")
    arquivo.write(t4)
    arquivo.write(" horas totais.</p></td></tr>")

    contador = 0
    if len(t5) > 0:
        contador += 1
    if len(t7) > 0:
        contador += 1
    if len(t9) > 0:
        contador += 1

    if contador == 1:

        if len(t5) > 0:
            nome = t5
            assin = t6
        if len(t7) > 0:
            nome = t7
            assin = t8
        if len(t9) > 0:
            nome = t9
            assin = t10

        arquivo.write("<tr class='margin-elementos bloco-grande'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco bloco-assinatura' colspan='3'><hr><p class='texto-assinatura'>")
        arquivo.write(nome)
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(assin)
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-escuro'></th></tr></table>")

    elif contador == 2:

        nomes = []

        if len(t5) > 0:
            nomes.append(t5)
            nomes.append(t6)
        if len(t7) > 0:
            nomes.append(t7)
            nomes.append(t8)
        if len(t9) > 0:
            nomes.append(t9)
            nomes.append(t10)

        arquivo.write("<th class='bloco bloco-assinatura' colspan='2'><hr><p class='texto-assinatura'>")
        arquivo.write(nomes[0])
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(nomes[1])
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco bloco-assinatura' colspan='2'><hr><p class='texto-assinatura'>")
        arquivo.write(nomes[2])
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(nomes[3])
        arquivo.write("</p></th></tr></table>")

    elif contador == 3:    
        arquivo.write("<tr class='margin-elementos bloco-grande'><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(t5)
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(t6)
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(t7)
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(t8)
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(t9)
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(t10)
        arquivo.write("</p></th></tr></table>")

    arquivo.write("<br>")

    t12 -= 1

arquivo.write("</body></html>")

arquivo.close()

if t0 == 0:
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'orientation': 'landscape' # Mudar a orientação da página
    }
else:
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
    }

"""
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
}

array = ['certificado.html', 'descricao.html', 'certificado.html', 'descricao.html']

pdfkit.from_file(array, 'teste1.pdf', options=options)
#pdfkit.from_file('certificado.html', 'teste1.pdf', options=options)