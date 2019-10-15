import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QPushButton, QAction
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QObject, pyqtSignal
import matplotlib
matplotlib.use('QT5Agg')

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

app = QApplication(sys.argv)
widget = uic.loadUi('test.ui')

def setGraphs(maxW,first):
        
        x = [50, 50]

        w = int(maxW)
        plt.cla()
        fig, axarr = plt.subplots(w)

        # draw the initial pie chart
        factorX = 0.7
        factorY = 0
        for i in range(0,w):
            axarr[i].pie(x,autopct='%1.1f%%')
            axarr[i].set_position([factorY,factorX,.2,.2])

            factorY = factorY + 0.2
            if factorY == 1.0:
                factorX = factorX - 0.2
                factorY = 0

        
        
        
        canvas = FigureCanvas(fig) 
        plot = QtWidgets.QVBoxLayout(widget.content_plot) 
        plot.addWidget(canvas)

widget.btnStart.clicked.connect(lambda: setGraphs(widget.wInput.text(),False))
widget.show()
sys.exit(app.exec_())