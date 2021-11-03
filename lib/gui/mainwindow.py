import sys
import os
import tkinter as tk
import qdarkstyle
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QAction,
    QStatusBar,
    QVBoxLayout,
)
from PySide2.QtGui import (
    QIcon
)

import lib.core.file_manipulation as file_manip

from lib.gui.MainWidget import MainWidget
import lib.gui.commonFunctions as cofunc

import lib.core.ivec as ivec

_STR_PROJECT_FOLDER = os.path.normpath(os.path.realpath(__file__) + '/../../../')

_INT_SCREEN_WIDTH = tk.Tk().winfo_screenwidth()  # get the screen width
_INT_SCREEN_HEIGHT = tk.Tk().winfo_screenheight()  # get the screen height
_INT_WIN_WIDTH = 1024  # this variable is only for the if __name__ == "__main__"
_INT_WIN_HEIGHT = 512  # this variable is only for the if __name__ == "__main__"

_INT_MAX_STRETCH = 100000  # Spacer Max Stretch
_INT_BUTTON_MIN_WIDTH = 50  # Minimum Button Width
_INT_SPACES = 10  # Set Spaces for Menu Items

# Icon Paths
_ICON_PATH_LOGO_32x32 = _STR_PROJECT_FOLDER + '/icon/crabsMLearning_32x32.png'
_ICON_PATH_OPEN_128x128 = _STR_PROJECT_FOLDER + '/icon/open_128x128.png'
_ICON_PATH_SETTINGS_48x48 = _STR_PROJECT_FOLDER + '/icon/settings_48_48.png'
_ICON_PATH_EXIT_APP_48x48 = _STR_PROJECT_FOLDER + '/icon/exit_app_48x48.png'
_ICON_PATH_CALENDAR_48x48 = _STR_PROJECT_FOLDER + '/icon/calendar_48x48.png'


