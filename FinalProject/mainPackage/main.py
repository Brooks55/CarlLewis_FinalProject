# main.py

import json
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from locationPackage.location import *



with open('hints.json') as f:
    data = json.load(f)
#print(data['Carl Lewis'])

json_file = 'hints.json'
english_file = 'english.txt'
team = 'Carl Lewis'

decrypted_location = decrypt_location(json_file, english_file, team)
print(decrypted_location)



im = Image.open("../image.jpg")
my_image = load_image("../image.jpg")
try:
    my_image.show(my_image)
except Exception as e: 
    print(e)
    pass 