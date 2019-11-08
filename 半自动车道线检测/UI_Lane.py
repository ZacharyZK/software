#coding:utf-8

from PyQt5 import  QtCore,QtGui,QtWidgets
import sys
import qtawesome

class MainUI(object):
    def setupUi(self,MainWindow):
        super().__init__()
        self.setMouseTracking(True)
        self.setWindowTitle("半自动车道线检测系统")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icons/K.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(1000,1000)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setFixedSize(200,980)
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        self.left_widget.setStyleSheet('''
                            QPushButton{border:none;color:white;}
                            QRadioButton{border:none;color:white;font-size:18px;font-weight:500}
                            QCheckBox{border:none;color:white;font-size:18px;font-weight:500}
                            QPushButton#left_label{
                                border:none;
                                border-top:1px solid white;
                                border-bottom:1px solid white;
                                font-size:18px;
                                font-weight:500;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QPushButton#left_label_little{
                                border:none;
                                font-size:14px;
                                font-weight:500;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QPushButton#left_button:hover{border-left:4px solid red;font-size:20px;font-weight:600;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                            QRadioButton#left_radiobutton:hover{color:red;font-size:20px;font-weight:600;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}                           
                            QCheckBox#left_checkbox:hover{color:green;font-size:20px;font-weight:600;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;}
                            QWidget#left_widget{
                                background:gray;
                                border-top:1px solid white;
                                border-bottom:1px solid white;
                                border-left:1px solid white;
                                border-top-left-radius:10px;
                                border-bottom-left-radius:10px;
                            }
                            QLabel#left_num{
                                color:black;
                                background:white;
                                border-width:0;
                                border:none;
                                border-style:outset;
                                font-size:18px;
                                font-weight:400;
                                font-family:"Helvetica Neue",Helvetica,Arial,sans_serif;
                            }
                        ''')





        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setFixedSize(780,980)
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)
        self.right_widget.setStyleSheet('''
                            
                            QLabel#right_label{
                                        border-image:url(:/icon/picture/car1.jpg);
                                        border-top-right-radius:10px;
                                        border-bottom-right-radius:10px;
                                        border-top-left-radius:10px;
                                        border-bottom-left-radius:10px;
                            }
                            QWidget#right_widget{
                                        background:gray;
                                        border-top:1px solid white;
                                        border-bottom:1px solid white;
                                        border-left:1px solid gray;
                                        border-right:1px solid gray;
                                        border-top-right-radius:10px;
                                        border-bottom-right-radius:10px;
                            }
                            QPushButton{border:none;color:white;}
                            QPushButton#right_button:hover{border-left:4px solid red;border-right:4px solid red;font-size:20px;font-weight:600;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
                            QLabel#right_label_title{
                                        color:white;
                                        font-size:20px;
                                        font-weight:500;          
                            }
                       ''')
        self.main_layout.addWidget(self.left_widget,0,0,16,3)
        self.main_layout.addWidget(self.right_widget,0,3,16,13)
        self.setCentralWidget(self.main_widget)

        self.left_close = QtWidgets.QPushButton(qtawesome.icon('fa.close',color='white'),'')
        self.left_mini = QtWidgets.QPushButton(qtawesome.icon('fa.minus',color='white'),'')
        self.left_info = QtWidgets.QPushButton(qtawesome.icon('fa.info',color='white'),'')
        self.left_clear = QtWidgets.QPushButton(qtawesome.icon('fa.trash',color='white'),'')

        self.left_close.setFixedSize(25,25)
        self.left_mini.setFixedSize(25,25)
        self.left_info.setFixedSize(25,25)
        self.left_clear.setFixedSize(25,25)
        self.left_close.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_info.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:blue;}''')
        self.left_clear.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:yellow;}''')

        self.left_label1 = QtWidgets.QPushButton('提取车道图像')
        self.left_label1.setObjectName('left_label')
        self.left_label2 = QtWidgets.QPushButton('提取车道像素点')
        self.left_label2.setObjectName('left_label')
        self.left_label3 = QtWidgets.QPushButton('车道线检测')
        self.left_label3.setObjectName('left_label')

        self.left_photo  = QtWidgets.QPushButton(qtawesome.icon('fa.photo',color='white'),'打开图片')
        self.left_photo.setObjectName('left_button')
        self.left_1_run = QtWidgets.QPushButton(qtawesome.icon('fa.play-circle-o',color='white'),'生成仿射图像')
        self.left_1_run.setObjectName('left_button')
        self.left_2_run = QtWidgets.QPushButton(qtawesome.icon('fa.play-circle-o', color='white'), '生成')
        self.left_2_run.setObjectName('left_button')
        self.left_2_noise = QtWidgets.QPushButton(qtawesome.icon('fa.wrench',color='white'),'去噪')
        self.left_2_noise.setObjectName('left_button')
        self.left_3_run = QtWidgets.QPushButton(qtawesome.icon('fa.play-circle-o', color='white'), '生成')
        self.left_3_run.setObjectName('left_button')
        self.left_3_ni = QtWidgets.QPushButton(qtawesome.icon('fa.undo',color='white'),'逆仿射')
        self.left_3_ni.setObjectName('left_button')

        self.left_1_top_left = QtWidgets.QPushButton('左上角坐标：')
        self.left_1_top_left.setObjectName('left_label_little')
        self.left_1_top_right = QtWidgets.QPushButton('右上角坐标：')
        self.left_1_top_right.setObjectName('left_label_little')
        self.left_1_bottom_left = QtWidgets.QPushButton('左下角坐标：')
        self.left_1_bottom_left.setObjectName('left_label_little')
        self.left_1_bottom_right = QtWidgets.QPushButton('右下角坐标：')
        self.left_1_bottom_right.setObjectName('left_label_little')

        self.left_1_top_left_num_x = QtWidgets.QLabel('X')
        self.left_1_top_left_num_x.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_top_left_num_x.setObjectName('left_num')
        self.left_1_top_left_num_y = QtWidgets.QLabel('Y')
        self.left_1_top_left_num_y.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_top_left_num_y.setObjectName('left_num')
        self.left_1_top_right_num_x = QtWidgets.QLabel('X')
        self.left_1_top_right_num_x.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_top_right_num_x.setObjectName('left_num')
        self.left_1_top_right_num_y = QtWidgets.QLabel('Y')
        self.left_1_top_right_num_y.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_top_right_num_y.setObjectName('left_num')
        self.left_1_bottom_left_num_y = QtWidgets.QLabel('Y')
        self.left_1_bottom_left_num_y.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_bottom_left_num_y.setObjectName('left_num')
        self.left_1_bottom_left_num_x = QtWidgets.QLabel('X')
        self.left_1_bottom_left_num_x.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_bottom_left_num_x.setObjectName('left_num')
        self.left_1_bottom_right_num_y  =QtWidgets.QLabel('Y')
        self.left_1_bottom_right_num_y.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_bottom_right_num_y.setObjectName('left_num')
        self.left_1_bottom_right_num_x = QtWidgets.QLabel('X')
        self.left_1_bottom_right_num_x.setAlignment(QtCore.Qt.AlignCenter)
        self.left_1_bottom_right_num_x.setObjectName('left_num')

        self.left_1_chose = QtWidgets.QPushButton('选择X/Y')
        #self.left_1_top_left_chose.setFixedSize(20, 20)
        self.left_1_chose.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_1_clear = QtWidgets.QPushButton('清除')
        #self.left_1_top_left_clear.setFixedSize(20, 20)
        self.left_1_clear.setStyleSheet(
            '''QPushButton{background:gray;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.binary_2 = QtWidgets.QCheckBox("二值化")
        self.binary_2.setChecked(True)
        self.binary_2.setObjectName('left_checkbox')
        self.binary_2_low = QtWidgets.QLineEdit("")
        self.binary_2_high = QtWidgets.QLineEdit("")
        #self.binary_2.toggled.connect(self.fdjls)
        self.HSL_2 = QtWidgets.QCheckBox("HSL")
        self.HSL_2_low = QtWidgets.QLineEdit("")
        self.HSL_2_high = QtWidgets.QLineEdit("")
        self.HSL_2.setChecked(False)
        self.HSL_2.setObjectName('left_checkbox')





        self.left_3_2lane = QtWidgets.QRadioButton("检测两条车道线")
        self.left_3_2lane.setChecked(True)
        self.left_3_2lane.setObjectName('left_radiobutton')
        self.left_3_3lane = QtWidgets.QRadioButton("检测三条车道线")
        self.left_3_3lane.setObjectName('left_radiobutton')






        self.left_layout.addWidget(self.left_close,0,0,1,1)
        self.left_layout.addWidget(self.left_mini,0,1,1,1)
        self.left_layout.addWidget(self.left_clear,0,2,1,1)
        self.left_layout.addWidget(self.left_info,0,3,1,1)
        self.left_layout.addWidget(self.left_label1,1,0,1,4)
        self.left_layout.addWidget(self.left_photo,2,0,1,4)
        self.left_layout.addWidget(self.left_1_chose,3,0,1,2)
        self.left_layout.addWidget(self.left_1_clear,3,2,1,2)

        self.left_layout.addWidget(self.left_1_top_left,4,0,1,2)
        #self.left_layout.addWidget(self.left_1_top_left_chose,4,0,1,1)
        #self.left_layout.addWidget(self.left_1_top_left_clear,4,1,1,1)
        self.left_layout.addWidget(self.left_1_top_left_num_x,4,2,1,1)
        self.left_layout.addWidget(self.left_1_top_left_num_y,4,3,1,1)
        self.left_layout.addWidget(self.left_1_top_right,5,0,1,2)
        #self.left_layout.addWidget(self.left_1_top_right_chose,6,0,1,1)
        #self.left_layout.addWidget(self.left_1_top_right_clear,6,1,1,1)
        self.left_layout.addWidget(self.left_1_top_right_num_x,5,2,1,1)
        self.left_layout.addWidget(self.left_1_top_right_num_y, 5, 3, 1,1)
        self.left_layout.addWidget(self.left_1_bottom_left,6,0,1,2)
        #self.left_layout.addWidget(self.left_1_bottom_left_chose,8,0,1,1)
        #self.left_layout.addWidget(self.left_1_bottom_left_clear,8,1,1,1)
        self.left_layout.addWidget(self.left_1_bottom_left_num_x,6,2,1,1)
        self.left_layout.addWidget(self.left_1_bottom_left_num_y, 6, 3, 1, 1)
        self.left_layout.addWidget(self.left_1_bottom_right,7,0,1,2)
        #self.left_layout.addWidget(self.left_1_bottom_right_chose,10,0,1,1)
        #self.left_layout.addWidget(self.left_1_bottom_right_clear,10,1,1,1)
        self.left_layout.addWidget(self.left_1_bottom_right_num_x,7,2,1,1)
        self.left_layout.addWidget(self.left_1_bottom_right_num_y, 7, 3, 1, 1)
        self.left_layout.addWidget(self.left_1_run,11,0,1,4)
        self.left_layout.addWidget(self.left_label2,12,0,1,4)

        self.left_layout.addWidget(self.binary_2,13,0,1,2)
        self.left_layout.addWidget(self.binary_2_low,13,2,1,1)
        self.left_layout.addWidget(self.binary_2_high,13,3,1,1)
        self.left_layout.addWidget(self.HSL_2,14,0,1,2)
        self.left_layout.addWidget(self.HSL_2_low,14,2,1,1)
        self.left_layout.addWidget(self.HSL_2_high,14,3,1,1)
        self.left_layout.addWidget(self.left_2_run,15,0,1,2)
        self.left_layout.addWidget(self.left_2_noise,15,2,1,2)
        self.left_layout.addWidget(self.left_label3,16,0,1,4)

        self.left_layout.addWidget(self.left_3_2lane,17,0,1,4)
        self.left_layout.addWidget(self.left_3_3lane,18,0,1,4)
        self.left_layout.addWidget(self.left_3_run,19,0,1,2)
        self.left_layout.addWidget(self.left_3_ni,19,2,1,2)
        ####################################################################

        self.right_title = QtWidgets.QLabel("半    自    动    车    道    线    检    测    系    统")
        self.right_title.setObjectName('right_title')
        self.right_title.setAlignment(QtCore.Qt.AlignCenter)
        self.right_title.setFixedSize(760, 100)
        self.right_title.setStyleSheet('''
                                                    QLabel#right_title{
                                                        color:white;
                                                        border-image:url(:/icon/picture/cool_car.jpg);
                                                        border-width:0;
                                                        border:none;
                                                        border-style:outset;
                                                        border-top-right-radius:10px;
                                                        border-bottom-right-radius:10px;
                                                        border-bottom-left-radius:10px;
                                                        border-top-left-radius:10px;
                                                        font-size:30px;
                                                        font-weight:700;
                                                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                                    }
                                                ''')
        self.right_1_yuan = QtWidgets.QLabel("")
        self.right_1_yuan.setObjectName("right_label")
        self.right_1_yuan.setScaledContents(True)
        self.right_1_yuan.setFixedSize(275,200)
        self.right_1_yuan_label = QtWidgets.QPushButton("原始图像")
        self.right_1_yuan_label.setObjectName("right_button")
        self.right_1_niao = QtWidgets.QLabel("")
        self.right_1_niao.setFixedSize(275, 200)
        self.right_1_niao.setObjectName("right_label")
        self.right_1_niao.setScaledContents(True)
        self.right_1_niao_label = QtWidgets.QPushButton("仿射图像")
        self.right_1_niao_label.setObjectName("right_button")

        self.right_2_pixel = QtWidgets.QLabel("")
        self.right_2_pixel.setObjectName("right_label")
        self.right_2_pixel.setFixedSize(275, 200)
        self.right_2_pixel.setScaledContents(True)
        self.right_2_pixel_label = QtWidgets.QPushButton("像素图像")
        self.right_2_pixel_label.setObjectName("right_button")
        self.right_2_noise = QtWidgets.QLabel("")
        self.right_2_noise.setObjectName("right_label")
        self.right_2_noise.setFixedSize(275, 200)
        self.right_2_noise.setScaledContents(True)
        self.right_2_noise_label = QtWidgets.QPushButton("去噪图像")
        self.right_2_noise_label.setObjectName("right_button")

        self.right_3_get = QtWidgets.QLabel("")
        self.right_3_get.setObjectName("right_label")
        self.right_3_get.setFixedSize(275, 200)
        self.right_3_get.setScaledContents(True)
        self.right_3_get_label = QtWidgets.QPushButton("检测图像")
        self.right_3_get_label.setObjectName("right_button")
        self.right_3_ni = QtWidgets.QLabel("")
        self.right_3_ni.setObjectName("right_label")
        self.right_3_ni.setFixedSize(275, 200)
        self.right_3_ni.setScaledContents(True)
        self.right_3_ni_label = QtWidgets.QPushButton("逆仿射图像")
        self.right_3_ni_label.setObjectName("right_button")




        self.right_1_label = QtWidgets.QLabel("提取车道图像过程")
        self.right_1_label.setObjectName("right_label_title")
        self.right_2_label = QtWidgets.QLabel("提取车道像素过程")
        self.right_2_label.setObjectName("right_label_title")
        self.right_3_label = QtWidgets.QLabel("车道线检测过程")
        self.right_3_label.setObjectName("right_label_title")







        self.right_layout.addWidget(self.right_title,0,0,2,13)
        self.right_layout.addWidget(self.right_1_label,2,0,1,5)
        self.right_layout.addWidget(self.right_1_yuan,3,1,3,5)
        self.right_layout.addWidget(self.right_1_yuan_label,6,1,1,5)
        self.right_layout.addWidget(self.right_1_niao,3,7,3,5)
        self.right_layout.addWidget(self.right_1_niao_label,6,7,1,5)
        self.right_layout.addWidget(self.right_2_label,7,0,1,5)
        self.right_layout.addWidget(self.right_2_pixel,8,1,3,5)
        self.right_layout.addWidget(self.right_2_pixel_label,11,1,1,5)
        self.right_layout.addWidget(self.right_2_noise,8,7,3,5)
        self.right_layout.addWidget(self.right_2_noise_label,11,7,1,5)
        self.right_layout.addWidget(self.right_3_label,12,0,1,5)
        self.right_layout.addWidget(self.right_3_get,13,1,3,5)
        self.right_layout.addWidget(self.right_3_get_label,16,1,1,5)
        self.right_layout.addWidget(self.right_3_ni,13,7,3,5)
        self.right_layout.addWidget(self.right_3_ni_label,16,7,1,5)

import Icons_rc

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()