class MainWindowTemplate(QMainWindow):
    def __init__(self, app, w=512, h=512, minW=256, minH=256, winTitle='My Window', iconPath='', parent=None):
        super(MainWindowTemplate, self).__init__(parent)  # super().__init__()
        self.app = app
        # ----------------------------- #
        # ----- Set Other Widgets ----- #
        # ----------------------------- #
        self.mainWidget = MainWidget(maxW=None, maxH=None)

        # -------------------------- #
        # ----- Set MainWindow ----- #
        # -------------------------- #
        self.setStyle_()
        self.setWindowTitle(winTitle)  # Set Window Title
        self.setWindowIcon(QIcon(iconPath))  # Set Window Icon
        self.setGeometry(_INT_SCREEN_WIDTH / 4, _INT_SCREEN_HEIGHT / 4, w, h)  # Set Window Geometry
        self.setMinimumWidth(minW)  # Set Window Minimum Width
        self.setMinimumHeight(minH)  # Set Window Minimum Height

        self.vbox_main_layout = QVBoxLayout(self)  # Create the main vbox

        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.vbox_main_layout)

        # ----------------------- #
        # ----- Set MenuBar ----- #
        # ----------------------- #
        self.mainMenu = self.menuBar()  # Set the Menu Bar

        # ***** ACTIONS ***** #
        self.actionExit = QAction(QIcon(_ICON_PATH_EXIT_APP_48x48), 'Exit' + self.setSpaces(_INT_SPACES))  # Exit
        self.actionExit.setShortcut('Ctrl+Q')  # Ctrl + Q
        self.actionExit.setToolTip('Application exit.')  # ToolTip
        # ******************* #

        self.actionIVEC = QAction('ivec')

        self.createMenuBar()  # Create all Menu/Sub-Menu/Actions

        # ---------------------------- #
        # ----- Set Main Content ----- #
        # ---------------------------- #

        # ------------------------- #
        # ----- Set StatusBar ----- #
        # ------------------------- #
        self.statusBar = QStatusBar()  # Create Status Bar

        # ------------------------------- #
        # ----- Set Actions Signals ----- #
        # ------------------------------- #
        self.setActions_SignalSlots()  # Contains all the actions

        # --------------------- #
        # ----- Variables ----- #
        # --------------------- #
        self.my_ivec = ivec.IVEC()
        self.dict_ivecPaths = {}

    # -------------------------- #
    # ----- Static Methods ----- #
    # -------------------------- #
    @staticmethod
    def widgetDialogParams(widget: QWidget):
        widget.setWindowModality(Qt.ApplicationModal)
        # widget.setWindowFlags(Qt.WindowStaysOnTopHint)

    @staticmethod
    def setSpaces(number):
        return number * ' '

    # ---------------------------- #
    # ----- Override Methods ----- #
    # ---------------------------- #

    def closeEvent(self, event):
        self.actionExit_func_()

    # ------------------------------ #
    # ----- Non-Static Methods ----- #
    # ------------------------------ #

    def setMainWindow(self):
        self.mainWidget.setWidget()
        self.vbox_main_layout.addWidget(self.mainWidget)

    def setStyle_(self):
        self.app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

    def createMenuBar(self):
        """
        This function runs all the createMenuBar* menu functions to create each menu.
        By default the template have a Menu File and a Menu Tool
        :return: Nothing
        """
        # Create Menu
        self.createMenuBarFile()  # File
        self.createMenuBarTools()  # Tools

    def createMenuBarFile(self):
        """
        Use this function to create the Menu File.
        Useful Commands:
        menuMain = self.mainMenu.addMenu('NewMenuName')
        menuMain.addAction(self.Action)  # add action created in def __init__()
        menuMain.addSeparator()  # add a separator line between Actions/Menus
        menuNewMenu = menuMain.addMenu("NewMenu")  # create a new Menu inside menuMain
        :return: Nothing
        """
        menuFile = self.mainMenu.addMenu('File')  # File
        # Set Actions and Menus to menuFile
        menuImport = menuFile.addMenu('Import')
        menuImport.addAction(self.actionIVEC)
        # Project Actions (New Project, Open, Save, etc)
        menuFile.addSeparator()  # Separator
        # Action Exit
        menuFile.addAction(self.actionExit)

    def createMenuBarTools(self):
        """
        Use this function to create the Menu File.
        Useful Commands:
        menuMain = self.mainMenu.addMenu('NewMenuName')
        menuMain.addAction(self.Action)  # add action created in def __init__()
        menuMain.addSeparator()  # add a separator line between Actions/Menus
        menuNewMenu = menuMain.addMenu("NewMenu")  # create a new Menu inside menuMain
        :return: Nothing
        """
        menuTools = self.mainMenu.addMenu('Tools')  # File
        # Set Actions and Menus to menuTools
        # Project Menu/Actions (Calendar, Machine Learning, )
        menuTools.addSeparator()

    # ------------------- #
    # ----- Actions ----- #
    # ------------------- #
    def setActions_SignalSlots(self):
        """
        A function for storing all the trigger connections
        :return: Nothing
        """
        # ----------------- #
        # Triggered Actions #
        # ----------------- #
        # ********* #
        # Menu FILE #
        # ********* #
        self.actionExit.triggered.connect(self.actionExit_func_)  # actionExit
        self.actionIVEC.triggered.connect(self.actionIVEC_func_)  # actionIVEC

        # ----------- #
        # Main Widget #
        # ----------- #
        self.mainWidget.listWidget_Path_Images.currentItemChanged.connect(self.actionIVECPathSelection_func_)
        self.mainWidget.listWidget_X_Images.currentItemChanged.connect(self.actionListXSelectionChanged_func_)
        self.mainWidget.listWidget_Y_Images.currentItemChanged.connect(self.actionListYSelectionChanged_func_)

    # ************ #
    # *** File *** #
    # ************ #
    def actionExit_func_(self):
        self.close()  # close the application
        QApplication.closeAllWindows()

    def actionIVEC_func_(self):
        success, dialog = cofunc.openFileDialog(classRef=self,
                                                  dialogName='Pick an IVEC',
                                                  dialogOpenAt=file_manip.PATH_HOME,
                                                  dialogFilters=["*.ivec"],
                                                  dialogMultipleSelection=True)
        if success:
            for filePath in dialog.selectedFiles():
                baseName = os.path.basename(filePath)
                self.dict_ivecPaths[baseName] = filePath
                self.mainWidget.listWidget_Path_Images.addItem(baseName)

    def actionIVECPathSelection_func_(self):
        fileName = self.mainWidget.listWidget_Path_Images.currentItem().text()
        filePath = self.dict_ivecPaths[fileName]
        self.my_ivec.load_ivec(filePath)

        labels_x = self.my_ivec.getXLabels()
        labels_y = self.my_ivec.getYLabels()

        self.mainWidget.listWidget_X_Images.clear()
        self.mainWidget.listWidget_Y_Images.clear()

        for label in labels_x:
            self.mainWidget.listWidget_X_Images.addItem(label)

        for label in labels_y:
            self.mainWidget.listWidget_Y_Images.addItem(label)

        if labels_x.__len__() > 0:
            self.mainWidget.listWidget_X_Images.setCurrentRow(0)
        if labels_y.__len__() > 0:
            self.mainWidget.listWidget_Y_Images.setCurrentRow(0)

    def actionListXSelectionChanged_func_(self):
        currentLabel = self.mainWidget.listWidget_X_Images.currentItem().text()
        currentImageArr = self.my_ivec.getDataX_asArr_at(currentLabel)

        self.mainWidget.setPixmapForLabel_X(currentImageArr)
        self.mainWidget.setPixmapForLabel_Merged()

    def actionListYSelectionChanged_func_(self):
        currentLabel = self.mainWidget.listWidget_Y_Images.currentItem().text()
        currentImageArr = self.my_ivec.getDataY_asArr_at(currentLabel)

        self.mainWidget.setPixmapForLabel_Y(currentImageArr)
        self.mainWidget.setPixmapForLabel_Merged()

    def resizeEvent(self, event):
        if self.mainWidget.listWidget_X_Images.currentItem() is not None:
            self.actionListXSelectionChanged_func_()
        if self.mainWidget.listWidget_Y_Images.currentItem() is not None:
            self.actionListYSelectionChanged_func_()

        labelWidth = (self.width() / 3) - 20
        self.mainWidget.label_ShowImageArea_X.setMaximumWidth(labelWidth)
        self.mainWidget.label_ShowImageArea_Y.setMaximumWidth(labelWidth)
        self.mainWidget.label_ShowImageArea_Merge.setMaximumWidth(labelWidth)

# ******************************************************* #
# ********************   EXECUTION   ******************** #
# ******************************************************* #


def exec_app(w=512, h=512, minW=256, minH=256, winTitle='My Window', iconPath=''):
    myApp = QApplication(sys.argv)  # Set Up Application
    mainWin = MainWindowTemplate(myApp, w=w, h=h, minW=minW, minH=minH, winTitle=winTitle,
                                 iconPath=iconPath)  # Create MainWindow
    mainWin.setMainWindow()
    mainWin.show()  # Show Window
    myApp.exec_()  # Execute Application
    sys.exit(0)  # Exit Application


# ****************************************************** #
# ********************   __main__   ******************** #
# ****************************************************** #
if __name__ == "__main__":
    exec_app(w=1024, h=512, minW=512, minH=256,
             winTitle='ImageViewer', iconPath=_ICON_PATH_LOGO_32x32)
