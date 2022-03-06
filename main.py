#ignacy Bu
from colorit import init_colorit, background
from PIL import Image
import requests,os

shadows = list(" .:-=+*#%@")

def recall():
    a = requests.get("https://thispersondoesnotexist.com/image")
    with open("buff.png",'wb') as f:
        f.write(a.content)
        f.close()

    a.close()
    im = Image.open("buff.png")
    try:
        asci = int(input("asci[0] or color[1]:"))
        size = int(input("size : "))
    except ValueError:
        print("MUST BE A NUMBER")
        recall()
    if asci == 0:
        im = im.resize((size,size))
        im = im.convert("L")

        #init_colorit()


        for y in range(im.size[1]):
            for x in range(im.size[0]):
                consts = int(255 / (len(shadows) - 1))
                print(shadows[int(im.getpixel((x,y))/consts)],end='')
            print()

    elif asci == 1:
        im = im.resize((size, size))

        for y in range(im.size[1]):
            for x in range(im.size[0]):

                print(background(' ',im.getpixel((x, y))), end='')
            print()

    else:
        os.remove("buff.png")
        recall()

    os.remove("buff.png")
    recall()
if __name__ == "__main__":
    recall()

