from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image


def qrreader(kep_utvonal):
    kep = Image.open(kep_utvonal)
    result = decode(kep)
    return result


print(qrreader(r'C:\Users\filepz\Desktop\qr1.jpg'))
