import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image
import cv2

class Creador():
    def __init__(self):
        self.titulo = "Hola "
        # self.texto = "La asociación civil Da Vida a SP Tlaquepaque te desea que este nuevo ciclo venga con salud y éxito, pasa un día extraordinario. ¡Muchas felicidades!"
        self.path_results = 'results/'

        # self.globos_path = "images/globos.jpg"
        # self.logo_path = "images/logo.jpg"
        # self.banderines_path = "images/banderines.jpg"

        # self.globos_img = cv2.imread(self.globos_path)
        # self.logo_img = cv2.imread(self.logo_path)
        # self.banderines_img = cv2.imread(self.banderines_path)

        self.base_path = "images/base.jpg"
        self.img_base = cv2.imread(self.base_path)

    def create(self, nombre: str, numero: int, fecha: ()):
        img = self.img_base.copy()
        texto = self.titulo + nombre + '!'
        x = 50
        y = 100
        rgb = (0, 0, 0)

        font_path = "fuentes/Subway-Black.ttf"
        font = ImageFont.truetype(font_path, 70)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y),  texto, font = font, fill = (0, 0, 0))
        img = np.array(img_pil)

        # font = cv2.FONT_HERSHEY_TRIPLEX
        # cv2.putText(img, texto, (x, y), font, 3, rgb, 2, cv2.LINE_AA)
        month_folder = self.path_results + str(fecha[0]) + '/'
        day_folder = str(fecha[1]) + '/'
        try:
            os.mkdir(month_folder)
        except:
            pass

        try:
            os.mkdir(month_folder + day_folder)
        except:
            pass
        path_result = month_folder + day_folder + str(numero) + '_' + nombre + '.jpg'
        cv2.imwrite(path_result, img)