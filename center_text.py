from PIL import ImageFont, Image, ImageDraw, ImageChops
import textwrap
import logging

logging.basicConfig(level=logging.DEBUG)

fontsize = 1
font = ImageFont.truetype('impact.ttf', fontsize)


def text_size(text, font, fontsize):
    """To check how big the text size can be!"""
    img = Image.new("RGB", (500, 500))
    draw = ImageDraw.Draw(img)
    img_fraction = 0.75
    while draw.multiline_textsize(text, font)[0] < img_fraction * img.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1

        logging.debug('{} {}'.format(draw.multiline_textsize(text, font), fontsize))
        font = ImageFont.truetype('impact.ttf', fontsize)
    fontsize -= 1
    while draw.multiline_textsize(text, font)[1] > img_fraction * img.size[1]:
        # iterate until the text size is just smaller than the criteria
        fontsize -= 1
        font = ImageFont.truetype('impact.ttf', fontsize)
        logging.debug('{} {}'.format(draw.multiline_textsize(text, font), fontsize))
    return fontsize, draw.multiline_textsize(text, font)[0], draw.multiline_textsize(text, font)[1]


def text_bracke(text, caracter, mode='TW'):
    """This is an help fuction to chuse wich is better"""
    if mode == 'LB':
        return '\n'.join(textwrap.wrap(text, caracter))
    else:
        return textwrap.wrap(text, width=caracter)


def text_layer_size(text, font):
    """Returns the size of te text area in a list
        firtst is """
    img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(img)
    return draw.multiline_textsize(text, font)


def test():
    image = Image.new('RGB', (512, 256), (255, 255, 255))
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype('impact.ttf', 50)

    # drawing text
    STRING = 'Hello, python language!'
    drawer.text((10, 10), STRING, fill='black', font=font)

    # drawing rectangle surrounding text
    size = drawer.textsize(STRING, font=font)
    drawer.rectangle((10, 10, 10 + size[0], 10 + size[1]), outline='black')

    image.show()


def text_center():
    words = [
        ((10, 10), "Red", "#ff0000", 30),
        ((10, 50), "Green", "#00ff00", 30),
        ((10, 90), "Blue", "#0000ff", 30),
        ((10, 130), "White", "#ffffff", 30),
        ((10, 170), "Black", "#000000", 30),
    ]

    # A fully transparent image to work on, and a separate alpha channel.
    im = Image.new("RGB", (120, 210), (0, 0, 0))
    alpha = Image.new("L", im.size, "black")

    for pos, text, color, size in words:
        # Make a grayscale image of the font, white on black.
        imtext = Image.new("L", im.size, 0)
        drtext = ImageDraw.Draw(imtext)
        font = ImageFont.truetype('impact.ttf', size)
        drtext.text(pos, text, font=font, fill="white")

        # Add the white text to our collected alpha channel. Gray pixels around
        # the edge of the text will eventually become partially transparent
        # pixels in the alpha channel.
        alpha = ImageChops.lighter(alpha, imtext)

        # Make a solid color, and add it to the color layer on every pixel
        # that has even a little bit of alpha showing.
        solidcolor = Image.new("RGBA", im.size, color)
        immask = Image.eval(imtext, lambda p: 255 * (int(p != 0)))
        im = Image.composite(solidcolor, im, immask)

    # These two save()s are just to get demo images of the process.
    im.save("transcolor.png", "PNG")
    alpha.save("transalpha.png", "PNG")

    # Add the alpha channel to the image, and save it out.
    im.putalpha(alpha)
    im.save("transtext.png", "PNG")


def gen_center_text(text, width, height):
    img = Image.new("RGBA", (500, 500))
    draw = ImageDraw.Draw(img)
    btext = text_bracke(text, 25, mode='LB')
    #print(draw.multiline_textsize(btext, font))
    logging.debug(text_size(btext, font, fontsize))


if __name__ == '__main__':

    bgimg = Image.new("RGBA", (500,500), "#FFFFFF")
    #bgimg.show()
    gen_center_text("Soon, you will discover that we are not alone. Alien civilizations with their own histories and"
                    " motivations are expanding as well. Research new technology, design starships, negotiate trade "
                    "and treaties, wage wars, colonize new worlds, construct starbases in the largest 4X strategy game "
                    "ever made.", 500, 500)
    #print(text_layer_size("lollolololol0 dsdadasd adsadas asddadsda adsdasdd asdasdas asdasdas asdads", font))
