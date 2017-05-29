# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'percentagesdialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PercentagesDialog(object):
    def setupUi(self, PercentagesDialog):
        PercentagesDialog.setObjectName("PercentagesDialog")
        PercentagesDialog.resize(763, 348)
        self.buttonBox = QtWidgets.QDialogButtonBox(PercentagesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 305, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(PercentagesDialog)
        self.widget.setGeometry(QtCore.QRect(5, 40, 756, 256))
        self.widget.setObjectName("widget")
        self.tblPercentages = QtWidgets.QTableWidget(self.widget)
        self.tblPercentages.setGeometry(QtCore.QRect(35, 75, 701, 121))
        self.tblPercentages.setObjectName("tblPercentages")
        self.tblPercentages.setColumnCount(6)
        self.tblPercentages.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPercentages.setHorizontalHeaderItem(5, item)
        self.lblPercentages = QtWidgets.QLabel(self.widget)
        self.lblPercentages.setGeometry(QtCore.QRect(-250, 0, 1241, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.lblPercentages.setFont(font)
        self.lblPercentages.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPercentages.setObjectName("lblPercentages")
        self.btnExportPer = QtWidgets.QPushButton(self.widget)
        self.btnExportPer.setGeometry(QtCore.QRect(290, 220, 181, 23))
        self.btnExportPer.setObjectName("btnExportPer")

        self.retranslateUi(PercentagesDialog)
        self.buttonBox.accepted.connect(PercentagesDialog.accept)
        self.buttonBox.rejected.connect(PercentagesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PercentagesDialog)

    def retranslateUi(self, PercentagesDialog):
        _translate = QtCore.QCoreApplication.translate
        PercentagesDialog.setWindowTitle(_translate("PercentagesDialog", "Percentage Results"))
        item = self.tblPercentages.verticalHeaderItem(0)
        item.setText(_translate("PercentagesDialog", "Percentages"))
        item = self.tblPercentages.verticalHeaderItem(1)
        item.setText(_translate("PercentagesDialog", "Tagged Tweets"))
        item = self.tblPercentages.verticalHeaderItem(2)
        item.setText(_translate("PercentagesDialog", "Total Tweets"))
        item = self.tblPercentages.horizontalHeaderItem(0)
        item.setText(_translate("PercentagesDialog", "Political"))
        item = self.tblPercentages.horizontalHeaderItem(1)
        item.setText(_translate("PercentagesDialog", "Race"))
        item = self.tblPercentages.horizontalHeaderItem(2)
        item.setText(_translate("PercentagesDialog", "LGBT"))
        item = self.tblPercentages.horizontalHeaderItem(3)
        item.setText(_translate("PercentagesDialog", "Positivity"))
        item = self.tblPercentages.horizontalHeaderItem(4)
        item.setText(_translate("PercentagesDialog", "Negativity"))
        item = self.tblPercentages.horizontalHeaderItem(5)
        item.setText(_translate("PercentagesDialog", "Neutral"))
        self.lblPercentages.setText(_translate("PercentagesDialog", "Percentages"))
        self.btnExportPer.setText(_translate("PercentagesDialog", "Export Results to Excel"))

