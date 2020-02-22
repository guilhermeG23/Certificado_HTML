import pdfkit 
import sys
import re
import PyPDF2

def renameSpaces(entrada):
    return re.sub("_", " ", entrada)

def ajusteDatas(data):
    valor = data 
    saida = valor[2:4]

    saida = str(saida)
    mes = ""
    
    if saida == "01":
        mes = "janeiro"
    elif saida == "02":
        mes = "fevereiro"
    elif saida == "03":
        mes = "maio"
    elif saida == "04":
        mes = "abril"
    elif saida == "05":
        mes = "marco"
    elif saida == "06":
        mes= "junho"
    elif saida == "07":
        mes = "julho"
    elif saida == "08":
        mes = "agosto"
    elif saida == "09":
        mes = "setembro"
    elif saida == "10":
        mes = "outubro"
    elif saida == "11":
        mes = "novembro"
    elif saida == "12":
        mes = "dezembro"
    else:
        pass

    return "{} de {} de {}".format(valor[0:2], mes, valor[4:8])

treinamento = sys.argv[1]
data_emissao = sys.argv[2]
data_inicial = sys.argv[3]
data_final = sys.argv[4]
horas = sys.argv[5]
responsaveis = sys.argv[6].split(',')
funcionarios = sys.argv[7].split(',')
cursos = sys.argv[8].split(',')

#Parte certificado
#-----------------------------------------------
arquivo = open("certificado.html", "w", encoding="utf-8")

arquivo.write("<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='pdfkit-page-size' content='A4'/><meta name='pdfkit-orientation' content='Landscape'/><link rel='stylesheet' type='text/css' href='./css/css_a4.css'></head><body>")
for c in range(len(funcionarios)-1, -1, -1):
    arquivo.write("<table class='moldura'><tr><th class='bloco'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'><img class='imagem' src='/var/www/html/imagens/ramenzoni.png'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'></th></tr><tr><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco' colspan='3'><p class='titulo'>CERTIFICADO</p><p class='titulo texto-nome'>")
    arquivo.write(renameSpaces(funcionarios[c]).title())
    arquivo.write("</p></th><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th></tr><tr><td colspan='5'><p class='texto descricao'>É com satisfação que confiro-lhe o certificado, por sua participação no ")
    arquivo.write(renameSpaces(treinamento))
    arquivo.write(" realizado ")

    if int(data_final) == 0:
        arquivo.write(" em  ")
        arquivo.write(ajusteDatas(data_inicial))
    else:
        arquivo.write(" entre os dias ")
        arquivo.write(ajusteDatas(data_inicial))
        arquivo.write(" há ")
        arquivo.write(ajusteDatas(data_final))

    arquivo.write(" com carga horária de ")
    arquivo.write(horas)
    arquivo.write(" horas totais.</p><br>")
    arquivo.write("<p class='texto descricao centro'>Cordeirópolis, ")
    arquivo.write(ajusteDatas(data_emissao))
    arquivo.write("</p></td></tr>")

    if len(responsaveis) == 6:
        arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[0]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[1]).title())
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[2]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[3]).title())
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
        arquivo.write(renameSpaces(responsaveis[4]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[5]).title())
        arquivo.write("</p></th></tr></table></body></html>")
    elif len(responsaveis) == 4:
        arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[0]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[1]).title())
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
        arquivo.write(renameSpaces(responsaveis[2]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[3]).title())
        arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th></tr></table></body></html>")
    elif len(responsaveis) == 2:
        arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura' colspan='3'><hr><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[0]).title())
        arquivo.write("</p><p class='texto-assinatura'>")
        arquivo.write(renameSpaces(responsaveis[1]).title())
        arquivo.write("</p></th><th class='bloco bloco-minimizado' colspan='1'><div class='bloco-interno cor-verde-claro'></th></tr></table>")
    else:
        pass

    arquivo.write("<div class='moldura moldura-descricao'><br><p class='titulo'>Conteúdo programático</p><br><ul class='texto'>")
    for i in range(0, len(cursos)):
        arquivo.write("<li>")
        arquivo.write(renameSpaces(cursos[i]).capitalize())
        arquivo.write("</li>")
    arquivo.write("</ul></div>")

arquivo.write("</body></html>")

arquivo.close()
#-----------------------------------------------

#Saida
#-----------------------------------------------
array_arquivos = ['certificado.html']

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
    'orientation': 'landscape' 
}
pdfkit.from_file(array_arquivos, "pdf.pdf", options=options)

pdf_in = open('pdf.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open('saida.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
#-----------------------------------------------
