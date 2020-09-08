#  task 2 -> text on an image

from PIL import Image, ImageDraw, ImageFont

import os

path = os.path.join(os.getcwd(), 'session3')

print(path)

fontSize = ImageFont.truetype(r''+path + '\style\Asul-Regular.ttf', 150)

color = 'rgb(0,0,0)'

image = Image.open(r''+path+'\image\certificate.jpg')

draw = ImageDraw.Draw(image)

draw.text((1500, 1050), 'teckat services private limited',
          fill=color, font=fontSize)


image.save(r''+path+'\generatedImage\\test.jpg')
