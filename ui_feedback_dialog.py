# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_feedback_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Feedback(object):
    def setupUi(self, Feedback):
        Feedback.setObjectName(_fromUtf8("Feedback"))
        Feedback.resize(400, 354)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/qgis2web/icons/qgis2web.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Feedback.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Feedback)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Feedback)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(Feedback)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)
        self.feedbackText = QtGui.QPlainTextEdit(Feedback)
        self.feedbackText.setReadOnly(True)
        self.feedbackText.setObjectName(_fromUtf8("feedbackText"))
        self.gridLayout.addWidget(self.feedbackText, 0, 0, 1, 1)

        self.retranslateUi(Feedback)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Feedback.accept)
        QtCore.QMetaObject.connectSlotsByName(Feedback)

    def retranslateUi(self, Feedback):
        Feedback.setWindowTitle(_translate("Feedback", "Progress", None))

import resources_rc
