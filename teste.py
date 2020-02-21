import pdfkit 
import sys
import re
import PyPDF2

def renameSpaces(entrada):
    return re.sub("_", " ", entrada)

def ajusteDatas():
    pass

responsaveis = sys.argv[5].split(',')
funcionarios = sys.argv[6].split(',')
cursos = sys.argv[7].split(',')

treinamento = sys.argv[1]
data_inicial = sys.argv[2]
data_final = sys.argv[3]
horas = sys.argv[4]

orientacao = sys.argv[8]

data_emissao = sys.argv[9]

#Parte certificado
#-----------------------------------------------
arquivo = open("certificado.html", "w", encoding='utf-8')

if int(orientacao) == 0:
    arquivo.write("<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='pdfkit-page-size' content='A4'/><meta name='pdfkit-orientation' content='Landscape'/><link rel='stylesheet' type='text/css' href='./css/css_a4.css'></head><body>")
    for c in range(len(funcionarios)-1, -1, -1):
        arquivo.write("<table class='moldura'><tr><th class='bloco'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'><img class='imagem' src='/var/www/html/imagens/ramenzoni.png'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'></th></tr><tr><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco' colspan='3'><p class='titulo'>Certificado</p><p class='titulo texto-nome'>")
        arquivo.write(renameSpaces(funcionarios[c]))
        arquivo.write("</p></th><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th></tr><tr><td colspan='5'><p class='texto descricao'>E com satisfacao que confiro-lhe o certificado, por sua participacao no ")
        arquivo.write(renameSpaces(treinamento))
        arquivo.write(" realizado ")

        if data_final is None:
            arquivo.write(" no dia ")
            arquivo.write(data_inicial)
        else:
            arquivo.write(" entre os dias ")
            arquivo.write(data_inicial)
            arquivo.write(" há ")
            arquivo.write(data_final)

        arquivo.write(" com carga horaria de ")
        arquivo.write(horas)
        arquivo.write(" horas totais.</p><br>")
        arquivo.write("<p class='texto descricao centro'>Cordeiropolis, ")
        arquivo.write(data_emissao)
        arquivo.write("</p></td></tr>")
    
        if len(responsaveis) == 6:
            arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[0]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[1]))
            arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[2]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[3]))
            arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
            arquivo.write(renameSpaces(responsaveis[4]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[5]))
            arquivo.write("</p></th></tr></table></body></html>")
        elif len(responsaveis) == 4:
            arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[0]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[1]))
            arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
            arquivo.write(renameSpaces(responsaveis[2]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[3]))
            arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th></tr></table></body></html>")
        elif len(responsaveis) == 2:
            arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura' colspan='3'><hr><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[0]))
            arquivo.write("</p><p class='texto-assinatura'>")
            arquivo.write(renameSpaces(responsaveis[1]))
            arquivo.write("</p></th><th class='bloco bloco-minimizado' colspan='1'><div class='bloco-interno cor-verde-claro'></th></tr></table>")
        else:
            pass

        arquivo.write("<br><div class='moldura moldura-descricao'><br><p class='titulo'>Conteúdo programático</p><br><ul class='texto'>")
        for i in range((len(cursos)-1),-1,-1):
            arquivo.write("<li>")
            arquivo.write(renameSpaces(cursos[i]).capitalize())
            arquivo.write("</li>")
        arquivo.write("</ul></div>")

