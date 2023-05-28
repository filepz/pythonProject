from PyPDF2 import PdfWriter, PdfReader
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image
from tqdm import tqdm, trange
from random import random, randint
import re


def pdfcrop(original, target):
    i = 0
    # https://github.com/oschwartz10612/poppler-windows/releases/
    poppler = r'C:\Users\filepz\Downloads\Release-22.04.0-0\poppler-22.04.0\Library\bin'
    pdf = PdfReader(original)
    new = (120, 120)

    for page in pdf.pages:
        page.cropbox.setUpperRight(new)
        out = PdfWriter()
        out.add_page(page)
        cim = 'C:\\Users\\filepz\\Desktop\\pdfcrop\\final{}.pdf'.format(i)
        with open(cim, "wb") as out_f:
            out.write(out_f)
        image = convert_from_path(cim, poppler_path = poppler)
        lo = fasz(image[0])
            # print(i, len(result), str(result[0].data, 'UTF-8'),result[0].quality)
        print(lo, end =" ")

        i = i + 1

def fasz(kep):
    result = decode(kep, symbols=[ZBarSymbol.CODE39])
    if (len(result) > 0):
        fasz2 = str(result[0].data, 'UTF-8')
    else:
        fasz2 = '-'
    return fasz2

def qrreader(kep_utvonal):
    kep = Image.open(kep_utvonal)
    result = decode(kep)
    return result

def bcodecheck(fname):
    pattern1 = re.search("\+[0-9]{6}\.pdf", fname.lower())
    pattern2 = re.search("\$[0-9]{5}\.pdf", fname.lower())
    if pattern1 is not None:
        print(pattern1.group())
    elif pattern2 is not None:
        print(pattern2.group())
    else:
        print("Nem ervenyes formatum")




# a = r'C:\Users\filepz\Desktop\2022K07041_022184_FONOR_Kft_eBeszallitas_1.PDF'


a = r'C:\Users\filepz\Desktop\large3.PDF'
b = r'C:\Users\filepz\Desktop\final.PDF'

# pdfcrop(a, b)
# bcodecheck('$012s34.PDF')
qrreader(r'C:\Users\filepz\Desktop\qr3.jpg')