import numpy as np
import json

KEY_METADATA = 'METADATA:'
KEY_NAME = 'NAME:'
KEY_X_DIM = 'X-DIM:'
KEY_X_LABELS = 'X-LABELS:'
KEY_IMAGE_MODE_X = 'IMAGE-MODE-X:'
KEY_Y_DIM = 'Y-DIM:'
KEY_Y_LABELS = 'Y-LABELS:'
KEY_IMAGE_MODE_Y = 'IMAGE-MODE-Y:'
KEY_WIDTH = 'WIDTH:'
KEY_HEIGHT = 'HEIGHT:'

KEY_DATA = 'DATA:'
KEY_X_VEC = 'X:'
KEY_Y_VEC = 'Y:'

KEY_IMG_MODE_RGB = 'RGB'
KEY_IMG_MODE_RGBA = 'RGBA'
KEY_IMG_MODE_GRAYSCALE = 'GRAYSCALE'

KEY_RED = 'RED:'
KEY_GREEN = 'GREEN:'
KEY_BLUE = 'BLUE:'
KEY_ALPHA = 'ALPHA:'
KEY_GRAY = 'GRAY:'


class IVEC:
    def __init__(self):
        self._dict_ivec = {}
        self._set_ivec()

    def _set_ivec(self):
        self._dict_ivec = {
            KEY_METADATA: {
                KEY_NAME: 'Image',
                KEY_X_DIM: None,
                KEY_X_LABELS: [],
                KEY_IMAGE_MODE_X: None,
                KEY_Y_DIM: None,
                KEY_Y_LABELS: [],
                KEY_IMAGE_MODE_Y: None,
                KEY_WIDTH: None,
                KEY_HEIGHT: None
            },
            KEY_DATA: {
                KEY_X_VEC: {},
                KEY_Y_VEC: {}
            }
        }

    # ***** SETTERS ***** #

    def setName(self, name: str):
        self._dict_ivec[KEY_METADATA][KEY_NAME] = name

    def setXDim(self, dim: int):
        self._dict_ivec[KEY_METADATA][KEY_X_DIM] = dim

    def setXLabels(self, labels: []):
        self._dict_ivec[KEY_METADATA][KEY_X_LABELS] = labels

    def setYDim(self, dim: int):
        self._dict_ivec[KEY_METADATA][KEY_Y_DIM] = dim

    def setYLabels(self, labels: []):
        self._dict_ivec[KEY_METADATA][KEY_Y_LABELS] = labels

    def setImageModeX(self, mode: str):
        self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] = mode

    def setImageModeY(self, mode: str):
        self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] = mode

    def setImageWidth(self, width: int):
        self._dict_ivec[KEY_METADATA][KEY_WIDTH] = width

    def setImageHeight(self, height: int):
        self._dict_ivec[KEY_METADATA][KEY_HEIGHT] = height

    def setMetadata(self, name: str, x_dim: int, y_dim: int, width: int, height: int,
                    x_mode: str = KEY_IMG_MODE_GRAYSCALE, y_mode: str = KEY_IMG_MODE_GRAYSCALE):
        self.setName(name)
        self.setXDim(x_dim)
        self.setYDim(y_dim)
        self.setImageModeX(x_mode)
        self.setImageModeY(y_mode)
        self.setImageWidth(width)
        self.setImageHeight(height)

    # ***** GETTERS ***** #

    def getName(self):
        return self._dict_ivec[KEY_METADATA][KEY_NAME]

    def getXDim(self):
        return self._dict_ivec[KEY_METADATA][KEY_X_DIM]

    def getXLabels(self):
        return self._dict_ivec[KEY_METADATA][KEY_X_LABELS]

    def getYDim(self):
        return self._dict_ivec[KEY_METADATA][KEY_Y_DIM]

    def getYLabels(self):
        return self._dict_ivec[KEY_METADATA][KEY_Y_LABELS]

    def getImageModeX(self):
        return self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X]

    def getImageModeY(self):
        return self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y]

    def getImageWidth(self):
        return self._dict_ivec[KEY_METADATA][KEY_WIDTH]

    def getImageHeight(self):
        return self._dict_ivec[KEY_METADATA][KEY_HEIGHT]

    def getMetadata(self):
        return self._dict_ivec[KEY_METADATA]

    def getData(self):
        return self._dict_ivec[KEY_DATA]

    def getDataX(self):
        return self._dict_ivec[KEY_DATA][KEY_X_VEC]

    def getDataX_at(self, label: str):
        if label in self._dict_ivec[KEY_DATA][KEY_X_VEC].keys():
            return self._dict_ivec[KEY_DATA][KEY_X_VEC][label]
        return None

    def getDataX_asArr_at(self, label: str):
        arr = None
        if label in self._dict_ivec[KEY_DATA][KEY_X_VEC].keys():
            if self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] == KEY_IMG_MODE_RGB:
                pass
            elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] == KEY_IMG_MODE_RGBA:
                pass
            elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] == KEY_IMG_MODE_GRAYSCALE:
                arr = np.array(self._dict_ivec[KEY_DATA][KEY_X_VEC][label][KEY_GRAY])
        return arr

    def getDataY(self):
        return self._dict_ivec[KEY_DATA][KEY_Y_VEC]

    def getDataY_at(self, label: str):
        if label in self._dict_ivec[KEY_DATA][KEY_Y_VEC].keys():
            return self._dict_ivec[KEY_DATA][KEY_Y_VEC][label]
        return None

    def getDataY_asArr_at(self, label: str):
        arr = None
        if label in self._dict_ivec[KEY_DATA][KEY_Y_VEC].keys():
            if self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] == KEY_IMG_MODE_RGB:
                pass
            elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] == KEY_IMG_MODE_RGBA:
                pass
            elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] == KEY_IMG_MODE_GRAYSCALE:
                arr = np.array(self._dict_ivec[KEY_DATA][KEY_Y_VEC][label][KEY_GRAY])
        return arr

    def get_ivec(self):
        return self._dict_ivec

    # ***** ADD ***** #

    def addXLabel(self, label):
        self._dict_ivec[KEY_METADATA][KEY_X_LABELS].append(label)

    def addYLabel(self, label):
        self._dict_ivec[KEY_METADATA][KEY_Y_LABELS].append(label)

    def addData_X(self, x: np.ndarray, label=None):
        tmp_label = label
        if tmp_label is None:
            tmp_label = 'X'
            i = 0
            while True:
                if tmp_label + str(i) in self._dict_ivec[KEY_DATA][KEY_X_VEC].keys():
                    i += 1
                else:
                    tmp_label += str(i)
                    self._dict_ivec[KEY_METADATA][KEY_X_LABELS].append(tmp_label)
                    break

        self._dict_ivec[KEY_DATA][KEY_X_VEC][tmp_label] = {}

        if self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] is KEY_IMG_MODE_RGB:
            pass
        elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] is KEY_IMG_MODE_RGBA:
            pass
        elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_X] is KEY_IMG_MODE_GRAYSCALE:
            self._dict_ivec[KEY_DATA][KEY_X_VEC][tmp_label][KEY_GRAY] = x.tolist()

        # print(self._dict_ivec[KEY_DATA][KEY_X_VEC].keys())

    def addData_Y(self, y: np.ndarray, label=None):
        tmp_label = label
        if tmp_label is None:
            tmp_label = 'Y'
            i = 0
            while True:
                if tmp_label + str(i) in self._dict_ivec[KEY_DATA][KEY_Y_VEC].keys():
                    i += 1
                else:
                    tmp_label += str(i)
                    self._dict_ivec[KEY_METADATA][KEY_Y_LABELS].append(tmp_label)
                    self._dict_ivec[KEY_DATA][KEY_Y_VEC][tmp_label] = y.tolist()
                    break

        self._dict_ivec[KEY_DATA][KEY_Y_VEC][tmp_label] = {}

        if self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] is KEY_IMG_MODE_RGB:
            pass
        elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] is KEY_IMG_MODE_RGBA:
            pass
        elif self._dict_ivec[KEY_METADATA][KEY_IMAGE_MODE_Y] is KEY_IMG_MODE_GRAYSCALE:
            self._dict_ivec[KEY_DATA][KEY_Y_VEC][tmp_label][KEY_GRAY] = y.tolist()

        # print(self._dict_ivec[KEY_DATA][KEY_Y_VEC].keys())

    # ***** IMPORTING / EXPORTING ***** #
    def save_ivec(self, pathDir: str):
        fileName = self._dict_ivec[KEY_METADATA][KEY_NAME] + '.ivec'
        with open(pathDir + fileName, 'w') as fp:
            json.dump(self._dict_ivec, fp)

    def load_ivec(self, pathFile: str):
        with open(pathFile, 'r') as fp:
            self._dict_ivec = json.load(fp)

    def print_ivec(self):
        print(self._dict_ivec)
