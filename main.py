#создай тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PIL import *
from PyQt5.QtGui import QPixmap
import os

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700,500)

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка") 
lw_files = QListWidget()

btn_left = QPushButton("Лево") 
btn_right = QPushButton("Право") 
btn_flip = QPushButton("Зеркало") 
btn_sharp = QPushButton("Резкость") 
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout() 
col1 = QVBoxLayout() 
col2 = QVBoxLayout()

col1.addWidget(btn_dir,alignment = Qt.AlignLeft)
col1.addWidget(lw_files,alignment = Qt.AlignLeft)
col2.addWidget(lb_image, 95)


row_tools = QHBoxLayout() # и строка кнопок 
row_tools.addWidget(btn_left,alignment = Qt.AlignRight)
row_tools.addWidget(btn_right,alignment = Qt.AlignRight)
row_tools.addWidget(btn_flip,alignment = Qt.AlignRight)
row_tools.addWidget(btn_sharp,alignment = Qt.AlignRight)
row_tools.addWidget(btn_bw,alignment = Qt.AlignRight)

row.addLayout(col1,20)
col2.addLayout(row_tools)
row.addLayout(col2,80)

main_win.setLayout(row)

main_win.show()

workdir = ''

def filter(files, extensions):
    result = [] 
    for filename in files: 
        for ext in extensions:
            if filename.endswith(ext): 
                result.append(filename) 
                return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    #extensions = ['.txt','.xml']
    chooseWorkdir() 
    filenames = filter(os.listdir(workdir), extensions) 
    lw_files.clear() 
    for filename in filenames:
        lw_files.addItem(filename)
def LoadImage(self,filename):
    pass

def ShowFile():
    lb_image.hide()
    pixmapimage = QPixmap(path)
    w = lb_image.width()
    h = lb_image.height()
    pixmapimage = pixmapimage.scaled(w, h, Ot.KeepAspectRatio)
    lb_image.setPixmap(pixmapimage)
    lb_image.show()

btn_dir.clicked.connect(showFilenamesList)
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def showImage(self):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w = lb_image.width()
        h = lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Ot.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    def showChosenImage():
        

        lv_files.currentRowChanged.connect(showChosenImage())
#btn_bw.clicked.connect(workimage.do_bw)
workimage = ImageProcessor()
app.exec_()