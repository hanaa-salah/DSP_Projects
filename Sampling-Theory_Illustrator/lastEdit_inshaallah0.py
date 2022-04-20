# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents\try.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSlider
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from numpy.fft import fft, ifft ,fftfreq
from scipy import signal
from scipy.interpolate import interp1d
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 595) 
        Main_Icon = QtGui.QIcon()
        Main_Icon.addPixmap(QtGui.QPixmap("wicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(Main_Icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_mainwin = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_mainwin.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.outergridLayout_tab1 = QtWidgets.QGridLayout(self.tab1)
        self.outergridLayout_tab1.setObjectName("gridLayout_2")
        self.gridLayout_Tab1 = QtWidgets.QGridLayout()
        self.gridLayout_Tab1.setObjectName("gridLayout_Tab1")
        self.graphicsView_RecSignl =PlotWidget(self.tab1)
        self.graphicsView_RecSignl.setObjectName("graphicsView_RecSignl")
        self.gridLayout_Tab1.addWidget(self.graphicsView_RecSignl, 1, 1, 1, 1)
        self.graphicsView_RecSignl.plotItem.showGrid(x=True, y=True)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_Tab1.addItem(spacerItem, 0, 0, 1, 1)
        self.outer_gridLayout_mainGraph = QtWidgets.QGridLayout()
        self.outer_gridLayout_mainGraph.setObjectName("outer_gridLayout_mainGraph")
        self.inner_gridLayout_mainGraph = QtWidgets.QGridLayout()
        self.inner_gridLayout_mainGraph.setObjectName("inner_gridLayout_mainGraph")
        self.Sampling_Slider = QtWidgets.QLabel(self.tab1)
        self.Sampling_Slider.setObjectName("Sampling_Slider")
        self.inner_gridLayout_mainGraph.addWidget(self.Sampling_Slider, 3, 0, 1, 1)
        self.sample_horizontalSlider = QtWidgets.QSlider(self.tab1)
        self.sample_horizontalSlider.setMinimum(5)
        self.sample_horizontalSlider.setPageStep(5)
        self.sample_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.sample_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sample_horizontalSlider.setObjectName("sample_horizontalSlider")
        self.inner_gridLayout_mainGraph.addWidget(self.sample_horizontalSlider, 2, 0, 1, 1)
        self.Hide_checkBox = QtWidgets.QCheckBox(self.tab1)
        self.Hide_checkBox.setObjectName("Hide_checkBox")
        self.inner_gridLayout_mainGraph.addWidget(self.Hide_checkBox, 3, 1, 1, 1)
        self.graphicsView_main =PlotWidget(self.tab1)
        self.graphicsView_main.setObjectName("graphicsView_main")
        self.inner_gridLayout_mainGraph.addWidget(self.graphicsView_main, 1, 0, 1, 2)
        self.graphicsView_main.plotItem.showGrid(x=True, y=True)
        self.outer_gridLayout_mainGraph.addLayout(self.inner_gridLayout_mainGraph, 0, 0, 1, 1)
        self.gridLayout_Tab1.addLayout(self.outer_gridLayout_mainGraph, 0, 1, 1, 1)
        spacerItem_for_Tab1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_Tab1.addItem(spacerItem_for_Tab1, 0, 2, 1, 1)
        self.outergridLayout_tab1.addLayout(self.gridLayout_Tab1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.outer_gridLayout_tab2 = QtWidgets.QGridLayout(self.tab_2)
        self.outer_gridLayout_tab2.setObjectName("gridLayout_5")
        self.horizontalLayout_composer = QtWidgets.QHBoxLayout()
        self.horizontalLayout_composer.setObjectName("horizontalLayout_composer")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_composer.addWidget(self.line)
        spacerItem_for_composer_horizontal = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_composer.addItem(spacerItem_for_composer_horizontal)
        self.outer_verticalLayout_composer = QtWidgets.QVBoxLayout()
        self.outer_verticalLayout_composer.setObjectName("outer_verticalLayout_composer")
        spacerItem_for_composer_vertical = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.outer_verticalLayout_composer.addItem(spacerItem_for_composer_vertical)
        self.Iner_verticalLayout_composer = QtWidgets.QVBoxLayout()
        self.Iner_verticalLayout_composer.setObjectName("Iner_verticalLayout_composer")
        self.horizontalLayout_generateSig = QtWidgets.QHBoxLayout()
        self.horizontalLayout_generateSig.setObjectName("horizontalLayout_generateSig")
        self.verticalLayout_values = QtWidgets.QVBoxLayout()
        self.verticalLayout_values.setObjectName("verticalLayout_values")
        self.horizontalLayout_values = QtWidgets.QHBoxLayout()
        self.horizontalLayout_values.setObjectName("horizontalLayout_values")
        self.verticalLayout_values.addLayout(self.horizontalLayout_values)
        self.gridLayout_values = QtWidgets.QGridLayout()
        self.gridLayout_values.setObjectName("gridLayout_values")
        self.phase_label = QtWidgets.QLabel(self.tab_2)
        self.phase_label.setObjectName("phase_label")
        self.gridLayout_values.addWidget(self.phase_label, 2, 0, 1, 1)
        self.Freq_label = QtWidgets.QLabel(self.tab_2)
        self.Freq_label.setObjectName("Freq_label")
        self.gridLayout_values.addWidget(self.Freq_label, 1, 0, 1, 1)
        self.magnitude_LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.magnitude_LineEdit.setObjectName("magnitude_LineEdit")
        self.gridLayout_values.addWidget(self.magnitude_LineEdit, 0, 1, 1, 1)
        self.frequency_LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.frequency_LineEdit.setObjectName("frequency_LineEdit")
        self.gridLayout_values.addWidget(self.frequency_LineEdit, 1, 1, 1, 1)
        self.phaseshift_LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.phaseshift_LineEdit.setObjectName("phaseshift_LineEdit")
        self.gridLayout_values.addWidget(self.phaseshift_LineEdit, 2, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.tab_2)
        self.name_label.setObjectName("name_label")
        self.gridLayout_values.addWidget(self.name_label, 3, 0, 1, 1)
        self.nameOfSignal_LineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.nameOfSignal_LineEdit.setObjectName("nameOfSignal_LineEdit")
        self.gridLayout_values.addWidget(self.nameOfSignal_LineEdit, 3, 1, 1, 1)
        self.mag_Label = QtWidgets.QLabel(self.tab_2)
        self.mag_Label.setObjectName("mag_Label")
        self.gridLayout_values.addWidget(self.mag_Label, 0, 0, 1, 1)
        self.verticalLayout_values.addLayout(self.gridLayout_values)
        self.add_Button = QtWidgets.QPushButton(self.tab_2)
        self.add_Button.setObjectName("add_Button")
        self.verticalLayout_values.addWidget(self.add_Button)
        self.verticalLayout_values.setStretch(1, 8)
        self.horizontalLayout_generateSig.addLayout(self.verticalLayout_values)
        self.verticalLayout_comGraph = QtWidgets.QVBoxLayout()
        self.verticalLayout_comGraph.setObjectName("verticalLayout_comGraph")
        self.verticalLayout_generate = QtWidgets.QVBoxLayout()
        self.verticalLayout_generate.setObjectName("verticalLayout_2")
        self.generate_sig_label = QtWidgets.QLabel(self.tab_2)
        self.generate_sig_label.setObjectName("generate_sig_label")
        self.verticalLayout_generate.addWidget(self.generate_sig_label)
        self.graphicsView_genSignal = PlotWidget(self.tab_2)
        self.graphicsView_genSignal.setObjectName("graphicsView_genSignal")
        self.graphicsView_genSignal.plotItem.showGrid(x=True, y=True)
        self.verticalLayout_generate.addWidget(self.graphicsView_genSignal)

        self.verticalLayout_comGraph.addLayout(self.verticalLayout_generate)
        self.horizontalLayout_generateSig.addLayout(self.verticalLayout_comGraph)
        self.horizontalLayout_generateSig.setStretch(0, 6)
        self.horizontalLayout_generateSig.setStretch(1, 8)
        self.Iner_verticalLayout_composer.addLayout(self.horizontalLayout_generateSig)
        self.verticalLayout_sumSignal = QtWidgets.QVBoxLayout()
        self.verticalLayout_sumSignal.setObjectName("verticalLayout_sumSignal")
        self.gridLayout_sumsignal = QtWidgets.QGridLayout()
        self.gridLayout_sumsignal.setObjectName("gridLayout_3")
        self.graphicsView_sumSignal =PlotWidget(self.tab_2)
        self.graphicsView_sumSignal.setObjectName("graphicsView_sumSignal")
        self.gridLayout_sumsignal.addWidget(self.graphicsView_sumSignal, 1, 0, 1, 1)
        self.graphicsView_sumSignal.plotItem.showGrid(x=True, y=True)
        self.horizontalLayout_sumLabel = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sumLabel.setObjectName("horizontalLayout_sumLabel")
        spacerItem_summation = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sumLabel.addItem(spacerItem_summation)
        self.sum_label = QtWidgets.QLabel(self.tab_2)
        self.sum_label.setObjectName("sum_label")
        self.horizontalLayout_sumLabel.addWidget(self.sum_label)
        spacerItem_sum_tab2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_sumLabel.addItem(spacerItem_sum_tab2)
        self.gridLayout_sumsignal.addLayout(self.horizontalLayout_sumLabel, 0, 0, 1, 1)
        self.verticalLayout_sumSignal.addLayout(self.gridLayout_sumsignal)
        self.horizontalLayout_for_delete = QtWidgets.QHBoxLayout()
        self.horizontalLayout_for_delete.setObjectName("horizontalLayout_for_delete")
        self.select_label = QtWidgets.QLabel(self.tab_2)
        self.select_label.setObjectName("select_label")
        self.horizontalLayout_for_delete.addWidget(self.select_label)
        self.signalCombobox = QtWidgets.QComboBox(self.tab_2)
        self.signalCombobox.setObjectName("signalCombobox")
        self.horizontalLayout_for_delete.addWidget(self.signalCombobox)
        self.delete_button = QtWidgets.QPushButton(self.tab_2)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_for_delete.addWidget(self.delete_button)
        self.horizontalLayout_for_delete.setStretch(1, 8)
        self.horizontalLayout_for_delete.setStretch(2, 6)
        self.verticalLayout_sumSignal.addLayout(self.horizontalLayout_for_delete)
        self.verticalLayout_sumSignal.setStretch(0, 8)
        self.Iner_verticalLayout_composer.addLayout(self.verticalLayout_sumSignal)
        self.Iner_verticalLayout_composer.setStretch(0, 5)
        self.Iner_verticalLayout_composer.setStretch(1, 8)
        self.outer_verticalLayout_composer.addLayout(self.Iner_verticalLayout_composer)
        spacerItem6_composer_vertical = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.outer_verticalLayout_composer.addItem(spacerItem6_composer_vertical)
        self.outer_verticalLayout_composer.setStretch(1, 8)
        self.horizontalLayout_composer.addLayout(self.outer_verticalLayout_composer)
        spacerItem_composer_horizontal = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_composer.addItem(spacerItem_composer_horizontal)
        self.horizontalLayout_composer.setStretch(2, 8)
        self.outer_gridLayout_tab2.addLayout(self.horizontalLayout_composer, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_mainwin.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        Open_Icon = QtGui.QIcon()
        Open_Icon.addPixmap(QtGui.QPixmap("open.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(Open_Icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        Save_Icon = QtGui.QIcon()
        Save_Icon.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(Save_Icon)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mag = 0
        self.freq = 0
        self.phase = 0
        self.time_col = []
        self.amp_col = []
        self.status = True
        self.time = []
        self.ttime = []
        self.signallist = []
        self.sumsignal = []
        self.frequency_LineEdit.textChanged.connect(lambda: self.Generate_Signal())
        self.magnitude_LineEdit.textChanged.connect(lambda: self.Generate_Signal())
        self.phaseshift_LineEdit.textChanged.connect(lambda: self.Generate_Signal())
        self.actionSave.triggered.connect(lambda: self.savedata())
        self.add_Button.clicked.connect(lambda: self.sumsignals())
        self.delete_button.clicked.connect(lambda: self.Delete())
        self.actionOpen.triggered.connect(lambda: self.get_file())
        self.sample_horizontalSlider.valueChanged.connect(lambda: self.sampling())
        self.Hide_checkBox.stateChanged.connect(self.hide)
    def hide(self):
        if (self.Hide_checkBox.isChecked()):

            self.graphicsView_RecSignl.hide()

        else:

          self.graphicsView_RecSignl.show()

    def get_Frequency(self):
        if self.frequency_LineEdit.text() != "":
            self.freq = self.frequency_LineEdit.text()
        return float(self.freq)

    def get_Magnitude(self):
        if self.magnitude_LineEdit.text() != "":
            self.mag = self.magnitude_LineEdit.text()
        return float(self.mag)

    def get_Phase_shift(self):
        if self.phaseshift_LineEdit.text() != "":
            self.phase = self.phaseshift_LineEdit.text()
        return float(self.phase)

    def Sig_Name(self):
        self.name = self.nameOfSignal_LineEdit.text()

        return self.name

    def Generate_Signal(self):
        self.graphicsView_genSignal.clear()
        self.graphicsView_genSignal.setBackground('w')
        Freq = self.get_Frequency()
        Amp = self.get_Magnitude()
        theta = self.get_Phase_shift()
        self.time = np.arange(0.0, .999, 0.001)
        self.Signal = Amp * np.sin((2 * np.pi * Freq * self.time) + theta)
        self.graphicsView_genSignal.plot(self.time, self.Signal, pen='red')
        self.ttime.append(self.time)

    def sumsignals(self):
        self.graphicsView_sumSignal.clear()
        self.graphicsView_sumSignal.setBackground('w')
        self.signallist.append(self.Signal)

        self.sumsignal = sum(self.signallist)
        self.graphicsView_sumSignal.plot(self.time, self.sumsignal,pen='blue')
        self.signalCombobox.addItem(self.Sig_Name())

    def Delete(self):
        index = self.signalCombobox.currentIndex()
        if(self.signalCombobox.count()==0):
            del self.signallist[int(index)]
            self.graphicsView_sumSignal.clear()
        else:
            self.signalCombobox.removeItem(index)
            self.graphicsView_sumSignal.clear()
            del self.signallist[int(index)]
            self.sumsignal = sum(self.signallist)
            self.graphicsView_sumSignal.plot(self.time, self.sumsignal, pen='blue')

    def savedata(self):
        with open('SignalDATA.csv', 'w', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(['Time', 'Sum Signals'])
            for index2 in range(len(self.time)):
                self.writer.writerow([self.time[index2], self.sumsignal[index2]])

        ################# sampling ################

    def get_file(self):
        self.graphicsView_main.clear()
        self.graphicsView_main.setBackground('w')
        self.fileName = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
        data_frame = pd.read_csv(self.fileName)
        self.time_col = data_frame.values[:, 0]
        self.amp_col = data_frame.values[:, 1]
        FtAmp = np.fft.fft(self.amp_col)
        FtAmp = FtAmp[0:int(len(self.amp_col) / 2)]
        FtAmp = abs(FtAmp)
        maxpower = max(FtAmp)
        noise = (maxpower / 10)
        self.fmaxtuble = np.where(FtAmp > noise)
        self.maxFreq = max(self.fmaxtuble[0])
        print(self.maxFreq)
        self.graphicsView_main.plot(self.time_col, self.amp_col,pen='blue')

    def changedvalue(self):
        self.min_slider = 0
        self.max_slider = 3 * self.maxFreq
        self.sample_horizontalSlider.setMinimum(self.min_slider)
        self.sample_horizontalSlider.setMaximum(int(self.max_slider))
        self.sampling_factor = self.sample_horizontalSlider.value()
        self.sample_horizontalSlider.setTickInterval(int(1+self.maxFreq))
        return self.sampling_factor

    def sampling(self):
        self.graphicsView_main.clear()
        self.graphicsView_main.setBackground('w')
        self.changedvalue()

        if self.sampling_factor == 0:

            self.graphicsView_main.plot(self.time_col, self.amp_col)

        else:
            self.size = int(len((self.time_col))) - 1
            self.step = int(self.size / self.sample_horizontalSlider.value())
            self.data_sampled_list = [self.amp_col[0]]
            self.time_sampled_list = [self.time_col[0]]
            for index in range(int(self.step), self.size + 1, int(self.step)):
                self.data_sampled_list.append(self.amp_col[index])
                self.time_sampled_list.append(self.time_col[index])
            print(len(self.time_col))
            print(len(self.amp_col))
            self.Data_sampled_nparray = np.array(self.data_sampled_list)
            self.time_sampled_nparray = np.array(self.time_sampled_list)
            print(len(self.Data_sampled_nparray))
            print(len(self.time_sampled_nparray))
            self.graphicsView_main.plot(self.time_col, self.amp_col,pen='blue')
            self.graphicsView_main.plot(self.time_sampled_nparray, self.Data_sampled_nparray, symbol="o")

        self.sinc_interpolation()

    def sinc_interpolation(self):
        self.graphicsView_RecSignl.clear()
        self.graphicsView_RecSignl.setBackground('w')
        if len(self.Data_sampled_nparray) != len(self.time_sampled_nparray):
            raise ValueError('sampled Data and sampled time must be the same length')
        # Find the period
        self.Period = self.time_sampled_nparray[1] - self.time_sampled_nparray[0]
        self.sincMagnitude = np.tile(self.time_col, (len(self.time_sampled_nparray), 1)) - np.tile(
            self.time_sampled_nparray[:, np.newaxis], (1, len(self.time_col)))
        self.reconstruct = np.dot(self.Data_sampled_nparray, np.sinc(self.sincMagnitude / self.Period))
        self.graphicsView_RecSignl.plot(self.time_col, self.reconstruct,pen='red')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sampling-Theory_Illustrator"))
        self.Sampling_Slider.setText(_translate("MainWindow", " 0                                                                                    "
                                                           "Fmax                                                             "
                                                           "2Fmax                                                    "
                                                           "3Fmax"))
        self.Hide_checkBox.setText(_translate("MainWindow", "Press to Hide or Show the Reconstraction graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        self.phase_label.setText(_translate("MainWindow", "phase shift"))
        self.Freq_label.setText(_translate("MainWindow", "frequency"))
        self.name_label.setText(_translate("MainWindow", "Name of Signal"))
        self.mag_Label.setText(_translate("MainWindow", "magnitude"))
        self.add_Button.setText(_translate("MainWindow", "Add Signal"))
        self.generate_sig_label.setText(_translate("MainWindow", "Generated Signal"))
        self.sum_label.setText(_translate("MainWindow", "Summation Signals"))
        self.select_label.setText(_translate("MainWindow", "Select Signal to Delete"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
