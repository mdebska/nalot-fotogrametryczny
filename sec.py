import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import Arc
from matplotlib.ticker import FixedLocator, AutoLocator
from matplotlib.patches import Rectangle
import sys


class Demo(FigureCanvas):
    def __init__(self, parent, nx, ny, dx, dy):
        self.nx = int(nx)
        self.ny = int(ny)
        t1 = 0
        t2 = 0
        he = 0
        wi = 0
        fig, self.ax = plt.subplots(figsize=(6, 5), dpi=120)
        super().__init__(fig)
        self.setParent(parent)
        arc_coords = []
        for i in range(self.ny):
            xs, ys = [], []
            for j in range(self.nx):
                x = j
                y = i
                xs.append(x)
                ys.append(y)
                if j == 0 or j == self.nx - 1:
                    if dx < dy:
                        t1 = 90
                        t2 = 270
                        he = 1
                        wi = 3
                        arc_coords.append((x, y))
                    else:
                        t1 = 180
                        t2 = 360
                        he = 3
                        wi = 1
                        arc_coords.append((y, x))
                if dx < dy:
                    self.ax.scatter(x, y, color='k')
                    rect = Rectangle((x-0.5, y-0.5), 1, 1, edgecolor='r', facecolor='none')
                    self.ax.add_patch(rect)
                else:
                    self.ax.scatter(y, x, color='k')
                    rect = Rectangle((y-0.5, x-0.5), 1, 1, edgecolor='r', facecolor='none')
                    self.ax.add_patch(rect)
            if dx < dy:
                self.ax.plot(xs, ys, color='k')
            else:
                self.ax.plot(ys, xs, color='k')
        for i in range(1, len(arc_coords) - 2, 4):
            x1 = arc_coords[i][0]
            y1 = arc_coords[i][1]
            x2 = arc_coords[i + 2][0]
            y2 = arc_coords[i + 2][1]
            midX = abs((x1 + x2) / 2)
            midY = abs((y1 + y2) / 2)
            arc = Arc((midX, midY), wi, he, angle=180, theta1=t1, theta2=t2, color='k')
            self.ax.add_patch(arc)
        for i in range(2, len(arc_coords) - 2, 4):
            x1 = arc_coords[i][0]
            y1 = arc_coords[i][1]
            x2 = arc_coords[i + 2][0]
            y2 = arc_coords[i + 2][1]
            midX = abs((x1 + x2) / 2)
            midY = abs((y1 + y2) / 2)
            arc = Arc((midX, midY), wi, he, angle=180, theta2=t1, theta1=t2, color='k')
            self.ax.add_patch(arc)

        self.ax.set_xlabel('Oś Y')
        self.ax.set_ylabel('Oś X')

        # self.ax.grid(True, which='minor', axis='both', linestyle='--', linewidth=0.5)

        if dx > dy:
            self.ax.xaxis.set_minor_locator(FixedLocator([i - 0.5 for i in range(self.ny)]))
            self.ax.yaxis.set_minor_locator(FixedLocator([i - 0.5 for i in range(self.nx)]))
        else:
            self.ax.xaxis.set_minor_locator(FixedLocator([i - 0.5 for i in range(self.nx)]))
            self.ax.yaxis.set_minor_locator(FixedLocator([i - 0.5 for i in range(self.ny)]))



class SecWin(QWidget):
    def __init__(self, nx, ny, dx, dy):
        super().__init__()
        self.setWindowTitle('Wizualizacja lotu')
        self.resize(700, 600)
        Demo(self, nx, ny, dx, dy)
    def closeEvent(self, event):
        # close application
        print("Window closed")
        self.close()
        sys.exit()
