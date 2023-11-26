from PIL import Image, ImageDraw
import shutil
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from uic_file import Ui_Dialog

class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.imagePath = ''
        self.current = None
        self.pushButton_red.clicked.connect(self.run)
        self.pushButton_green.clicked.connect(self.run)
        self.pushButton_blue.clicked.connect(self.run)
        self.pushButton_all.clicked.connect(self.run)
        self.pushButton_bright.clicked.connect(self.bright)
        self.pushButton_left.clicked.connect(self.rotate)
        self.pushButton_right.clicked.connect(self.rotate)
        self.pushButton_negative.clicked.connect(self.negative)
        self.pushButton_wb.clicked.connect(self.wb)
        self.pushButton_gray.clicked.connect(self.gray)
        self.pushButton_sepia.clicked.connect(self.sepia)
        self.pushButton_contrast.clicked.connect(self.contrast)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_download.clicked.connect(self.download)
        self.pushButton_orig.clicked.connect(self.orig)

    def contrast(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        avg = 0
        for x in range(width):
            for y in range(height):
                r, g, b = im.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= width * height
        lst = []
        for i in range(256):
            temp = int(avg + 2 * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            lst.append(temp)
        for x in range(width):
            for y in range(height):
                r, g, b = im.getpixel((x, y))
                draw.point((x, y), (lst[r], lst[g], lst[b]))

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def sepia(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                all = (a + b + c) // 3
                a = all + 40 * 2
                b = all + 40
                c = all
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def gray(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                all = (a + b + c) // 3
                draw.point((i, j), (all, all, all))

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def wb(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                all = a + b + c
                if (all > (((255 - 100) // 2) * 3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def negative(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                draw.point((i, j), (255 - a, 255 - b, 255 - c))
        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def bright(self):
        im = Image.open('orig.png')
        x, y = im.size
        pix = im.load()
        draw = ImageDraw.Draw(im)
        width = im.size[0]
        height = im.size[1]
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + 100
                b = pix[i, j][1] + 100
                c = pix[i, j][2] + 100
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def run(self):
        im = Image.open("orig.png")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (self.sender().text() == 'RED'):
                    pixels[i, j] = r, 0, 0
                elif (self.sender().text() == 'GREEN'):
                    pixels[i, j] = 0, g, 0
                elif (self.sender().text() == 'BLUE'):
                    pixels[i, j] = 0, 0, b
                else:
                    pass

        im.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        im = Image.open("orig.png")
        if (self.sender().text() == "RIGHT"):
            degree = -90
        else:
            degree = 90
        im2 = im.rotate(degree, expand=True)
        im2.save("upd.png")
        self.pixmap.load("upd.png")
        self.current = "upd.png"
        self.image.setPixmap(self.pixmap)

    def save(self):

        if self.current:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(
                self, "SaveFileName", "",
                "Image Files (*.png *.jpg *.jpeg *.bmp)",
                options=options)
            if fileName:
                path = shutil.copy(self.current, fileName)

                msg = QtWidgets.QMessageBox.information(
                    self,
                    'Успех',
                    f'Текущий файл {self.current} \nсохранен в {path}.'
                )
        else:
            msg = QtWidgets.QMessageBox.warning(
                self,
                'Внимание',
                'Файл для сохранения не обозначен.'
            )
            return

    def download(self):
        self.imagePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)")
        kk = shutil.copy2(self.imagePath, 'orig.png')

        if not self.imagePath:
            return
        pixmap = QPixmap(self.imagePath)
        self.image.setPixmap(pixmap.scaled(740, 455))

    def orig(self):
        im = Image.open("orig.png")
        im.save("orig.png")
        self.pixmap.load("orig.png")
        self.current = "orig.png"
        self.image.setPixmap(self.pixmap)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_()) 