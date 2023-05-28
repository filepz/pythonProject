from tqdm import tqdm, trange
from random import random, randint
from time import sleep

from PyPDF2 import PdfWriter, PdfReader
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from PIL import ImageEnhance

#  https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar
#  https://github.com/NaturalHistoryMuseum/pyzbar/


def progress():
    with trange(100) as t:
        for i in t:
            t.set_description('GEN %i' % i)
            # Postfix will be displayed on the right,
            # formatted automatically based on argument's datatype
            t.set_postfix(loss=random(), barmi = randint(1, 999), str='h',
                      lst=[1, 2])
            sleep(0.1)

progress()




def dekofuggveny(func):
    print(type(func))


def kulsofuggveny(a,b):
    return a+b

#  print(dekofuggveny(kulsofuggveny(25,45)))

#  https://gist.github.com/alexzhan/1270222
