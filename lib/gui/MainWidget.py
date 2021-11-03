import sys
import os
import tkinter as tk

import cv2
import numpy as np
from PySide2.QtCore import (
    Qt
)
from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    # QPushButton,
    # QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    # QSpacerItem,
    QListWidget,
    QLabel
)
from PySide2.QtGui import (
    QIcon,
    QImage,
    QPixmap,
    qRgb
)


_PROJECT_FOLDER = os.path.normpath(os.path.realpath(__file__) + '/../../../')

_INT_SCREEN_WIDTH = tk.Tk().winfo_screenwidth()  # get the screen width
_INT_SCREEN_HEIGHT = tk.Tk().winfo_screenheight()  # get the screen height
_INT_WIN_WIDTH = 1024  # this variable is only for the if __name__ == "__main__"
_INT_WIN_HEIGHT = 512  # this variable is only for the if __name__ == "__main__"

_INT_MAX_STRETCH = 100000  # Spacer Max Stretch
_INT_BUTTON_MIN_WIDTH = 50  # Minimum Button Width


class MainWidget(QWidget):
    def __init__(self, w=512, h=512, minW=256, minH=256, maxW=512, maxH=512,
                 winTitle='My Window', iconPath=''):
        super().__init__()
        # ---------------------- #
        # ----- Set Window ----- #
        # ---------------------- #
        self.setWindowTitle(winTitle)  # Set Window Title
        self.setWindowIcon(QIcon(iconPath))  # Set Window Icon
        self.setGeometry(_INT_SCREEN_WIDTH / 4, _INT_SCREEN_HEIGHT / 4, w, h)  # Set Window Geometry
        self.setMinimumWidth(minW)  # Set Window Minimum Width
        self.setMinimumHeight(minH)  # Set Window Minimum Height
        if maxW is not None:
            self.setMaximumWidth(maxW)  # Set Window Maximum Width
        if maxH is not None:
            self.setMaximumHeight(maxH)  # Set Window Maximum Width

        self.vbox_main_layout = QVBoxLayout(self)  # Create the main vbox

        # -------------------------- #
        # ----- Set PushButton ----- #
        # -------------------------- #
        # self.buttonNext = QPushButton('Next')
        # self.buttonNext.setMinimumWidth(_INT_BUTTON_MIN_WIDTH)
        # self.buttonPrevious = QPushButton('Previous')
        # self.buttonPrevious.setMinimumWidth(_INT_BUTTON_MIN_WIDTH)

        # -------------------------- #
        # ----- Set ListWidget ----- #
        # -------------------------- #
        self.listWidget_X_Images = QListWidget()
        self.listWidget_X_Images.setMaximumHeight(200)

        self.listWidget_Y_Images = QListWidget()
        self.listWidget_Y_Images.setMaximumHeight(200)

        self.listWidget_Path_Images = QListWidget()
        self.listWidget_Path_Images.setMaximumHeight(200)

        # ---------------------- #
        # ----- Set QLabel ----- #
        # ---------------------- #
        _imageLabelStyle = """
            border: 1px solid black;
            background-color: black;
            """

        self.label_ShowImageArea_X = QLabel()
        self.label_ShowImageArea_X.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_ShowImageArea_X.setStyleSheet(_imageLabelStyle)
        self.label_ShowImageArea_X.setMinimumWidth(minW)
        self.label_ShowImageArea_X.setMinimumHeight(minH)
        self.label_ShowImageArea_X.setMaximumWidth(600)
        self.label_ShowImageArea_X.setMaximumHeight(600)

        self.label_ShowImageArea_Y = QLabel()
        self.label_ShowImageArea_Y.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_ShowImageArea_Y.setStyleSheet(_imageLabelStyle)
        self.label_ShowImageArea_Y.setMinimumWidth(minW)
        self.label_ShowImageArea_Y.setMinimumHeight(minH)
        self.label_ShowImageArea_Y.setMaximumWidth(600)
        self.label_ShowImageArea_Y.setMaximumHeight(600)

        self.label_ShowImageArea_Merge = QLabel()
        self.label_ShowImageArea_Merge.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_ShowImageArea_Merge.setStyleSheet(_imageLabelStyle)
        self.label_ShowImageArea_Merge.setMinimumWidth(minW)
        self.label_ShowImageArea_Merge.setMinimumHeight(minH)
        self.label_ShowImageArea_Merge.setMaximumWidth(600)
        self.label_ShowImageArea_Merge.setMaximumHeight(600)

        # setVariables
        self.arrForPixmap_X = None
        self.arrForPixmap_Y = None

    def setWidget(self):
        # create gridLayout
        gridLayout = QGridLayout()

        # create vbox
        vbox_x_showIMG = QVBoxLayout()
        vbox_y_showIMG = QVBoxLayout()
        vbox_merge_showIMG = QVBoxLayout()

        vbox_x_listIMG = QVBoxLayout()
        vbox_y_listIMG = QVBoxLayout()
        vbox_path_listIMG = QVBoxLayout()

        # create Labels
        label_x_showIMG = QLabel('X Viewer:')
        label_x_showIMG.setMaximumHeight(50)
        label_y_showIMG = QLabel('Y Viewer:')
        label_y_showIMG.setMaximumHeight(50)
        label_merge_showIMG = QLabel('Merge Viewer:')
        label_merge_showIMG.setMaximumHeight(50)

        label_x_channels = QLabel('X Channels:')
        label_x_channels.setMaximumHeight(50)
        label_y_channels = QLabel('Y Channels:')
        label_y_channels.setMaximumHeight(50)
        label_paths = QLabel('Path(s):')
        label_paths.setMaximumHeight(50)

        # add to vboxes
        vbox_x_showIMG.addWidget(label_x_showIMG)
        vbox_x_showIMG.addWidget(self.label_ShowImageArea_X)

        vbox_y_showIMG.addWidget(label_y_showIMG)
        vbox_y_showIMG.addWidget(self.label_ShowImageArea_Y)

        vbox_merge_showIMG.addWidget(label_merge_showIMG)
        vbox_merge_showIMG.addWidget(self.label_ShowImageArea_Merge)

        vbox_x_listIMG.addWidget(label_x_channels)
        vbox_x_listIMG.addWidget(self.listWidget_X_Images)

        vbox_y_listIMG.addWidget(label_y_channels)
        vbox_y_listIMG.addWidget(self.listWidget_Y_Images)

        vbox_path_listIMG.addWidget(label_paths)
        vbox_path_listIMG.addWidget(self.listWidget_Path_Images)

        # add to grid
        gridLayout.addLayout(vbox_x_showIMG, 0, 0)
        gridLayout.addLayout(vbox_y_showIMG, 0, 1)
        gridLayout.addLayout(vbox_merge_showIMG, 0, 2)
        gridLayout.addLayout(vbox_x_listIMG, 1, 0)
        gridLayout.addLayout(vbox_y_listIMG, 1, 1)
        gridLayout.addLayout(vbox_path_listIMG, 1, 2)

        self.vbox_main_layout.addLayout(gridLayout)

    # ------------------- #
    # ----- Actions ----- #
    # ------------------- #
    def setActions_(self):
        self.buttonNext.clicked.connect(self.actionButtonOk)
        self.buttonPrevious.clicked.connect(self.actionButtonOk)

    def actionButtonOk(self):
        # -----> Write here code for ok <-----
        self.close()  # Close the window

    def actionButtonCancel(self):
        self.close()  # Close the window

    # ------------------- #
    # ----- Pixmaps ----- #
    # ------------------- #
    def setPixmapForLabel_X(self, arr: np.ndarray):
        self.label_ShowImageArea_X.clear()

        tmp_arr = arr.copy()
        self.arrForPixmap_X = tmp_arr
        arrShape = tmp_arr.shape
        height = arrShape[0]
        width = arrShape[1]

        tmp_arr = np.reshape(tmp_arr, (width, height))
        tmp_arr = np.require(tmp_arr, np.uint16, 'C')

        img = QImage(tmp_arr.data, width, height, QImage.Format_Grayscale16)

        l_width = self.label_ShowImageArea_X.width()
        l_height = self.label_ShowImageArea_X.height()

        pixmap = QPixmap.fromImage(img)

        self.label_ShowImageArea_X.setPixmap(pixmap.scaled(l_width, l_height, Qt.KeepAspectRatio))

    def setPixmapForLabel_Y(self, arr: np.ndarray):
        self.label_ShowImageArea_Y.clear()

        tmp_arr = arr.copy()
        self.arrForPixmap_Y = tmp_arr
        arrShape = tmp_arr.shape
        height = arrShape[0]
        width = arrShape[1]

        tmp_arr = np.reshape(tmp_arr, (width, height))
        tmp_arr = np.require(tmp_arr, np.uint16, 'C')

        img = QImage(tmp_arr.data, width, height, QImage.Format_Grayscale16)

        l_width = self.label_ShowImageArea_Y.width()
        l_height = self.label_ShowImageArea_Y.height()

        pixmap = QPixmap.fromImage(img)

        self.label_ShowImageArea_Y.setPixmap(pixmap.scaled(l_width, l_height, Qt.KeepAspectRatio))

    def setPixmapForLabel_Merged(self):
        self.label_ShowImageArea_Merge.clear()
        tmp_arr_X = self.arrForPixmap_X
        tmp_arr_Y = self.arrForPixmap_Y

        l_width = self.label_ShowImageArea_Merge.width()
        l_height = self.label_ShowImageArea_Merge.height()

        if tmp_arr_X is not None and tmp_arr_Y is not None:
            tmp_arr_merged = tmp_arr_X + tmp_arr_Y
            arrShape = tmp_arr_merged.shape
            width = arrShape[1]
            height = arrShape[0]

            tmp_arr = np.reshape(tmp_arr_merged, (width, height))
            tmp_arr = np.require(tmp_arr, np.uint16, 'C')

            tmp_arr = np.expand_dims(tmp_arr, axis=0)
            tmp_arr = np.concatenate([tmp_arr, tmp_arr, tmp_arr], axis=0)

            img = QImage(tmp_arr.data, width, height, QImage.Format_Grayscale16)
            pixmap = QPixmap.fromImage(img)
            self.label_ShowImageArea_Merge.setPixmap(pixmap.scaled(l_width, l_height, Qt.KeepAspectRatio))
        else:
            if tmp_arr_X is not None:
                arrShape = tmp_arr_X.shape
                width = arrShape[1]
                height = arrShape[0]

                tmp_arr = np.reshape(tmp_arr_X, (width, height))
                tmp_arr = np.require(tmp_arr, np.uint16, 'C')

                img = QImage(tmp_arr.data, width, height, QImage.Format_Grayscale16)
                pixmap = QPixmap.fromImage(img)
                self.label_ShowImageArea_Merge.setPixmap(pixmap.scaled(l_width, l_height, Qt.KeepAspectRatio))
            if tmp_arr_Y is not None:
                arrShape = tmp_arr_Y.shape
                width = arrShape[1]
                height = arrShape[0]

                tmp_arr = np.reshape(tmp_arr_Y, (width, height))
                tmp_arr = np.require(tmp_arr, np.uint16, 'C')

                img = QImage(tmp_arr.data, width, height, QImage.Format_Grayscale16)
                pixmap = QPixmap.fromImage(img)
                self.label_ShowImageArea_Merge.setPixmap(pixmap.scaled(l_width, l_height, Qt.KeepAspectRatio))


# ******************************************************* #
# ********************   EXECUTION   ******************** #
# ******************************************************* #

def exec_app(w=512, h=512, minW=256, minH=256, maxW=512, maxH=512, winTitle='My Window', iconPath=''):
    myApp = QApplication(sys.argv)  # Set Up Application
    widgetWin = MainWidget(w=w, h=h, minW=minW, minH=minH, maxW=maxW, maxH=maxH,
                           winTitle=winTitle, iconPath=iconPath)  # Create MainWindow
    widgetWin.setWidget()
    widgetWin.show()  # Show Window
    myApp.exec_()  # Execute Application
    sys.exit(0)  # Exit Application


if __name__ == "__main__":
    exec_app(w=1024, h=512, minW=512, minH=256, maxW=512, maxH=512,
             winTitle='WidgetTemplate', iconPath=_PROJECT_FOLDER + '/icon/crabsMLearning_32x32.png')
