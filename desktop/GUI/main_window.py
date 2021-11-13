# Form implementation generated from reading ui file '.\GUI\design_files\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 276)
        MainWindow.setMinimumSize(QtCore.QSize(0, 276))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 276))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_table = QtWidgets.QTableWidget(self.centralwidget)
        self.data_table.setMinimumSize(QtCore.QSize(283, 115))
        self.data_table.setMaximumSize(QtCore.QSize(283, 115))
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(2)
        self.data_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.data_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.data_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.data_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.data_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.data_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(207, 207, 207))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
        self.data_table.setItem(2, 1, item)
        self.horizontalLayout.addWidget(self.data_table)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.height_panel = QtWidgets.QLCDNumber(self.centralwidget)
        self.height_panel.setMaximumSize(QtCore.QSize(16777215, 65))
        self.height_panel.setObjectName("height_panel")
        self.verticalLayout.addWidget(self.height_panel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pressure_on = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pressure_on.setFont(font)
        self.pressure_on.setChecked(False)
        self.pressure_on.setObjectName("pressure_on")
        self.pressure_group = QtWidgets.QButtonGroup(MainWindow)
        self.pressure_group.setObjectName("pressure_group")
        self.pressure_group.addButton(self.pressure_on)
        self.horizontalLayout_4.addWidget(self.pressure_on)
        self.pressure_off = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pressure_off.setFont(font)
        self.pressure_off.setChecked(True)
        self.pressure_off.setObjectName("pressure_off")
        self.pressure_group.addButton(self.pressure_off)
        self.horizontalLayout_4.addWidget(self.pressure_off)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cooler_on = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.cooler_on.setFont(font)
        self.cooler_on.setChecked(False)
        self.cooler_on.setObjectName("cooler_on")
        self.cooler_group = QtWidgets.QButtonGroup(MainWindow)
        self.cooler_group.setObjectName("cooler_group")
        self.cooler_group.addButton(self.cooler_on)
        self.horizontalLayout_2.addWidget(self.cooler_on)
        self.cooler_off = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.cooler_off.setFont(font)
        self.cooler_off.setChecked(True)
        self.cooler_off.setObjectName("cooler_off")
        self.cooler_group.addButton(self.cooler_off)
        self.horizontalLayout_2.addWidget(self.cooler_off)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.light_on = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.light_on.setFont(font)
        self.light_on.setChecked(False)
        self.light_on.setObjectName("light_on")
        self.light_group = QtWidgets.QButtonGroup(MainWindow)
        self.light_group.setObjectName("light_group")
        self.light_group.addButton(self.light_on)
        self.horizontalLayout_3.addWidget(self.light_on)
        self.light_off = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.light_off.setFont(font)
        self.light_off.setChecked(True)
        self.light_off.setObjectName("light_off")
        self.light_group.addButton(self.light_off)
        self.horizontalLayout_3.addWidget(self.light_off)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.cooler_group.buttonClicked['QAbstractButton*'].connect(MainWindow.cooler_state_slot) # type: ignore
        self.pressure_group.buttonClicked['QAbstractButton*'].connect(MainWindow.pressure_state_slot) # type: ignore
        self.light_group.buttonClicked['QAbstractButton*'].connect(MainWindow.light_state_slot) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Control Panel"))
        item = self.data_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.data_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.data_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BME280 (out)"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MS5611 (in)"))
        __sortingEnabled = self.data_table.isSortingEnabled()
        self.data_table.setSortingEnabled(False)
        item = self.data_table.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.data_table.item(0, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.data_table.item(1, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.data_table.item(1, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.data_table.item(2, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.data_table.item(2, 1)
        item.setText(_translate("MainWindow", "X"))
        self.data_table.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Current height"))
        self.label_4.setText(_translate("MainWindow", "Pressure"))
        self.pressure_on.setText(_translate("MainWindow", "On"))
        self.pressure_off.setText(_translate("MainWindow", "Off"))
        self.label_2.setText(_translate("MainWindow", "Cooler"))
        self.cooler_on.setText(_translate("MainWindow", "On"))
        self.cooler_off.setText(_translate("MainWindow", "Off"))
        self.label_3.setText(_translate("MainWindow", "Light"))
        self.light_on.setText(_translate("MainWindow", "On"))
        self.light_off.setText(_translate("MainWindow", "Off"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
