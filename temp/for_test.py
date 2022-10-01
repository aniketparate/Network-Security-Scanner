# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledHsENfL.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SideMenu = QFrame(self.centralwidget)
        self.SideMenu.setObjectName(u"SideMenu")
        self.SideMenu.setMaximumSize(QSize(200, 16777215))
        self.SideMenu.setFrameShape(QFrame.StyledPanel)
        self.SideMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.SideMenu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SideMenuCon = QFrame(self.SideMenu)
        self.SideMenuCon.setObjectName(u"SideMenuCon")
        self.SideMenuCon.setFrameShape(QFrame.StyledPanel)
        self.SideMenuCon.setFrameShadow(QFrame.Raised)
        self.portscanner = QPushButton(self.SideMenuCon)
        self.portscanner.setObjectName(u"portscanner")
        self.portscanner.setGeometry(QRect(30, 50, 131, 41))
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.portscanner.setFont(font)
        self.portscanner.setCheckable(False)
        self.portscanner.setAutoDefault(False)
        self.scheduledscan = QPushButton(self.SideMenuCon)
        self.scheduledscan.setObjectName(u"scheduledscan")
        self.scheduledscan.setGeometry(QRect(30, 110, 131, 41))
        self.scheduledscan.setFont(font)
        self.services = QPushButton(self.SideMenuCon)
        self.services.setObjectName(u"services")
        self.services.setGeometry(QRect(30, 170, 131, 41))
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(10)
        self.services.setFont(font1)

        self.horizontalLayout_2.addWidget(self.SideMenuCon)


        self.horizontalLayout.addWidget(self.SideMenu)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 51, 16))
        self.range = QCheckBox(self.frame_2)
        self.range.setObjectName(u"range")
        self.range.setGeometry(QRect(30, 80, 70, 16))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 80, 16, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.scan = QPushButton(self.frame_2)
        self.scan.setObjectName(u"scan")
        self.scan.setGeometry(QRect(220, 140, 75, 23))
        self.targetIP = QLineEdit(self.frame_2)
        self.targetIP.setObjectName(u"targetIP")
        self.targetIP.setGeometry(QRect(100, 40, 121, 21))
        self.rangeStart = QLineEdit(self.frame_2)
        self.rangeStart.setObjectName(u"rangeStart")
        self.rangeStart.setGeometry(QRect(100, 80, 121, 21))
        self.rangeEnd = QLineEdit(self.frame_2)
        self.rangeEnd.setObjectName(u"rangeEnd")
        self.rangeEnd.setGeometry(QRect(280, 80, 121, 21))
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 200, 531, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 529, 359))
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 61, 16))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(10)
        font3.setUnderline(True)
        self.label_3.setFont(font3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.portscanner.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.portscanner.setText(QCoreApplication.translate("MainWindow", u"PORT SCANNER", None))
        self.scheduledscan.setText(QCoreApplication.translate("MainWindow", u"SCHEDULED SCAN", None))
        self.services.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Target IP :", None))
        self.range.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.scan.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
    # retranslateUi