if int(orientacao) == 1:
    arquivo.write("<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='pdfkit-page-size' content='A4'/><meta name='pdfkit-orientation' content='Landscape'/><link rel='stylesheet' type='text/css' href='./css/css_meio.css'></head><body>")
    
    for c in range(len(funcionarios), -1, -2):
        
        if funcionarios[c-1] is not None:
            arquivo.write("<table class='moldura'><tr><th class='bloco'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'><img class='imagem' src='/var/www/html/imagens/ramenzoni.png'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'></th></tr><tr><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco' colspan='3'><p class='titulo'>Certificado</p><p class='titulo texto-nome'>")
            arquivo.write(renameSpaces(funcionarios[c-1]))
            arquivo.write("</p></th><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th></tr><tr><td colspan='5'><p class='texto descricao'>E com satisfacao que confiro-lhe o certificado, por sua participacao no ")
            arquivo.write(renameSpaces(treinamento))
            arquivo.write(" realizado ")

            if data_final is None:
                arquivo.write(" no dia ")
                arquivo.write(data_inicial)
            else:
                arquivo.write(" entre os dias ")
                arquivo.write(data_inicial)
                arquivo.write(" há ")
                arquivo.write(data_final)

            arquivo.write(" com carga horaria de ")
            arquivo.write(horas)
        
            arquivo.write(" horas totais.</p><br>")
            arquivo.write("<p class='texto descricao centro'>Cordeiropolis, ")
            arquivo.write(data_emissao)
            arquivo.write("</p></td></tr>")

            if len(responsaveis) == 6:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[2]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[3]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
                arquivo.write(renameSpaces(responsaveis[4]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[5]))
                arquivo.write("</p></th></tr></table></body></html>")
            elif len(responsaveis) == 4:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
                arquivo.write(renameSpaces(responsaveis[2]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[3]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th></tr></table></body></html>")
            else:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura' colspan='3'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado' colspan='1'><div class='bloco-interno cor-verde-claro'></th></tr></table>")
        
        if funcionarios[c-2] is not None:
            arquivo.write("<table class='moldura'><tr><th class='bloco'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'><img class='imagem' src='/var/www/html/imagens/ramenzoni.png'></th><th class='bloco'><div class='bloco-interno cor-verde-claro'></th><th class='bloco'></th></tr><tr><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th><th class='bloco' colspan='3'><p class='titulo'>Certificado</p><p class='titulo texto-nome'>")
            arquivo.write(renameSpaces(funcionarios[c-2]))
            arquivo.write("</p></th><th class='bloco'><div class='bloco-interno cor-verde-escuro'></th></tr><tr><td colspan='5'><p class='texto descricao'>E com satisfacao que confiro-lhe o certificado, por sua participacao no ")
            arquivo.write(renameSpaces(treinamento))
            arquivo.write(" realizado ")

            if data_final is None:
                arquivo.write(" no dia ")
                arquivo.write(data_inicial)
            else:
                arquivo.write(" entre os dias ")
                arquivo.write(data_inicial)
                arquivo.write(" há ")
                arquivo.write(data_final)

            arquivo.write(" com carga horaria de ")
            arquivo.write(horas)
        
            arquivo.write(" horas totais.</p><br>")
            arquivo.write("<p class='texto descricao centro'>Cordeiropolis, ")
            arquivo.write(data_emissao)
            arquivo.write("</p></td></tr>")

            if len(responsaveis) == 6:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[2]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[3]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
                arquivo.write(renameSpaces(responsaveis[4]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[5]))
                arquivo.write("</p></th></tr></table></body></html>")
            elif len(responsaveis) == 4:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura'><hr><p class='texto-assinatura'>")        
                arquivo.write(renameSpaces(responsaveis[2]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[3]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th></tr></table></body></html>")
            else:
                arquivo.write("<tr class='margin-elementos'><th class='bloco bloco-minimizado'><div class='bloco-interno cor-verde-claro'></th><th class='bloco bloco-assinatura' colspan='3'><hr><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[0]))
                arquivo.write("</p><p class='texto-assinatura'>")
                arquivo.write(renameSpaces(responsaveis[1]))
                arquivo.write("</p></th><th class='bloco bloco-minimizado' colspan='1'><div class='bloco-interno cor-verde-claro'></th></tr></table>")
        
        arquivo.write("<br><br><br>")

        arquivo.write("<div class='moldura moldura-descricao'><br><p class='titulo'>Conteúdo programático</p><br><ul class='texto'>")
        for i in range((len(cursos)-1),-1,-1):
            arquivo.write("<li>")
            arquivo.write(renameSpaces(cursos[i]).capitalize())
            arquivo.write("</li>")
        arquivo.write("</ul></div>")
        
        arquivo.write("<div class='moldura moldura-descricao'><br><p class='titulo'>Conteúdo programático</p><br><ul class='texto'>")
        for i in range((len(cursos)-1),-1,-1):
            arquivo.write("<li>")
            arquivo.write(renameSpaces(cursos[i]).capitalize())
            arquivo.write("</li>")
        arquivo.write("</ul></div>")
        
        arquivo.write("<br><br><br>")

arquivo.write("</body></html>")

arquivo.close()
#-----------------------------------------------

#Saida
#-----------------------------------------------
array_arquivos = ['certificado.html']

if int(orientacao) == 0:
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
 
elif int(orientacao) == 1:
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8'
    }
    pdfkit.from_file(array_arquivos, "pdf.pdf", options=options)

else:
    pass
#-----------------------------------------------
