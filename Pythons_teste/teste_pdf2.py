from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import sys

def main(args):
    cnv = canvas.Canvas("alomundo.pdf", pagesize=A4)
    width, height = A4
    cnv.drawString(150,450,"Alô mundo!")

    cnv.setLineWidth(.3)
    cnv.setFont('Helvetica', 12)
    
    cnv.drawString(30,750,'COMUNICADO OFICIAL')
    cnv.drawString(30,735,'EMPRESAS ACME')
    cnv.drawString(500,750,"12/12/2011")
    cnv.line(480,747,580,747)
    
    cnv.drawString(275,725,'SALDO DEVEDOR:')
    cnv.drawString(500,725,"R$ 1.000,00")
    cnv.line(378,723,580,723)
    
    cnv.drawString(30,703,'RECEBIDO POR:')
    cnv.line(130,700,580,700)
    cnv.drawString(130,703,"JOHN DOE")



    cnv.save()
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))