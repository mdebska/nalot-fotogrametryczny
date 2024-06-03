from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from sec import *

nx = 0
ny = 0
dx = 0
dy = 0

def calcpq(nx, ny, dx, dy, lx, ly):
    nx = np.ceil(nx)
    ny = np.ceil(ny)
    by = dy / ny
    bx = dx / (nx - 4)
    p = 100 * (lx - bx) / lx
    q = 100 * (ly - by) / ly
    return p, q


class Sam:
    name: str
    velocityRange: tuple
    height: int
    flightTime: int

    def __init__(self, n, vr, h, t):
        self.name = n
        self.velocityRange = vr
        self.height = h
        self.flightTime = t


class Cam:
    matrixSize: tuple = (int, int)
    pxSize: float
    spectCanal: tuple = (str, str, str, str)
    focal: int
    workCycle: float
    weight: int

    def __init__(self, ms, pxs, sc, f, wc, w):
        self.matrixSize = ms
        self.pxSize = pxs
        self.spectCanal = sc
        self.focal = f
        self.workCycle = wc
        self.weight = w


class Ui_MainWindow(object):
    def __init__(self):

        self.statusbar = None
        self.wizualizacja_button = None
        self.label_11 = None
        self.label_14 = None
        self.punktA_Y = None
        self.label_4 = None
        self.punktA_X = None
        self.punktB_Y = None
        self.label_12 = None
        self.param_q = None
        self.label_10 = None
        self.label_2 = None
        self.gsd = None
        self.label_3 = None
        self.model_sam = None
        self.hmax = None
        self.label_9 = None
        self.punktB_X = None
        self.label_5 = None
        self.label_15 = None
        self.gridLayout_2 = None
        self.pushButton = None
        self.plainTextEdit = None
        self.param_p = None
        self.hmin = None
        self.label_7 = None
        self.label_6 = None
        self.gridLayoutWidget_2 = None
        self.label_8 = None
        self.model_kam = None
        self.gridLayout = None
        self.gridLayoutWidget = None
        self.label = None
        self.centralwidget = None
        self.main = None
        self.window = None

    def openGraphWindow(self):
        global nx, ny, dx, dy
        self.window = QtWidgets.QApplication([])
        self.main = SecWin(nx, ny, dx, dy)
        self.main.show()
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 490, 189))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.model_kam = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.model_kam.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.model_kam.setObjectName("model_kam")
        self.model_kam.addItem("")
        self.model_kam.addItem("")
        self.model_kam.addItem("")
        self.model_kam.addItem("")
        self.gridLayout.addWidget(self.model_kam, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.hmax = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.hmax.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.hmax.setMaximum(99999.99)
        self.hmax.setObjectName("hmax")
        self.gridLayout.addWidget(self.hmax, 5, 1, 1, 1)
        self.model_sam = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.model_sam.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.model_sam.setObjectName("model_sam")
        self.model_sam.addItem("")
        self.model_sam.addItem("")
        self.model_sam.addItem("")
        self.model_sam.addItem("")
        self.gridLayout.addWidget(self.model_sam, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gsd = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.gsd.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.gsd.setMaximum(1000000000.0)
        self.gsd.setObjectName("gsd")
        self.gridLayout.addWidget(self.gsd, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.param_q = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.param_q.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.param_q.setMaximum(100.0)
        self.param_q.setObjectName("param_q")
        self.gridLayout.addWidget(self.param_q, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.hmin = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.hmin.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.hmin.setMaximum(10000.0)
        self.hmin.setObjectName("hmin")
        self.gridLayout.addWidget(self.hmin, 4, 1, 1, 1)
        self.param_p = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.param_p.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.param_p.setMaximum(100.0)
        self.param_p.setObjectName("param_p")
        self.gridLayout.addWidget(self.param_p, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 460, 491, 141))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 420, 241, 31))
        self.pushButton.setStyleSheet("background-color: rgb(115, 167, 10);\n"
                                      "font: 10pt \"NSimSun\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonClicked)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 250, 490, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.punktB_X = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.punktB_X.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.punktB_X.setMaximum(1000000000.0)
        self.punktB_X.setObjectName("punktB_X")
        self.gridLayout_2.addWidget(self.punktB_X, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setStyleSheet("font: 10pt \"Mongolian Baiti\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 2)
        self.punktB_Y = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.punktB_Y.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.punktB_Y.setMaximum(999999999.99)
        self.punktB_Y.setObjectName("punktB_Y")
        self.gridLayout_2.addWidget(self.punktB_Y, 5, 1, 1, 1)
        self.punktA_X = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.punktA_X.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.punktA_X.setMaximum(9999999999.99)
        self.punktA_X.setObjectName("punktA_X")
        self.gridLayout_2.addWidget(self.punktA_X, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.punktA_Y = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.punktA_Y.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.punktA_Y.setMaximum(999999.99)
        self.punktA_Y.setObjectName("punktA_Y")
        self.gridLayout_2.addWidget(self.punktA_Y, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setStyleSheet("font: 8pt \"Mongolian Baiti\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setStyleSheet("font: 10pt \"Mongolian Baiti\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 2)
        self.wizualizacja_button = QtWidgets.QPushButton(self.centralwidget)
        self.wizualizacja_button.setGeometry(QtCore.QRect(270, 610, 241, 28))
        self.wizualizacja_button.setStyleSheet("background-color: rgb(29, 169, 255);\n"
                                               "font: 10pt \"NSimSun\";")
        self.wizualizacja_button.setObjectName("wizualizacja_button")
        self.wizualizacja_button.clicked.connect(self.openGraphWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buttonClicked(self):
        global nx, ny, dx, dy
        nx, ny, dx, dy = self.obliczenia(self.param_p.value(), self.param_q.value(),
                        self.punktA_X.value(), self.punktA_Y.value(), self.punktB_X.value(), self.punktB_Y.value(),
                        self.gsd.value(), self.hmin.value(), self.hmax.value(), self.model_sam.currentText(),
                        self.model_kam.currentText())

    def obliczenia(self, p, q, pAX, pAY, pBX, pBY, GSD, Hmin, Hmax, sam, cam):
        if sam == 'Cessna 402':
            x = Sam(sam, (132, 428), 8200, 5)
        elif sam == 'Cessna T206H NAV III':
            x = Sam(sam, (100, 280), 4785, 5)
        elif sam == 'Vulcan Air P68 Obeserver 2':
            x = Sam(sam, (135, 275), 6100, 6)
        else:
            x = Sam(sam, (120, 267), 4572, 6)
        if cam == 'Z/I DMC IIe 230':
            y = Cam((15552, 14144), 5.6, ('R', 'G', 'B', 'NIR'), 92, 1.8, 63)
        elif cam == 'Leica DMC III':
            y = Cam((25728, 14592), 3.9, ('R', 'G', 'B', 'NIR'), 92, 1.9, 63)
        elif cam == 'UltraCam Falcon M2 70':
            y = Cam((17310, 11310), 6.0, ('R', 'G', 'B', 'NIR'), 70, 1.35, 61)
        else:
            y = Cam((23010, 14790), 4.6, ('R', 'G', 'B', 'NIR'), 80, 1.65, 61)

        Dx = abs(pAX - pBX)
        Dy = abs(pAY - pBY)
        W = GSD * 10 * y.focal / y.pxSize  # wysokość fotografowania
        # print('W', W)
        m = y.focal / W  # skala zdjęcia
        Lx = (y.matrixSize[1] * GSD) / 100  # terenowy zasięg zdjęcia wzdłuż kierunku lotu
        Ly = (y.matrixSize[0] * GSD) / 100  # terenowy zasięg zdjęcia w poprzek kierunku lotu
        # print('lx', Lx, 'ly', Ly)
        Bx = Lx * (100 - p) / 100  # baza podłużna
        By = Ly * (100 - q) / 100  # baza pooprzeczna
        # print('bx', Bx, 'by', By)
        Pz = Lx * Ly  # terenowa powierzchnia zdjęcia
        Pm = (Lx - Bx) * Ly  # terenowa powierzchnia modelu stereoskopowego
        Pn = Bx * By  # powierzchnia użyteczna (nowa) modelu
        Ny = Dy / By  # liczba szeregów
        Nx = Dx / Bx + 4  # liczba zdjęć w szeregu
        Hsr = (Hmin + Hmax) / 2
        H_abs = W + Hsr
        if H_abs > x.height:
            text = f'Absolut height is grater than plane ceiling ({H_abs} > {x.height}'
            self.plainTextEdit.setPlainText(text)
            return Nx, Ny
        new_p, new_q = calcpq(Nx, Ny, Dx, Dy, Lx, Ly)
        Nx = np.ceil(Nx)
        Ny = np.ceil(Ny)
        deltaT = Bx / x.velocityRange[1]
        if deltaT < y.workCycle:
            text = f'Time interval between expositions is shorter than camera work cycle ({deltaT} < {y.workCycle}'
            self.plainTextEdit.setPlainText(text)
            return Nx, Ny
        N = Nx * Ny
        K = N * Pn / (Dx * Dy)
        if Dx > Dy:
            l = Dx
        else:
            l = Dy
        s = l * Ny
        t1 = (s / x.velocityRange[0] / 1000) + (
                (Ny - 1) * (140 / 3600))  # czas bez przylotu i dolotu do lotniska !!
        t2 = (s / x.velocityRange[1] / 1000) + (
                (Ny - 1) * (140 / 3600))  # czas bez przylotu i dolotu do lotniska !!
        t = (t1 / 60, t2 / 60)  # w minutach
        text = (
            f'Liczba zdjęć: {N}\nDługość drogi przelotu [km]: {round(s / 1000, 4)}\nMinimalny czas przelotu [min]: '
            f'{round(t2 * 60, 4)}\nMaksymalny czas przelotu [min]: {round(t1 * 60, 4)}')
        self.plainTextEdit.setPlainText(text)
        return Nx, Ny, Dx, Dy

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WYBÓR PARAMETRÓW POMIARU:"))
        self.model_kam.setItemText(0, _translate("MainWindow", "Z/I DMC IIe 230"))
        self.model_kam.setItemText(1, _translate("MainWindow", "Leica DMC III"))
        self.model_kam.setItemText(2, _translate("MainWindow", "UltraCam Falcon M2 70"))
        self.model_kam.setItemText(3, _translate("MainWindow", "UltraCam Eagle M2 80"))
        self.label_8.setText(_translate("MainWindow", "Wysokość maksymalna obszaru (Hmax)"))
        self.label_9.setText(_translate("MainWindow", "Model samolotu"))
        self.model_sam.setItemText(0, _translate("MainWindow", "Cessna 402"))
        self.model_sam.setItemText(1, _translate("MainWindow", "Cessna T206H NA V III"))
        self.model_sam.setItemText(2, _translate("MainWindow", "Vulcan Air P68 Obeserver 2"))
        self.model_sam.setItemText(3, _translate("MainWindow", "Tencam MMA"))
        self.label_3.setText(_translate("MainWindow", "Parametr q"))
        self.label_2.setText(_translate("MainWindow", "Parametr p"))
        self.label_10.setText(_translate("MainWindow", "Model kamery"))
        self.label_7.setText(_translate("MainWindow", "Wysokość minimalna obszaru (Hmin)"))
        self.label_6.setText(_translate("MainWindow", "Piksel ortofotomapy (GSD)"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Zatwierdź</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_5.setText(_translate("MainWindow", "Współrzędna X"))
        self.label_12.setText(_translate("MainWindow", "Punkt A - prawy górny róg"))
        self.label_15.setText(_translate("MainWindow", "Wszpółrzędna X"))
        self.label_4.setText(_translate("MainWindow", "Współrzędna Y"))
        self.label_14.setText(_translate("MainWindow", "Współrzędna Y"))
        self.label_11.setText(_translate("MainWindow", "Punkt B - lewy dolny róg"))
        self.wizualizacja_button.setText(_translate("MainWindow", "WIZUALIZACJA LOTU"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.destroyed.connect(QtWidgets.qApp.quit)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
