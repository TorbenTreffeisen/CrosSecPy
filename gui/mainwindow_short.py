# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arktos_analysis_v1\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 439)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(19, 19, 1001, 351))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stacked1 = QtWidgets.QWidget()
        self.stacked1.setObjectName("stacked1")
        self.input_model1 = QtWidgets.QLineEdit(self.stacked1)
        self.input_model1.setGeometry(QtCore.QRect(20, 10, 300, 30))
        self.input_model1.setObjectName("input_model1")
        self.input_model2 = QtWidgets.QLineEdit(self.stacked1)
        self.input_model2.setGeometry(QtCore.QRect(20, 60, 300, 30))
        self.input_model2.setObjectName("input_model2")
        self.pb_models = QtWidgets.QPushButton(self.stacked1)
        self.pb_models.setGeometry(QtCore.QRect(710, 120, 100, 30))
        self.pb_models.setObjectName("pb_models")
        self.input_folder_m1 = QtWidgets.QLineEdit(self.stacked1)
        self.input_folder_m1.setGeometry(QtCore.QRect(510, 10, 300, 30))
        self.input_folder_m1.setObjectName("input_folder_m1")
        self.checkbox_folder_m1 = QtWidgets.QCheckBox(self.stacked1)
        self.checkbox_folder_m1.setGeometry(QtCore.QRect(380, 10, 120, 30))
        self.checkbox_folder_m1.setObjectName("checkbox_folder_m1")
        self.checkbox_folder_m2 = QtWidgets.QCheckBox(self.stacked1)
        self.checkbox_folder_m2.setGeometry(QtCore.QRect(380, 60, 120, 30))
        self.checkbox_folder_m2.setObjectName("checkbox_folder_m2")
        self.input_folder_m2 = QtWidgets.QLineEdit(self.stacked1)
        self.input_folder_m2.setGeometry(QtCore.QRect(510, 60, 300, 30))
        self.input_folder_m2.setObjectName("input_folder_m2")
        self.pb_selection = QtWidgets.QPushButton(self.stacked1)
        self.pb_selection.setGeometry(QtCore.QRect(510, 120, 180, 30))
        self.pb_selection.setObjectName("pb_selection")
        self.stackedWidget.addWidget(self.stacked1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.cbx_inp_model_m1 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_model_m1.setGeometry(QtCore.QRect(350, 10, 200, 30))
        self.cbx_inp_model_m1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_model_m1.setObjectName("cbx_inp_model_m1")
        self.cbx_inp_model_m2 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_model_m2.setGeometry(QtCore.QRect(350, 60, 200, 30))
        self.cbx_inp_model_m2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_model_m2.setObjectName("cbx_inp_model_m2")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cbx_inp_loadstep_m2 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_loadstep_m2.setGeometry(QtCore.QRect(570, 60, 200, 30))
        self.cbx_inp_loadstep_m2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_loadstep_m2.setObjectName("cbx_inp_loadstep_m2")
        self.cbx_inp_loadstep_m2.addItem("")
        self.cbx_inp_loadstep_m2.addItem("")
        self.cbx_inp_depth_m1 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_depth_m1.setGeometry(QtCore.QRect(130, 10, 200, 30))
        self.cbx_inp_depth_m1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_depth_m1.setObjectName("cbx_inp_depth_m1")
        self.cbx_inp_depth_m1.addItem("")
        self.cbx_inp_depth_m1.addItem("")
        self.cbx_inp_loadstep_m1 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_loadstep_m1.setGeometry(QtCore.QRect(570, 10, 200, 30))
        self.cbx_inp_loadstep_m1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_loadstep_m1.setObjectName("cbx_inp_loadstep_m1")
        self.cbx_inp_loadstep_m1.addItem("")
        self.cbx_inp_loadstep_m1.addItem("")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pb_filepath_selec = QtWidgets.QPushButton(self.page_3)
        self.pb_filepath_selec.setGeometry(QtCore.QRect(470, 120, 180, 30))
        self.pb_filepath_selec.setObjectName("pb_filepath_selec")
        self.pb_models_2 = QtWidgets.QPushButton(self.page_3)
        self.pb_models_2.setGeometry(QtCore.QRect(670, 120, 100, 30))
        self.pb_models_2.setObjectName("pb_models_2")
        self.cbx_inp_depth_m2 = QtWidgets.QComboBox(self.page_3)
        self.cbx_inp_depth_m2.setGeometry(QtCore.QRect(130, 60, 200, 30))
        self.cbx_inp_depth_m2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_inp_depth_m2.setObjectName("cbx_inp_depth_m2")
        self.cbx_inp_depth_m2.addItem("")
        self.cbx_inp_depth_m2.addItem("")
        self.stackedWidget.addWidget(self.page_3)
        self.stacked2 = QtWidgets.QWidget()
        self.stacked2.setObjectName("stacked2")
        self.cbx_mod1 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_mod1.setGeometry(QtCore.QRect(30, 10, 200, 30))
        self.cbx_mod1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbx_mod1.setObjectName("cbx_mod1")
        self.cbx_cat_c1 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_cat_c1.setGeometry(QtCore.QRect(30, 100, 200, 30))
        self.cbx_cat_c1.setObjectName("cbx_cat_c1")
        self.cbx_cat_c1.addItem("")
        self.cbx_cat_c1.addItem("")
        self.cbx_cat_c1.addItem("")
        self.cbx_cat_c1.addItem("")
        self.cbx_cat_c1.addItem("")
        self.cbx_cat_c2 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_cat_c2.setGeometry(QtCore.QRect(270, 100, 200, 30))
        self.cbx_cat_c2.setObjectName("cbx_cat_c2")
        self.cbx_cat_c2.addItem("")
        self.cbx_cat_c2.addItem("")
        self.cbx_cat_c2.addItem("")
        self.cbx_cat_c2.addItem("")
        self.cbx_cat_c2.addItem("")
        self.cbx_cat_c3 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_cat_c3.setGeometry(QtCore.QRect(510, 100, 200, 30))
        self.cbx_cat_c3.setObjectName("cbx_cat_c3")
        self.cbx_cat_c3.addItem("")
        self.cbx_cat_c3.addItem("")
        self.cbx_cat_c3.addItem("")
        self.cbx_cat_c3.addItem("")
        self.cbx_cat_c3.addItem("")
        self.cbx_cat_c4 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_cat_c4.setGeometry(QtCore.QRect(750, 100, 200, 30))
        self.cbx_cat_c4.setObjectName("cbx_cat_c4")
        self.cbx_cat_c4.addItem("")
        self.cbx_cat_c4.addItem("")
        self.cbx_cat_c4.addItem("")
        self.cbx_cat_c4.addItem("")
        self.cbx_cat_c4.addItem("")
        self.cbx_scat_c1 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_scat_c1.setGeometry(QtCore.QRect(30, 150, 200, 30))
        self.cbx_scat_c1.setObjectName("cbx_scat_c1")
        self.cbx_scat_c2 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_scat_c2.setGeometry(QtCore.QRect(270, 150, 200, 30))
        self.cbx_scat_c2.setObjectName("cbx_scat_c2")
        self.cbx_scat_c3 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_scat_c3.setGeometry(QtCore.QRect(510, 150, 200, 30))
        self.cbx_scat_c3.setObjectName("cbx_scat_c3")
        self.cbx_scat_c4 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_scat_c4.setGeometry(QtCore.QRect(750, 150, 200, 30))
        self.cbx_scat_c4.setObjectName("cbx_scat_c4")
        self.cbx_mod2 = QtWidgets.QComboBox(self.stacked2)
        self.cbx_mod2.setGeometry(QtCore.QRect(270, 10, 200, 30))
        self.cbx_mod2.setObjectName("cbx_mod2")
        self.line = QtWidgets.QFrame(self.stacked2)
        self.line.setGeometry(QtCore.QRect(10, 240, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.stacked2)
        self.line_2.setGeometry(QtCore.QRect(10, 70, 961, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.stacked2)
        self.line_3.setGeometry(QtCore.QRect(240, 80, 20, 170))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.stacked2)
        self.line_4.setGeometry(QtCore.QRect(480, 80, 20, 170))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.stacked2)
        self.line_5.setGeometry(QtCore.QRect(720, 80, 20, 170))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.cshades_c4 = QtWidgets.QSpinBox(self.stacked2)
        self.cshades_c4.setGeometry(QtCore.QRect(880, 200, 50, 30))
        self.cshades_c4.setMaximum(40)
        self.cshades_c4.setObjectName("cshades_c4")
        self.cbx_legend = QtWidgets.QComboBox(self.stacked2)
        self.cbx_legend.setGeometry(QtCore.QRect(110, 290, 120, 30))
        self.cbx_legend.setObjectName("cbx_legend")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.cbx_legend.addItem("")
        self.resolution = QtWidgets.QSpinBox(self.stacked2)
        self.resolution.setGeometry(QtCore.QRect(400, 290, 50, 30))
        self.resolution.setMinimum(100)
        self.resolution.setMaximum(10000)
        self.resolution.setObjectName("resolution")
        self.label = QtWidgets.QLabel(self.stacked2)
        self.label.setGeometry(QtCore.QRect(40, 290, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_plot = QtWidgets.QPushButton(self.stacked2)
        self.pb_plot.setGeometry(QtCore.QRect(750, 270, 200, 30))
        self.pb_plot.setObjectName("pb_plot")
        self.label_2 = QtWidgets.QLabel(self.stacked2)
        self.label_2.setGeometry(QtCore.QRect(290, 290, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.stacked2)
        self.label_3.setGeometry(QtCore.QRect(770, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cshades_c1 = QtWidgets.QSpinBox(self.stacked2)
        self.cshades_c1.setGeometry(QtCore.QRect(160, 200, 50, 30))
        self.cshades_c1.setMaximum(40)
        self.cshades_c1.setObjectName("cshades_c1")
        self.label_7 = QtWidgets.QLabel(self.stacked2)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cshades_c2 = QtWidgets.QSpinBox(self.stacked2)
        self.cshades_c2.setGeometry(QtCore.QRect(400, 200, 50, 30))
        self.cshades_c2.setMaximum(40)
        self.cshades_c2.setObjectName("cshades_c2")
        self.label_8 = QtWidgets.QLabel(self.stacked2)
        self.label_8.setGeometry(QtCore.QRect(290, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cshades_c3 = QtWidgets.QSpinBox(self.stacked2)
        self.cshades_c3.setGeometry(QtCore.QRect(640, 200, 50, 30))
        self.cshades_c3.setMaximum(40)
        self.cshades_c3.setObjectName("cshades_c3")
        self.label_9 = QtWidgets.QLabel(self.stacked2)
        self.label_9.setGeometry(QtCore.QRect(530, 200, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pb_select = QtWidgets.QPushButton(self.stacked2)
        self.pb_select.setGeometry(QtCore.QRect(510, 10, 200, 30))
        self.pb_select.setObjectName("pb_select")
        self.widget = QtWidgets.QWidget(self.stacked2)
        self.widget.setGeometry(QtCore.QRect(560, 270, 161, 61))
        self.widget.setObjectName("widget")
        self.radb_freesel = QtWidgets.QRadioButton(self.widget)
        self.radb_freesel.setEnabled(False)
        self.radb_freesel.setGeometry(QtCore.QRect(10, 10, 111, 17))
        self.radb_freesel.setObjectName("radb_freesel")
        self.radb_predsel = QtWidgets.QRadioButton(self.widget)
        self.radb_predsel.setEnabled(False)
        self.radb_predsel.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.radb_predsel.setObjectName("radb_predsel")
        self.pb_select_2 = QtWidgets.QPushButton(self.stacked2)
        self.pb_select_2.setGeometry(QtCore.QRect(750, 10, 200, 30))
        self.pb_select_2.setObjectName("pb_select_2")
        self.pb_plot_diff = QtWidgets.QPushButton(self.stacked2)
        self.pb_plot_diff.setGeometry(QtCore.QRect(750, 320, 200, 30))
        self.pb_plot_diff.setObjectName("pb_plot_diff")
        self.stackedWidget.addWidget(self.stacked2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_model1.setText(_translate("MainWindow", "model1"))
        self.input_model2.setText(_translate("MainWindow", "model2"))
        self.pb_models.setText(_translate("MainWindow", "layout"))
        self.input_folder_m1.setText(_translate("MainWindow", "Input Folder"))
        self.checkbox_folder_m1.setText(_translate("MainWindow", "change folderpath"))
        self.checkbox_folder_m2.setText(_translate("MainWindow", "change folderpath"))
        self.input_folder_m2.setText(_translate("MainWindow", "Input Folder"))
        self.pb_selection.setText(_translate("MainWindow", "go to predefined selection"))
        self.label_5.setText(_translate("MainWindow", "Model 2"))
        self.cbx_inp_loadstep_m2.setItemText(0, _translate("MainWindow", "l1"))
        self.cbx_inp_loadstep_m2.setItemText(1, _translate("MainWindow", "last"))
        self.cbx_inp_depth_m1.setItemText(0, _translate("MainWindow", "Mod1"))
        self.cbx_inp_depth_m1.setItemText(1, _translate("MainWindow", "Mod2"))
        self.cbx_inp_loadstep_m1.setItemText(0, _translate("MainWindow", "l1"))
        self.cbx_inp_loadstep_m1.setItemText(1, _translate("MainWindow", "last"))
        self.label_4.setText(_translate("MainWindow", "Model 1"))
        self.pb_filepath_selec.setText(_translate("MainWindow", "go to filepath selection"))
        self.pb_models_2.setText(_translate("MainWindow", "layout"))
        self.cbx_inp_depth_m2.setItemText(0, _translate("MainWindow", "Mod1"))
        self.cbx_inp_depth_m2.setItemText(1, _translate("MainWindow", "Mod2"))
        self.cbx_cat_c1.setItemText(0, _translate("MainWindow", "pressure"))
        self.cbx_cat_c1.setItemText(1, _translate("MainWindow", "stress"))
        self.cbx_cat_c1.setItemText(2, _translate("MainWindow", "el. strain"))
        self.cbx_cat_c1.setItemText(3, _translate("MainWindow", "pl. strain"))
        self.cbx_cat_c1.setItemText(4, _translate("MainWindow", "tot. strain"))
        self.cbx_cat_c2.setItemText(0, _translate("MainWindow", "pressure"))
        self.cbx_cat_c2.setItemText(1, _translate("MainWindow", "stress"))
        self.cbx_cat_c2.setItemText(2, _translate("MainWindow", "el. strain"))
        self.cbx_cat_c2.setItemText(3, _translate("MainWindow", "pl. strain"))
        self.cbx_cat_c2.setItemText(4, _translate("MainWindow", "tot. strain"))
        self.cbx_cat_c3.setItemText(0, _translate("MainWindow", "pressure"))
        self.cbx_cat_c3.setItemText(1, _translate("MainWindow", "stress"))
        self.cbx_cat_c3.setItemText(2, _translate("MainWindow", "el. strain"))
        self.cbx_cat_c3.setItemText(3, _translate("MainWindow", "pl. strain"))
        self.cbx_cat_c3.setItemText(4, _translate("MainWindow", "tot. strain"))
        self.cbx_cat_c4.setItemText(0, _translate("MainWindow", "pressure"))
        self.cbx_cat_c4.setItemText(1, _translate("MainWindow", "stress"))
        self.cbx_cat_c4.setItemText(2, _translate("MainWindow", "el. strain"))
        self.cbx_cat_c4.setItemText(3, _translate("MainWindow", "pl. strain"))
        self.cbx_cat_c4.setItemText(4, _translate("MainWindow", "tot. strain"))
        self.cbx_legend.setItemText(0, _translate("MainWindow", "RdYlBu"))
        self.cbx_legend.setItemText(1, _translate("MainWindow", "RdBu"))
        self.cbx_legend.setItemText(2, _translate("MainWindow", "RdYlGn"))
        self.cbx_legend.setItemText(3, _translate("MainWindow", "YlOrRd"))
        self.cbx_legend.setItemText(4, _translate("MainWindow", "Spectral"))
        self.cbx_legend.setItemText(5, _translate("MainWindow", "coolwarm"))
        self.cbx_legend.setItemText(6, _translate("MainWindow", "bwr"))
        self.cbx_legend.setItemText(7, _translate("MainWindow", "seismic"))
        self.cbx_legend.setItemText(8, _translate("MainWindow", "jet"))
        self.cbx_legend.setItemText(9, _translate("MainWindow", "Greys"))
        self.label.setText(_translate("MainWindow", "Legend"))
        self.pb_plot.setText(_translate("MainWindow", "plot"))
        self.label_2.setText(_translate("MainWindow", "Resolution"))
        self.label_3.setText(_translate("MainWindow", "Colorshades"))
        self.label_7.setText(_translate("MainWindow", "Colorshades"))
        self.label_8.setText(_translate("MainWindow", "Colorshades"))
        self.label_9.setText(_translate("MainWindow", "Colorshades"))
        self.pb_select.setText(_translate("MainWindow", "select new models"))
        self.radb_freesel.setText(_translate("MainWindow", "free selection"))
        self.radb_predsel.setText(_translate("MainWindow", "predifined selection"))
        self.pb_select_2.setText(_translate("MainWindow", "select predefined models"))
        self.pb_plot_diff.setText(_translate("MainWindow", "differences"))

