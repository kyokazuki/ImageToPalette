from PIL import Image, ImageColor, ImagePalette
import os, sys
from math import floor 

if __name__ == '__main__':
    # check arguments
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print('Invalid number of arguments!')
        quit()

    if os.path.isfile(f'{sys.argv[1]}') != True:
        print(f'Image "{sys.argv[1]}" does not exist!')
        quit()

    if os.path.isfile(f'palettes/{sys.argv[2]}') != True:
        print(f'Palette "{sys.argv[2]}" does not exist!')
        quit()

    # open image and load pixel map
    image = Image.open(f'{sys.argv[1]}')
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pxl_map = image.load()

    # import palette in RGB
    palette_file = open(f'palettes/{sys.argv[2]}', 'r')
    palette_hex = palette_file.read().splitlines()

    palette_rgb = []
    for i in palette_hex:
        palette_rgb.append(ImageColor.getrgb(i))

    # replace pixels with color from palette
    def Distance(a, b):
        d = 0
        for i in range(3):
            d += (a[i]-b[i])**2
        return d

    size = image.size[0]*image.size[1]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pxl = image.getpixel((x, y))
            d_min = 3*255**2
            for i, j in enumerate(palette_rgb):
                d = Distance(pxl, j)
                if d < d_min:
                    d_min = d
                    pxl_map[x, y] = j
        print(f'Converting... {floor(x*(image.size[1]+1)*100/size)}%', end='\r', flush=True)

    # save output
    if len(sys.argv) == 4:
        output_file = f'{sys.argv[3]}'
    else:
        output_file = f'{os.path.splitext(sys.argv[1])[0]}_{sys.argv[2]}{os.path.splitext(sys.argv[1])[1]}'

    image.save(output_file)
    print(f'Converted image saved to "{output_file}"!')

