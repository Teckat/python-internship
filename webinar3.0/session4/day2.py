from PIL import Image, ImageDraw, ImageFont
import os


def generate(name, date):

    path = os.path.join(os.getcwd(), 'webinar3.0', 'session4')

    image = Image.open(r''+path+'\download.jpg')

    draw = ImageDraw.Draw(image)

    fontname = ImageFont.truetype(
        r''+path+'\SansitaSwashed-VariableFont_wght.ttf', 15)

    fontdate = ImageFont.truetype(
        r''+path+'\SansitaSwashed-VariableFont_wght.ttf', 17)

    #  name

    (x, y) = (290, 230)
    color = 'rgb(0,0,0)'

    (w, h) = draw.textsize(name, font=fontname)

    # draw
    draw.text((x-(w/2), y), name, fill=color, font=fontname)

    # date

    (x, y) = (100, 340)
    color = 'rgb(0,0,0)'

    (w, h) = draw.textsize(date, font=fontdate)

    # draw
    draw.text((x-(w/2), y), date, fill=color, font=fontdate)

    # # save

    image.save(r''+path+'\generated.pdf')


generate('Ajay Kumar', '30/09/2020')
