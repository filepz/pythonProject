from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\filepz\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#  eredmeny = pytesseract.image_to_string(Image.open(r'C:\Users\filepz\Desktop\Papirmentes\test.jpg'))

print(pytesseract.image_to_string(r'C:\Users\filepz\Desktop\Papirmentes\test.jpg'))