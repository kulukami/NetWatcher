#!/usr/bin/python2.7
#!--coding:utf-8--!#
# Author : Shinukami

import sys
from PyQt4 import QtCore, QtGui

from os import listdir
from os import system
from time import sleep

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Shinukamis(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.setObjectName(_fromUtf8("Shinukamis"))
        self.setEnabled(True)
        self.resize(304, 252)
        self.Device="lo"
        self.Watcher=Worker(Device=self.Device)
        self.Watcher.start()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Study/Python-study/Tkinter/3/Black18.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.setStatusTip(_fromUtf8("Shinukami's Work"))

        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 285, 228))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))

        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)

        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())

        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())

        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())

        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())

        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)

        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 2, 1, 1)

        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi()

        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),
                     self.SetDev)

        self.connect(self,QtCore.SIGNAL('output(QString)'),
                     self.Watcher.setDev)

        self.connect(self.Watcher,QtCore.SIGNAL('output(QString)'),
                     self.SetData)


    def retranslateUi(self):
        self.setWindowTitle(_translate("Shinukamis", "Shinukami\'s  NetWatch", None))
        self.label_5.setText(_translate("Shinukamis", "p/s", None))
        self.pushButton.setText(_translate("Shinukamis", "Set", None))
        self.lineEdit_3.setText(_translate("Shinukamis", "0", None))
        self.label_8.setText(_translate("Shinukamis", "Tsp Bts", None))
        self.label_6.setText(_translate("Shinukamis", "b/s", None))
        self.label_2.setText(_translate("Shinukamis", "Rcv Pks", None))
        self.label_3.setText(_translate("Shinukamis", "Rcv Bts", None))
        self.label_4.setText(_translate("Shinukamis", "Tsp Pks", None))
        self.label_7.setText(_translate("Shinukamis", "p/s", None))
        self.lineEdit_4.setText(_translate("Shinukamis", "0", None))
        self.lineEdit_2.setText(_translate("Shinukamis", "0", None))
        self.lineEdit_5.setText(_translate("Shinukamis", "0", None))
        self.label_9.setText(_translate("Shinukamis", "b/s", None))
        self.label.setText(_translate("Shinukamis", "Device", None))

    def SetDev(self):
        self.emit(QtCore.SIGNAL('output(QString)'),self.lineEdit.text())

    def SetData(self,data):
        self.lineEdit_2.setText(data.split('|')[0])
        self.lineEdit_3.setText(data.split("|")[1])
        self.lineEdit_4.setText(data.split("|")[2])
        self.lineEdit_5.setText(data.split("|")[3])

class Worker(QtCore.QThread):
    def __init__(self,parent=None,Device=''):
        super(Worker,self).__init__(parent)
        self.working=True
        self.Dev=Device
    def __del__(self):
        self.working=False
        self.wait()
    def ShowDev(self):
        timeout=2
        Path = "/sys/class/net/"
        Dev_files = ["rx_packets","tx_packets","rx_bytes","tx_bytes"]
        Files = [ open(Path+self.Dev+"/statistics/"+i) for i in Dev_files ]
        Data1 = [ int(i.read()) for i in Files ]
        for i in Files: i.close()
        sleep(timeout)
        Files = [ open(Path+self.Dev+"/statistics/"+i) for i in Dev_files ]
        Data2 = [ int(i.read()) for i in Files ]
        res= str((Data2[0]-Data1[0])/timeout)+'|'+str((Data2[2]-Data1[2])/timeout)+'|'+str((Data2[1]-Data1[1])/timeout)+'|'+str((Data2[3]-Data1[3])/timeout)
        self.emit(QtCore.SIGNAL('output(QString)'),res)
    def run(self):
        while self.working==True:
            self.ShowDev()
    def setDev(self,Dev):
        self.Dev=Dev


app=QtGui.QApplication(sys.argv)
w=Shinukamis()
w.show()
sys.exit(app.exec_())
