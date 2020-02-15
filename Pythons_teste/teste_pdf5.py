from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import sys

def main(args):
    cnv = canvas.Canvas("teste1.pdf", pagesize=A4)
    cnv.translate(cm, cm)
    width, height = A4
    print("{}, {}".format(width, height))
    #X, Y
    cnv.roundRect(0, 0, (width - 60), (height - 50), 0, stroke=1, fill=0)
    cnv.drawImage("ramenzoni.png", 100, 100, width=100, height=100)
    cnv.save()
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))