# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShengYuan_Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShengYuan_Main(object):
    def setupUi(self, ShengYuan_Main):
        if not ShengYuan_Main.objectName():
            ShengYuan_Main.setObjectName(u"ShengYuan_Main")
        ShengYuan_Main.setWindowModality(Qt.WindowModal)
        ShengYuan_Main.resize(1109, 862)
        ShengYuan_Main.setInputMethodHints(Qt.ImhNone)
        self.tabWidget = QTabWidget(ShengYuan_Main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1091, 851))
        font = QFont()
        font.setFamily(u"Malgun Gothic")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setMovable(True)
        self.tab_Main = QWidget()
        self.tab_Main.setObjectName(u"tab_Main")
        self.tab_Main.setMinimumSize(QSize(1045, 0))
        font1 = QFont()
        font1.setFamily(u"AGA Arabesque Desktop")
        font1.setPointSize(14)
        self.tab_Main.setFont(font1)
        self.verticalLayoutWidget_2 = QWidget(self.tab_Main)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 9, 1071, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamily(u"\u7d30\u660e\u9ad4")
        font2.setPointSize(16)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(156, 156, 156);\n"
"	border-width: 1px;\n"
"	border-style: solid;	\n"
"	margin-top: 0.5ex;\n"
"};\n"
"QGroupBox::title {\n"
"            subcontrol-origin: margin;\n"
"            subcontrol-position: top left;\n"
"            left: 10px;\n"
"            margin-left: 2px;\n"
"            padding: 0  0px;\n"
"        }\n"
"")
        self.groupBox.setFlat(False)
        self.gridFrame = QFrame(self.groupBox)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(19, 29, 1041, 521))
        self.gridFrame.setStyleSheet(u"border-style: none;")
        self.gridLayout_4 = QGridLayout(self.gridFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.gridFrame)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setFamily(u"\u7d30\u660e\u9ad4")
        font3.setPointSize(48)
        self.label_12.setFont(font3)

        self.gridLayout_4.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_10 = QLabel(self.gridFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.gridLayout_4.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_21 = QLabel(self.gridFrame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.gridLayout_4.addWidget(self.label_21, 1, 1, 1, 1)

        self.lbl_Input_Tiler = QLabel(self.gridFrame)
        self.lbl_Input_Tiler.setObjectName(u"lbl_Input_Tiler")
        self.lbl_Input_Tiler.setFont(font3)

        self.gridLayout_4.addWidget(self.lbl_Input_Tiler, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridFrame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_11 = QLabel(self.gridFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayoutWidget_3 = QWidget(self.tab_Main)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 590, 531, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"border-color: rgb(156, 156, 156);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"margin-top: 0.5ex;")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 91, 31))
        font4 = QFont()
        font4.setFamily(u"\u7d30\u660e\u9ad4")
        font4.setPointSize(14)
        self.label_8.setFont(font4)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 70, 91, 31))
        self.label_13.setFont(font4)
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 30, 181, 31))
        self.comboBox_2.setFont(font4)
        self.comboBox_3 = QComboBox(self.groupBox_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(130, 70, 181, 31))
        self.comboBox_3.setFont(font4)
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(410, 30, 75, 31))
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(410, 70, 75, 31))
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(320, 30, 75, 31))
        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(320, 70, 75, 31))

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayoutWidget_11 = QWidget(self.tab_Main)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(549, 589, 531, 211))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.groupBox_7.setStyleSheet(u"border-color: rgb(156, 156, 156);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"margin-top: 0.5ex;")
        self.pushButton_11 = QPushButton(self.groupBox_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(260, 160, 75, 31))
        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 30, 101, 31))
        self.label_15.setFont(font4)
        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 70, 101, 31))
        self.label_14.setFont(font4)
        self.pushButton_12 = QPushButton(self.groupBox_7)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(350, 160, 75, 31))
        self.pushButton_13 = QPushButton(self.groupBox_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(440, 160, 75, 31))
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 110, 101, 31))
        self.label_16.setFont(font4)
        self.lineEdit_6 = QLineEdit(self.groupBox_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(140, 29, 271, 31))
        self.lineEdit_6.setFont(font4)
        self.lineEdit_7 = QLineEdit(self.groupBox_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(140, 70, 271, 31))
        self.lineEdit_7.setFont(font4)
        self.lineEdit_8 = QLineEdit(self.groupBox_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(140, 110, 271, 31))
        self.lineEdit_8.setFont(font4)

        self.verticalLayout_8.addWidget(self.groupBox_7)

        self.tabWidget.addTab(self.tab_Main, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget = QWidget(self.tab_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1081, 801))
        self.verticalLayout_temp = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_temp.setObjectName(u"verticalLayout_temp")
        self.verticalLayout_temp.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1081, 801))
        self.verticalLayout_cnt = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_cnt.setObjectName(u"verticalLayout_cnt")
        self.verticalLayout_cnt.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 710, 1081, 91))
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(156, 156, 156);\n"
"	border-width: 1px;\n"
"	border-style: solid;	\n"
"	margin-top: 0.5ex;\n"
"};\n"
"QGroupBox::title {\n"
"            subcontrol-origin: margin;\n"
"            subcontrol-position: top left;\n"
"            left: 10px;\n"
"            margin-left: 2px;\n"
"            padding: 0  0px;\n"
"        }")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 50, 101, 16))
        self.label_7.setFont(font4)
        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(130, 50, 741, 20))
        self.lineEdit_5.setFont(font4)
        self.pushButton_2 = QPushButton(self.groupBox_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(890, 40, 75, 31))
        self.pushButton_2.setFont(font4)
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(990, 40, 75, 31))
        self.pushButton_3.setFont(font4)
        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 0, 1081, 691))
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(156, 156, 156);\n"
"	border-width: 1px;\n"
"	border-style: solid;	\n"
"	margin-top: 0.5ex;\n"
"};\n"
"QGroupBox::title {\n"
"            subcontrol-origin: margin;\n"
"            subcontrol-position: top left;\n"
"            left: 10px;\n"
"            margin-left: 2px;\n"
"            padding: 0  0px;\n"
"        }")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(19, 39, 1051, 641))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(19, 9, 711, 791))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(156, 156, 156);\n"
"	border-width: 1px;\n"
"	border-style: solid;	\n"
"	margin-top: 0.5ex;\n"
"};\n"
"QGroupBox::title {\n"
"            subcontrol-origin: margin;\n"
"            subcontrol-position: top left;\n"
"            left: 10px;\n"
"            margin-left: 2px;\n"
"            padding: 0  0px;\n"
"        }")
        self.tableWidget = QTableWidget(self.groupBox_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(15, 41, 681, 731))
        self.tableWidget.setFont(font4)
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(740, 10, 331, 269))
        self.groupBox_4.setFont(font2)
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(156, 156, 156);\n"
"	border-width: 1px;\n"
"	border-style: solid;	\n"
"	margin-top: 0.5ex;\n"
"};\n"
"QGroupBox::title {\n"
"            subcontrol-origin: margin;\n"
"            subcontrol-position: top left;\n"
"            left: 10px;\n"
"            margin-left: 2px;\n"
"            padding: 0  0px;\n"
"        }")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 101, 21))
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 91, 21))
        self.label_3.setFont(font4)
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 80, 181, 20))
        self.lineEdit.setFont(font4)
        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 110, 181, 20))
        self.lineEdit_2.setFont(font4)
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 140, 101, 21))
        self.label_4.setFont(font4)
        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 140, 181, 20))
        self.lineEdit_3.setFont(font4)
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 170, 91, 21))
        self.label_5.setFont(font4)
        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(130, 170, 181, 20))
        self.lineEdit_4.setFont(font4)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 50, 101, 21))
        self.label_6.setFont(font4)
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 220, 75, 31))
        self.pushButton.setFont(font4)
        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 50, 181, 22))
        self.comboBox.setFont(font4)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(ShengYuan_Main)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ShengYuan_Main)
    # setupUi

    def retranslateUi(self, ShengYuan_Main):
        ShengYuan_Main.setWindowTitle(QCoreApplication.translate("ShengYuan_Main", u"\u6607\u5143\u9060\u7aef\u6578\u64da\u63a1\u96c6\u7cfb\u7d71", None))
        self.groupBox.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u63a1\u6a23\u72c0\u614b", None))
        self.label_12.setText(QCoreApplication.translate("ShengYuan_Main", u"0.00", None))
        self.label_10.setText(QCoreApplication.translate("ShengYuan_Main", u"0", None))
        self.label_21.setText(QCoreApplication.translate("ShengYuan_Main", u"0", None))
        self.lbl_Input_Tiler.setText(QCoreApplication.translate("ShengYuan_Main", u"0", None))
        self.label_20.setText(QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u6578\u91cf:", None))
        self.label_9.setText(QCoreApplication.translate("ShengYuan_Main", u"\u51fa\u6599\u6578\u91cf:", None))
        self.label_11.setText(QCoreApplication.translate("ShengYuan_Main", u"\u51fa\u576f\u826f\u7387(%):", None))
        self.label.setText(QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u6eab\u5ea6:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u63a1\u6a23\u8a2d\u5b9a", None))
        self.label_8.setText(QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u8a2d\u5099:", None))
        self.label_13.setText(QCoreApplication.translate("ShengYuan_Main", u"\u51fa\u6599\u8a2d\u5099:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u6a5f1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u6a5f2", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("ShengYuan_Main", u"\u51fa\u6599\u6a5f1", None))

        self.pushButton_4.setText(QCoreApplication.translate("ShengYuan_Main", u"\u672a\u9023\u7dda", None))
        self.pushButton_5.setText(QCoreApplication.translate("ShengYuan_Main", u"\u672a\u9023\u7dda", None))
        self.pushButton_6.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8a2d\u5b9a", None))
        self.pushButton_7.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8a2d\u5b9a", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u63a1\u6a23\u6642\u9593", None))
        self.pushButton_11.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8a2d\u5b9a", None))
        self.label_15.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u6642\u9593: ", None))
        self.label_14.setText(QCoreApplication.translate("ShengYuan_Main", u"\u7d50\u675f\u6642\u9593:", None))
        self.pushButton_12.setText(QCoreApplication.translate("ShengYuan_Main", u"\u91cd\u7f6e", None))
        self.pushButton_13.setText(QCoreApplication.translate("ShengYuan_Main", u"\u555f\u52d5\u63a1\u6a23", None))
        self.label_16.setText(QCoreApplication.translate("ShengYuan_Main", u"\u5269\u9918\u6642\u9593:", None))
        self.lineEdit_6.setText(QCoreApplication.translate("ShengYuan_Main", u"2023-01-01 00:00:00", None))
        self.lineEdit_7.setText(QCoreApplication.translate("ShengYuan_Main", u"2023-01-01 23:59:59", None))
        self.lineEdit_8.setText(QCoreApplication.translate("ShengYuan_Main", u"23:59:59", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Main), QCoreApplication.translate("ShengYuan_Main", u"\u5373\u6642\u72c0\u614b\u770b\u677f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ShengYuan_Main", u"\u5373\u6642\u6eab\u5ea6\u66f2\u7dda", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ShengYuan_Main", u"\u5373\u6642\u8a08\u6578\u66f2\u7dda", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u67e5\u8a62\u8a2d\u5b9a", None))
        self.label_7.setText(QCoreApplication.translate("ShengYuan_Main", u"\u6a94\u6848\u8def\u5f91:", None))
        self.lineEdit_5.setText(QCoreApplication.translate("ShengYuan_Main", u"C:\\workspace\\ShengYuanSCADA", None))
        self.pushButton_2.setText(QCoreApplication.translate("ShengYuan_Main", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("ShengYuan_Main", u"\u986f\u793a", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u53d6\u6a23\u5716\u5f62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ShengYuan_Main", u"\u6b77\u53f2\u63a1\u6a23\u66f2\u7dda", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u67e5\u8a62\u7d50\u679c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShengYuan_Main", u"\u53d6\u6a23\u6a5f\u53f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u6642\u9593", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ShengYuan_Main", u"\u505c\u6b62\u6642\u9593", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ShengYuan_Main", u"\u53d6\u6a23\u6578\u91cf", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("ShengYuan_Main", u"\u67e5\u8a62\u8a2d\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u65e5\u671f:", None))
        self.label_3.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u6642\u9593:", None))
        self.lineEdit.setText(QCoreApplication.translate("ShengYuan_Main", u"2023-01-01", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ShengYuan_Main", u"00:00", None))
        self.label_4.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u65e5\u671f:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("ShengYuan_Main", u"2023-01-31", None))
        self.label_5.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u6642\u9593:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("ShengYuan_Main", u"23:59", None))
        self.label_6.setText(QCoreApplication.translate("ShengYuan_Main", u"\u8d77\u59cb\u8a2d\u5099:", None))
        self.pushButton.setText(QCoreApplication.translate("ShengYuan_Main", u"\u67e5\u8a62", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ShengYuan_Main", u"\u5165\u6599\u6a5f", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ShengYuan_Main", u"\u51fa\u6599\u6a5f", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ShengYuan_Main", u"\u6b77\u53f2\u8a08\u6578\u8cc7\u8a0a", None))
    # retranslateUi

