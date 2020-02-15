#pip install reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import sys

def main(args):
    cnv = canvas.Canvas("alomundo.pdf")
    width, height = A4
    cnv.drawString(150,450,"Alô mundo!")
    cnv.save()
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))