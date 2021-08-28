# Form implementation generated from reading ui file 'desktop\GUI\design_files\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1077, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1077, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1051, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.i2c_devices = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.i2c_devices.setWidgetResizable(True)
        self.i2c_devices.setObjectName("i2c_devices")
        self.i2c_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.i2c_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 254, 133))
        self.i2c_scrollAreaWidgetContents.setObjectName("i2c_scrollAreaWidgetContents")
        self.i2c_devices.setWidget(self.i2c_scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.i2c_devices)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.spi_devices = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.spi_devices.setWidgetResizable(True)
        self.spi_devices.setObjectName("spi_devices")
        self.spi_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.spi_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 254, 133))
        self.spi_scrollAreaWidgetContents.setObjectName("spi_scrollAreaWidgetContents")
        self.spi_devices.setWidget(self.spi_scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.spi_devices)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.web_cameras = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.web_cameras.setWidgetResizable(True)
        self.web_cameras.setObjectName("web_cameras")
        self.web_cameras_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.web_cameras_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 253, 133))
        self.web_cameras_scrollAreaWidgetContents.setObjectName("web_cameras_scrollAreaWidgetContents")
        self.web_cameras.setWidget(self.web_cameras_scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.web_cameras)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gpio = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.gpio.setWidgetResizable(True)
        self.gpio.setObjectName("gpio")
        self.gpio_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gpio_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 254, 133))
        self.gpio_scrollAreaWidgetContents.setObjectName("gpio_scrollAreaWidgetContents")
        self.gpio.setWidget(self.gpio_scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.gpio)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionI2C_device = QtGui.QAction(MainWindow)
        self.actionI2C_device.setObjectName("actionI2C_device")
        self.actionSPI_device = QtGui.QAction(MainWindow)
        self.actionSPI_device.setObjectName("actionSPI_device")
        self.actionWeb_Camera = QtGui.QAction(MainWindow)
        self.actionWeb_Camera.setObjectName("actionWeb_Camera")
        self.actionGPIO_controller = QtGui.QAction(MainWindow)
        self.actionGPIO_controller.setObjectName("actionGPIO_controller")
        self.actionUpdate_I2C_devices_list = QtGui.QAction(MainWindow)
        self.actionUpdate_I2C_devices_list.setObjectName("actionUpdate_I2C_devices_list")
        self.menuAdd.addAction(self.actionI2C_device)
        self.menuAdd.addAction(self.actionSPI_device)
        self.menuAdd.addAction(self.actionWeb_Camera)
        self.menuAdd.addAction(self.actionGPIO_controller)
        self.menuTools.addAction(self.actionUpdate_I2C_devices_list)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Chamber"))
        self.label.setText(_translate("MainWindow", "I2C"))
        self.label_2.setText(_translate("MainWindow", "SPI"))
        self.label_3.setText(_translate("MainWindow", "Web-Cameras"))
        self.label_4.setText(_translate("MainWindow", "GPIO"))
        self.menuAdd.setTitle(_translate("MainWindow", "New"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionI2C_device.setText(_translate("MainWindow", "I2C device"))
        self.actionSPI_device.setText(_translate("MainWindow", "SPI device"))
        self.actionWeb_Camera.setText(_translate("MainWindow", "Web-Camera"))
        self.actionGPIO_controller.setText(_translate("MainWindow", "GPIO controller"))
        self.actionUpdate_I2C_devices_list.setText(_translate("MainWindow", "Update I2C devices list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
