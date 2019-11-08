#coding: utf-8
from  UI_Lane import MainUI
from PyQt5 import QtWidgets,QtGui
from extract_xy import on_mouse
import cv2
class MainWindow(QtWidgets.QMainWindow,MainUI):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.showMinimized)
        self.left_photo.clicked.connect(self.open_photo)
        self.right_1_yuan_label.clicked.connect(self.save_niao)
        self.left_1_chose.clicked.connect(self.chose_axis)


    def open_photo(self):
        self.fname,_ = QtWidgets.QFileDialog.getOpenFileName(self,"打开待检测车道图片",'/home/zach/ZK/Algorithms/Zachary/半自动车道线检测/lane_photos',"Image files (*.jpg *.png)")
        self.right_1_yuan.setPixmap(QtGui.QPixmap(self.fname))
    def save_niao(self):
        self.fname = QtWidgets.QFileDialog.getSaveFileName(self,'保存图片','/home/zach/ZK/Algorithms/Zachary/半自动车道线检测/lane_photos',"Image files (*.jpg *.png)")


    def chose_axis(self):
        global img, img2, ROI
        img = cv2.imread(self.fname)

        # ---------------------------------------------------------
        # --图像预处理，设置其大小
        #height, width = img.shape[:2]
        #size = (int(width * 0.3), int(height * 0.3))
        #img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        # ------------------------------------------------------------
        ROI = img.copy()
        cv2.namedWindow('src')
        cv2.setMouseCallback('src', on_mouse)
        cv2.imshow('src', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()