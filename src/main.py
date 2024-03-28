import os
from rembg import remove
from PIL import Image


def removebg(input_path):
    original_img = Image.open(input_path)
    no_bg_img = remove(original_img)
    
    filename = os.path.splitext(input_path)[0]
    output_path = filename + ".png"

    no_bg_img.save(output_path)


if __name__ == "__main__":
    input_path = 'image.jpg'
    removebg(input_path)
    print('Fundo removido com sucesso')