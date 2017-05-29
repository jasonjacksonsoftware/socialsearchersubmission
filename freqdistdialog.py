# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freqdistdialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FreqDistDialog(object):
    def setupUi(self, FreqDistDialog):
        FreqDistDialog.setObjectName("FreqDistDialog")
        FreqDistDialog.resize(908, 773)
        FreqDistDialog.setSizeGripEnabled(False)
        self.frFreqDist = QtWidgets.QFrame(FreqDistDialog)
        self.frFreqDist.setGeometry(QtCore.QRect(0, 5, 891, 761))
        self.frFreqDist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frFreqDist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frFreqDist.setObjectName("frFreqDist")
        self.gridLayout = QtWidgets.QGridLayout(self.frFreqDist)
        self.gridLayout.setObjectName("gridLayout")
        self.tblTopWords = QtWidgets.QTableWidget(self.frFreqDist)
        self.tblTopWords.setRowCount(100)
        self.tblTopWords.setObjectName("tblTopWords")
        self.tblTopWords.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tblTopWords.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTopWords.setHorizontalHeaderItem(1, item)
        self.tblTopWords.horizontalHeader().setCascadingSectionResizes(False)
        self.tblTopWords.horizontalHeader().setDefaultSectionSize(132)
        self.gridLayout.addWidget(self.tblTopWords, 2, 0, 1, 2)
        self.gvFreqDistGraph = QtWidgets.QGraphicsView(self.frFreqDist)
        self.gvFreqDistGraph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.gvFreqDistGraph.setObjectName("gvFreqDistGraph")
        self.gridLayout.addWidget(self.gvFreqDistGraph, 1, 0, 1, 2)
        self.btnSave = QtWidgets.QPushButton(self.frFreqDist)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout.addWidget(self.btnSave, 3, 0, 1, 1)
        self.lblFreqDistGrapg = QtWidgets.QLabel(self.frFreqDist)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblFreqDistGrapg.setFont(font)
        self.lblFreqDistGrapg.setObjectName("lblFreqDistGrapg")
        self.gridLayout.addWidget(self.lblFreqDistGrapg, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frFreqDist)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.retranslateUi(FreqDistDialog)
        self.buttonBox.accepted.connect(FreqDistDialog.accept)
        self.buttonBox.rejected.connect(FreqDistDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FreqDistDialog)

    def retranslateUi(self, FreqDistDialog):
        _translate = QtCore.QCoreApplication.translate
        FreqDistDialog.setWindowTitle(_translate("FreqDistDialog", "Frequency Distribution Results"))
        self.tblTopWords.setSortingEnabled(True)
        item = self.tblTopWords.horizontalHeaderItem(0)
        item.setText(_translate("FreqDistDialog", "Top Words"))
        item = self.tblTopWords.horizontalHeaderItem(1)
        item.setText(_translate("FreqDistDialog", "Number of Occurences"))
        self.btnSave.setText(_translate("FreqDistDialog", "Save Results"))
        self.lblFreqDistGrapg.setText(_translate("FreqDistDialog", "Frequency Distribution Graph (Overall)"))

