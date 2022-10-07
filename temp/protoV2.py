# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'for_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import subprocess
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIntValidator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideMenu = QtWidgets.QFrame(self.centralwidget)
        self.SideMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideMenu.setObjectName("SideMenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SideMenu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SideMenuCon = QtWidgets.QFrame(self.SideMenu)
        self.SideMenuCon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideMenuCon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideMenuCon.setObjectName("SideMenuCon")
        self.scheduledscan = QtWidgets.QPushButton(self.SideMenuCon)
        self.scheduledscan.setGeometry(QtCore.QRect(10, 70, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scheduledscan.setFont(font)
        self.scheduledscan.setObjectName("scheduledscan")
        self.services = QtWidgets.QPushButton(self.SideMenuCon)
        self.services.setGeometry(QtCore.QRect(10, 110, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.services.setFont(font)
        self.services.setObjectName("services")
        self.portscanner = QtWidgets.QPushButton(self.SideMenuCon)
        self.portscanner.setGeometry(QtCore.QRect(11, 31, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.portscanner.setFont(font)
        self.portscanner.setCheckable(False)
        self.portscanner.setAutoDefault(False)
        self.portscanner.setDefault(False)
        self.portscanner.setObjectName("portscanner")
        self.horizontalLayout_2.addWidget(self.SideMenuCon)
        self.horizontalLayout.addWidget(self.SideMenu)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 561, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.PortScanner = QtWidgets.QWidget()
        self.PortScanner.setObjectName("PortScanner")
        self.frame_4 = QtWidgets.QFrame(self.PortScanner)
        self.frame_4.setGeometry(QtCore.QRect(9, -1, 551, 551))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tab1_3 = QtWidgets.QTabWidget(self.frame_4)
        self.tab1_3.setGeometry(QtCore.QRect(0, 20, 551, 531))
        self.tab1_3.setObjectName("tab1_3")
        self.individualScanTab = QtWidgets.QWidget()
        self.individualScanTab.setObjectName("individualScanTab")
        self.frame_5 = QtWidgets.QFrame(self.individualScanTab)
        self.frame_5.setGeometry(QtCore.QRect(0, 10, 541, 511))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.ind_targetinput = QtWidgets.QLineEdit(self.frame_5)
        self.ind_targetinput.setGeometry(QtCore.QRect(120, 0, 231, 20))
        self.ind_targetinput.setObjectName("ind_targetinput")
        self.Targetlabel = QtWidgets.QLabel(self.frame_5)
        self.Targetlabel.setGeometry(QtCore.QRect(10, 0, 71, 21))
        self.Targetlabel.setObjectName("Targetlabel")
        self.ind_portinput = QtWidgets.QLineEdit(self.frame_5)
        self.ind_portinput.setGeometry(QtCore.QRect(120, 30, 151, 20))
        self.ind_portinput.setObjectName("ind_portinput")
        self.portlabel = QtWidgets.QLabel(self.frame_5)
        self.portlabel.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.portlabel.setObjectName("portlabel")
        self.ind_ScanButton = QtWidgets.QPushButton(self.frame_5)
        self.ind_ScanButton.setGeometry(QtCore.QRect(320, 70, 131, 31))
        self.ind_ScanButton.setObjectName("ind_ScanButton")
        self.tolabel_3 = QtWidgets.QLabel(self.frame_5)
        self.tolabel_3.setGeometry(QtCore.QRect(280, 30, 21, 20))
        self.tolabel_3.setMinimumSize(QtCore.QSize(0, 20))
        self.tolabel_3.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tolabel_3.setFont(font)
        self.tolabel_3.setObjectName("tolabel_3")
        self.Outputlabel = QtWidgets.QLabel(self.frame_5)
        self.Outputlabel.setGeometry(QtCore.QRect(10, 110, 521, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setUnderline(True)
        self.Outputlabel.setFont(font)
        self.Outputlabel.setObjectName("Outputlabel")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(9, 129, 521, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.indScanOpArea = QtWidgets.QTextEdit(self.frame)
        self.indScanOpArea.setGeometry(QtCore.QRect(0, 0, 521, 361))
        self.indScanOpArea.setMinimumSize(QtCore.QSize(521, 351))
        self.indScanOpArea.setObjectName("indScanOpArea")
        self.ind_portinput_2 = QtWidgets.QLineEdit(self.frame_5)
        self.ind_portinput_2.setGeometry(QtCore.QRect(300, 30, 151, 20))
        self.ind_portinput_2.setObjectName("ind_portinput_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.ind_typeOfPortScan = QtWidgets.QComboBox(self.frame_5)
        self.ind_typeOfPortScan.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.ind_typeOfPortScan.setObjectName("ind_typeOfPortScan")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.ind_typeOfPortScan.addItem("")
        self.tab1_3.addTab(self.individualScanTab, "")
        self.FullScanTab = QtWidgets.QWidget()
        self.FullScanTab.setObjectName("FullScanTab")
        self.frame_6 = QtWidgets.QFrame(self.FullScanTab)
        self.frame_6.setGeometry(QtCore.QRect(-1, 9, 541, 501))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.full_targetinput_1 = QtWidgets.QLineEdit(self.frame_6)
        self.full_targetinput_1.setGeometry(QtCore.QRect(120, 0, 131, 20))
        self.full_targetinput_1.setObjectName("full_targetinput_1")
        self.full_outputSA = QtWidgets.QScrollArea(self.frame_6)
        self.full_outputSA.setGeometry(QtCore.QRect(10, 150, 521, 341))
        self.full_outputSA.setWidgetResizable(True)
        self.full_outputSA.setObjectName("full_outputSA")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 519, 339))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.full_outputSA.setWidget(self.scrollAreaWidgetContents_2)
        self.Targetlabel_2 = QtWidgets.QLabel(self.frame_6)
        self.Targetlabel_2.setGeometry(QtCore.QRect(10, 0, 101, 21))
        self.Targetlabel_2.setObjectName("Targetlabel_2")
        self.full_portinput = QtWidgets.QLineEdit(self.frame_6)
        self.full_portinput.setGeometry(QtCore.QRect(120, 30, 131, 20))
        self.full_portinput.setObjectName("full_portinput")
        self.portlabel_2 = QtWidgets.QLabel(self.frame_6)
        self.portlabel_2.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.portlabel_2.setObjectName("portlabel_2")
        self.full_ScanButton = QtWidgets.QPushButton(self.frame_6)
        self.full_ScanButton.setGeometry(QtCore.QRect(310, 60, 111, 31))
        self.full_ScanButton.setObjectName("full_ScanButton")
        self.full_targetinput_2 = QtWidgets.QLineEdit(self.frame_6)
        self.full_targetinput_2.setGeometry(QtCore.QRect(290, 0, 131, 20))
        self.full_targetinput_2.setObjectName("full_targetinput_2")
        self.tolabel = QtWidgets.QLabel(self.frame_6)
        self.tolabel.setGeometry(QtCore.QRect(260, 0, 21, 20))
        self.tolabel.setMinimumSize(QtCore.QSize(0, 20))
        self.tolabel.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tolabel.setFont(font)
        self.tolabel.setObjectName("tolabel")
        self.full_portinput_2 = QtWidgets.QLineEdit(self.frame_6)
        self.full_portinput_2.setGeometry(QtCore.QRect(290, 30, 131, 20))
        self.full_portinput_2.setObjectName("full_portinput_2")
        self.tolabel_2 = QtWidgets.QLabel(self.frame_6)
        self.tolabel_2.setGeometry(QtCore.QRect(260, 30, 21, 20))
        self.tolabel_2.setMinimumSize(QtCore.QSize(0, 20))
        self.tolabel_2.setMaximumSize(QtCore.QSize(21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tolabel_2.setFont(font)
        self.tolabel_2.setObjectName("tolabel_2")
        self.Outputlabel_2 = QtWidgets.QLabel(self.frame_6)
        self.Outputlabel_2.setGeometry(QtCore.QRect(20, 120, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setUnderline(True)
        self.Outputlabel_2.setFont(font)
        self.Outputlabel_2.setObjectName("Outputlabel_2")
        self.full_typeOfPortScan = QtWidgets.QComboBox(self.frame_6)
        self.full_typeOfPortScan.setGeometry(QtCore.QRect(120, 60, 171, 31))
        self.full_typeOfPortScan.setObjectName("full_typeOfPortScan")
        self.full_typeOfPortScan.addItem("")
        self.full_typeOfPortScan.addItem("")
        self.full_typeOfPortScan.addItem("")
        self.full_typeOfPortScan.addItem("")
        self.full_typeOfPortScan.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_9.setObjectName("label_9")
        self.tab1_3.addTab(self.FullScanTab, "")
        self.label_7 = QtWidgets.QLabel(self.PortScanner)
        self.label_7.setGeometry(QtCore.QRect(20, 0, 521, 16))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.PortScanner)
        self.Services = QtWidgets.QWidget()
        self.Services.setObjectName("Services")
        self.frame_3 = QtWidgets.QFrame(self.Services)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 571, 571))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tab1 = QtWidgets.QTabWidget(self.frame_3)
        self.tab1.setGeometry(QtCore.QRect(10, 39, 551, 521))
        self.tab1.setObjectName("tab1")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 551, 511))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.listServicesRefresh = QtWidgets.QPushButton(self.frame_8)
        self.listServicesRefresh.setGeometry(QtCore.QRect(170, 10, 151, 28))
        self.listServicesRefresh.setObjectName("listServicesRefresh")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_8)
        self.tableWidget.setGeometry(QtCore.QRect(5, 50, 531, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tab1.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_9 = QtWidgets.QFrame(self.tab_2)
        self.frame_9.setGeometry(QtCore.QRect(-1, 9, 541, 511))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 40, 521, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.getServicesRefreshBtn = QtWidgets.QPushButton(self.frame_9)
        self.getServicesRefreshBtn.setGeometry(QtCore.QRect(20, 10, 151, 28))
        self.getServicesRefreshBtn.setObjectName("getServicesRefreshBtn")
        self.tab1.addTab(self.tab_2, "")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 531, 16))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.Services)
        self.ScheduledScan = QtWidgets.QWidget()
        self.ScheduledScan.setObjectName("ScheduledScan")
        self.frame_7 = QtWidgets.QFrame(self.ScheduledScan)
        self.frame_7.setGeometry(QtCore.QRect(10, 0, 541, 571))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame_7)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 531, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.label_5.setObjectName("label_5")
        self.SingSchScanBtn = QtWidgets.QPushButton(self.tab_3)
        self.SingSchScanBtn.setGeometry(QtCore.QRect(10, 140, 181, 31))
        self.SingSchScanBtn.setObjectName("SingSchScanBtn")
        self.singSchScanTarget = QtWidgets.QTextEdit(self.tab_3)
        self.singSchScanTarget.setGeometry(QtCore.QRect(150, 20, 361, 31))
        self.singSchScanTarget.setObjectName("singSchScanTarget")
        self.singSchScanTimeIntervalDD = QtWidgets.QComboBox(self.tab_3)
        self.singSchScanTimeIntervalDD.setGeometry(QtCore.QRect(150, 61, 361, 31))
        self.singSchScanTimeIntervalDD.setObjectName("singSchScanTimeIntervalDD")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTimeIntervalDD.addItem("")
        self.singSchScanTypeScanDD = QtWidgets.QComboBox(self.tab_3)
        self.singSchScanTypeScanDD.setGeometry(QtCore.QRect(150, 100, 361, 31))
        self.singSchScanTypeScanDD.setObjectName("singSchScanTypeScanDD")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.singSchScanTypeScanDD.addItem("")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 121, 31))
        self.label_6.setObjectName("label_6")
        self.SingSchScanOp = QtWidgets.QTextEdit(self.tab_3)
        self.SingSchScanOp.setGeometry(QtCore.QRect(0, 186, 531, 311))
        self.SingSchScanOp.setObjectName("SingSchScanOp")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 521, 21))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.ScheduledScan)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tab1_3.setCurrentIndex(0)
        self.tab1.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # my functions 

        self.ind_portinput.setText("0")
        self.ind_portinput_2.setText("65535")
        self.indScanOpArea.setReadOnly(True)


        self.ind_portinput.setValidator(QIntValidator())
        self.ind_portinput_2.setValidator(QIntValidator())
        self.portscanner.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PortScanner))
        self.scheduledscan.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ScheduledScan))
        self.services.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Services))
        self.ind_ScanButton.clicked.connect(self.indPortScan)
        # self.ind_ScanButton.setDisabled(True)
    
        


    def indPortScan(self):
        indPortInp1 = int(self.ind_portinput.text())
        indPortInp2 = int(self.ind_portinput_2.text())
        indtargetIp = self.ind_targetinput.text()
        indTypeScan = self.ind_typeOfPortScan.currentIndex()
        QApplication.processEvents()

        def regularScan(target):
            regScan = subprocess.run(['nmap',target],capture_output=True,text=True)
            return regScan.stdout
        def pingScan(target):
            regScan = subprocess.run(['nmap','-sn',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseScan(target):
            regScan = subprocess.run(['nmap','-T4','-A','-v',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseUDPScan(target,port1,port2):
            regScan = subprocess.run(['nmap','-p',port1+'-'+port2,'-sS','-sU','-T4',target],capture_output=True,text=True)
            return regScan.stdout
        def intenseTCPScan(target,port1,port2):
            regScan = subprocess.run(['nmap','-p',port1+'-'+port2,target],capture_output=True,text=True)
            return regScan.stdout
            
        def displayIndPortOp(string):
            self.indScanOpArea.setText(string)

        if indtargetIp=="" or indPortInp1=="" or indPortInp2=="":
            self.indScanOpArea.setText("Enter All Fields")
        else:
            if indTypeScan == 0:
                indRegPortScanOp = regularScan(indtargetIp)
                displayIndPortOp(indRegPortScanOp)

            elif indTypeScan == 1:
                indPingPortScanOp = pingScan(indtargetIp)
                displayIndPortOp(indRegPortScanOp)

            elif indTypeScan == 2:
                indIntPortScanOp = intenseScan(indtargetIp)
                displayIndPortOp(indIntPortScanOp)

            elif indTypeScan == 3:
                indIntUDPPortScanOp = intenseUDPScan(indtargetIp,indPortInp1,indPortInp2)
                displayIndPortOp(indIntUDPPortScanOp)

            elif indTypeScan == 4:
                indIntTCPPortScanOp = intenseTCPScan(indtargetIp,indPortInp1,indPortInp2)
                displayIndPortOp(indIntTCPPortScanOp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scheduledscan.setText(_translate("MainWindow", "SCHEDULED SCAN"))
        self.services.setText(_translate("MainWindow", "SERVICES"))
        self.portscanner.setText(_translate("MainWindow", "PORT SCANNER"))
        self.individualScanTab.setToolTip(_translate("MainWindow", "<html><head/><body><p>axca</p><p><br/></p></body></html>"))
        self.Targetlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Target :</span></p></body></html>"))
        self.portlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Port Range :</span></p></body></html>"))
        self.ind_ScanButton.setText(_translate("MainWindow", "Scan"))
        self.tolabel_3.setText(_translate("MainWindow", "to"))
        self.Outputlabel.setText(_translate("MainWindow", "<html><head/><body><p>OUTPUT</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Type of Scan :</span></p></body></html>"))
        self.ind_typeOfPortScan.setItemText(0, _translate("MainWindow", "Regular Scan"))
        self.ind_typeOfPortScan.setItemText(1, _translate("MainWindow", "Ping Scan"))
        self.ind_typeOfPortScan.setItemText(2, _translate("MainWindow", "Intensive Scan"))
        self.ind_typeOfPortScan.setItemText(3, _translate("MainWindow", "Intensive | UDP Scan"))
        self.ind_typeOfPortScan.setItemText(4, _translate("MainWindow", "Intensive | TCP Scan"))
        self.tab1_3.setTabText(self.tab1_3.indexOf(self.individualScanTab), _translate("MainWindow", "Individual Target"))
        self.Targetlabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Range of Ip :</span></p></body></html>"))
        self.portlabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Port Range :</span></p></body></html>"))
        self.full_ScanButton.setText(_translate("MainWindow", "Full Scan"))
        self.tolabel.setText(_translate("MainWindow", "to"))
        self.tolabel_2.setText(_translate("MainWindow", "to"))
        self.Outputlabel_2.setText(_translate("MainWindow", "OUTPUT"))
        self.full_typeOfPortScan.setItemText(0, _translate("MainWindow", "Regular Scan"))
        self.full_typeOfPortScan.setItemText(1, _translate("MainWindow", "Ping Scan"))
        self.full_typeOfPortScan.setItemText(2, _translate("MainWindow", "Intensive Scan"))
        self.full_typeOfPortScan.setItemText(3, _translate("MainWindow", "Intensive | UDP Scan"))
        self.full_typeOfPortScan.setItemText(4, _translate("MainWindow", "Intensive | TCP Scan"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Type of Scan :</span></p></body></html>"))
        self.tab1_3.setTabText(self.tab1_3.indexOf(self.FullScanTab), _translate("MainWindow", "Full Network "))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Port Scan :</span></p></body></html>"))
        self.listServicesRefresh.setText(_translate("MainWindow", "List Services"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Allowed Services : </span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.tab1.setTabText(self.tab1.indexOf(self.tab), _translate("MainWindow", "List Services"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kill"))
        self.getServicesRefreshBtn.setText(_translate("MainWindow", "Refresh"))
        self.tab1.setTabText(self.tab1.indexOf(self.tab_2), _translate("MainWindow", "Edit Services"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Services :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Target :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Time Interval :</span></p></body></html>"))
        self.SingSchScanBtn.setText(_translate("MainWindow", "Schedule"))
        self.singSchScanTimeIntervalDD.setItemText(0, _translate("MainWindow", "1 minutes"))
        self.singSchScanTimeIntervalDD.setItemText(1, _translate("MainWindow", "60 minutes"))
        self.singSchScanTimeIntervalDD.setItemText(2, _translate("MainWindow", "24 hours"))
        self.singSchScanTypeScanDD.setItemText(0, _translate("MainWindow", "Ping Scan"))
        self.singSchScanTypeScanDD.setItemText(1, _translate("MainWindow", "Quick Scan"))
        self.singSchScanTypeScanDD.setItemText(2, _translate("MainWindow", "Quick Scan ++"))
        self.singSchScanTypeScanDD.setItemText(3, _translate("MainWindow", "Regular Scan"))
        self.singSchScanTypeScanDD.setItemText(4, _translate("MainWindow", "Intensive Scan"))
        self.singSchScanTypeScanDD.setItemText(5, _translate("MainWindow", "Intensive Scan + UDP"))
        self.singSchScanTypeScanDD.setItemText(6, _translate("MainWindow", "Intensive Scan | All TCP Ports"))
        self.singSchScanTypeScanDD.setItemText(7, _translate("MainWindow", "Intensive Safe Scan(No Ping)"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Type Of Scan :</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Single Machine"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Full Network"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Schedule Scan :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
