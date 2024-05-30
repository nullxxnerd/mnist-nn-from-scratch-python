from matrix import *

class Img:
    def __init__(self, label, img_data):
        self.label = label
        self.img_data = img_data

def csv_to_imgs(file_string, number_of_imgs):
    imgs = []
    with open(file_string, 'r') as fp:
        # Read the first line
        fp.readline()
        
        for i in range(number_of_imgs):
            row = fp.readline().strip()
            if not row:
                break
            tokens = row.split(',')
            label = int(tokens[0])
            img_data = Matrix(28, 28)
            for r in range(28):
                for c in range(28):
                    img_data.entries[r][c] = int(tokens[1 + r * 28 + c]) / 256.0
            imgs.append(Img(label, img_data))
    
    return imgs

def img_print(img):
    print(img.img_data)
    print(f"Img Label: {img.label}")

def img_free(img):
    del img

def imgs_free(imgs):
    for img in imgs:
        img_free(img)
    del imgs

