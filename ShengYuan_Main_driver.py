#!/usr/bin/python
# -*- coding: utf-8 -*-

from ShengYuan_Main import *
import sys
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter,QColor,QCloseEvent
from PySide2.QtCore import QTimer,QDateTime
import numpy as np
from multiprocessing import Manager,Process,Queue
from threading import Thread

class TagData:
    # Data struct.
    data = list()

    # Initial signleTon object.
    _instance = None 
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
        return cls._instance  
    # Initial object.
    def __init__(self): pass


class ShengYuan_Main(QMainWindow, Ui_ShengYuan_Main):
    
    def __init__(self):
        super(ShengYuan_Main, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1109, 862)
        self.chart_cnt()
        self.chart_temp()
        self.yvalueList = []
        # self.pushButton_startTagServer.clicked.connect(self.start_smarttag_server, Qt.UniqueConnection)


    def chart_cnt(self): # 繪製Real-time chart
        ''' '''
        # 初始化ACC X數據
        self.serial_input_cnt = QtCharts.QSplineSeries()
        self.serial_input_cnt.setName("入料計數")
        self.serial_input_cnt.setColor(QColor("blue"))

        self.serial_output_cnt = QtCharts.QSplineSeries()
        self.serial_output_cnt.setName("出料計數")
        self.serial_output_cnt.setColor(QColor("red"))

        # 設定Chart
        self.mchart_cnt =QtCharts.QChart()
        self.mchart_cnt.setTitle("計數曲線")   # self.mchart.setWindowTitle("Title")
        self.mchart_cnt.addSeries(self.serial_input_cnt)
        self.mchart_cnt.addSeries(self.serial_output_cnt)
        # self.mchart.createDefaultAxes()

        #  設定X軸
        self.dtaxisX_cnt = QtCharts.QValueAxis()
        self.dtaxisX_cnt.setMin(0)
        self.dtaxisX_cnt.setMax(500)
        self.dtaxisX_cnt.setTickCount(10)
        self.dtaxisX_cnt.setTitleText("時間")

        # 設定Y軸
        self.vlaxisY_cnt = QtCharts.QValueAxis()
        self.vlaxisY_cnt.setMin(-5)
        self.vlaxisY_cnt.setMax(5)
        self.vlaxisY_cnt.setTickCount(10)
        self.vlaxisY_cnt.setTitleText("數量")
        self.yvalue = 0

        self.mchart_cnt.addAxis(self.dtaxisX_cnt, Qt.AlignBottom)
        self.mchart_cnt.addAxis(self.vlaxisY_cnt, Qt.AlignLeft)

        self.serial_input_cnt.attachAxis(self.dtaxisX_cnt)
        self.serial_input_cnt.attachAxis(self.vlaxisY_cnt)

        self.serial_output_cnt.attachAxis(self.dtaxisX_cnt)
        self.serial_output_cnt.attachAxis(self.vlaxisY_cnt)

        # 設定CV
        cv = QtCharts.QChartView(self.mchart_cnt)
        cv.chart().setBackgroundBrush(QColor("white"))
        # cv.chart().legend().hide()
        
        # 設定圖像
        self.verticalLayout_cnt.addWidget(cv)
        
    
    def chart_temp(self): # 繪製Real-time temp chart.
        ''' 
        '''
        # 初始化ACC X數據
        self.serial_input_temp = QtCharts.QSplineSeries()
        self.serial_input_temp.setName("入料溫度")
        self.serial_input_temp.setColor(QColor("red"))

        # 設定Chart
        self.mchart_temp =QtCharts.QChart()
        self.mchart_temp.setTitle("溫度曲線")   # self.mchart.setWindowTitle("Title")
        self.mchart_temp.addSeries(self.serial_input_temp)
        # self.mchart.createDefaultAxes()

        # 設定X軸
        self.dtaxisX_temp = QtCharts.QValueAxis()
        self.dtaxisX_temp.setMin(0)
        self.dtaxisX_temp.setMax(500)
        self.dtaxisX_temp.setTickCount(10)
        self.dtaxisX_temp.setTitleText("時間")

        # 設定Y軸
        self.vlaxisY_temp = QtCharts.QValueAxis()
        self.vlaxisY_temp.setMin(-5)
        self.vlaxisY_temp.setMax(5)
        self.vlaxisY_temp.setTickCount(10)
        self.vlaxisY_temp.setTitleText("溫度")
        self.yvalue = 0

        self.mchart_temp.addAxis(self.dtaxisX_temp, Qt.AlignBottom)
        self.mchart_temp.addAxis(self.vlaxisY_temp, Qt.AlignLeft)

        self.serial_input_temp.attachAxis(self.dtaxisX_temp)
        self.serial_input_temp.attachAxis(self.vlaxisY_temp)

        # 設定CV
        cv = QtCharts.QChartView(self.mchart_temp)
        cv.chart().setBackgroundBrush(QColor("white"))
        # cv.chart().legend().hide()
        self.verticalLayout_temp.addWidget(cv)  


    def display(self): # Real-time display chart.
        ''' Display '''      
        tag_data = TagData()        
        self.yvalueList = tag_data.data
        
        self.serial_input_cnt.clear()
        self.serial_output_cnt.clear()

        for idx,val in enumerate(self.yvalueList):
            self.serial_input_cnt.append(idx, val[5])
            self.serial_output_cnt.append(idx, val[6])


class ShengYuanDriver():
    def __init__(self) -> None:
        pass
    
    def handle_vibTool_thread(self):
        app = QApplication(sys.argv)                   
        window=ShengYuan_Main()        # window.setWindowFlag(Qt.FramelessWindowHint)
        window.show()

        Refresh_Timer = QTimer()
        Refresh_Timer.timeout.connect(lambda : window.display())
        
        Refresh_Timer.start(100)
        sys.exit(app.exec_())    


if __name__=="__main__":    
    vib = ShengYuanDriver()
    vib.handle_vibTool_thread()
