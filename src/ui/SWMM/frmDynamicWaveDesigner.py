# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmDynamicWaveDesigner.ui'
#
# Created: Tue Mar 08 16:50:14 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_frmDynamicWave(object):
    def setupUi(self, frmDynamicWave):
        frmDynamicWave.setObjectName(_fromUtf8("frmDynamicWave"))
        frmDynamicWave.resize(345, 402)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmDynamicWave.setFont(font)
        self.centralWidget = QtGui.QWidget(frmDynamicWave)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame1 = QtGui.QFrame(self.centralWidget)
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lblInertial = QtGui.QLabel(self.frame1)
        self.lblInertial.setObjectName(_fromUtf8("lblInertial"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblInertial)
        self.cboInertial = QtGui.QComboBox(self.frame1)
        self.cboInertial.setMinimumSize(QtCore.QSize(50, 0))
        self.cboInertial.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboInertial.setObjectName(_fromUtf8("cboInertial"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboInertial)
        self.lblNormal = QtGui.QLabel(self.frame1)
        self.lblNormal.setObjectName(_fromUtf8("lblNormal"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblNormal)
        self.cboNormal = QtGui.QComboBox(self.frame1)
        self.cboNormal.setMinimumSize(QtCore.QSize(50, 0))
        self.cboNormal.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboNormal.setObjectName(_fromUtf8("cboNormal"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboNormal)
        self.lblForce = QtGui.QLabel(self.frame1)
        self.lblForce.setObjectName(_fromUtf8("lblForce"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblForce)
        self.cboForce = QtGui.QComboBox(self.frame1)
        self.cboForce.setMinimumSize(QtCore.QSize(50, 0))
        self.cboForce.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboForce.setObjectName(_fromUtf8("cboForce"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboForce)
        self.verticalLayout.addWidget(self.frame1)
        self.frame2 = QtGui.QFrame(self.centralWidget)
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName(_fromUtf8("frame2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbxUseVariable = QtGui.QCheckBox(self.frame2)
        self.cbxUseVariable.setObjectName(_fromUtf8("cbxUseVariable"))
        self.horizontalLayout_2.addWidget(self.cbxUseVariable)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lblAdjusted = QtGui.QLabel(self.frame2)
        self.lblAdjusted.setObjectName(_fromUtf8("lblAdjusted"))
        self.horizontalLayout_2.addWidget(self.lblAdjusted)
        self.sbxAdjusted = QtGui.QSpinBox(self.frame2)
        self.sbxAdjusted.setObjectName(_fromUtf8("sbxAdjusted"))
        self.horizontalLayout_2.addWidget(self.sbxAdjusted)
        self.lblPercent = QtGui.QLabel(self.frame2)
        self.lblPercent.setObjectName(_fromUtf8("lblPercent"))
        self.horizontalLayout_2.addWidget(self.lblPercent)
        self.verticalLayout.addWidget(self.frame2)
        self.frame3 = QtGui.QFrame(self.centralWidget)
        self.frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setObjectName(_fromUtf8("frame3"))
        self.formLayout = QtGui.QFormLayout(self.frame3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblMinimum = QtGui.QLabel(self.frame3)
        self.lblMinimum.setObjectName(_fromUtf8("lblMinimum"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblMinimum)
        self.txtMinimum = QtGui.QLineEdit(self.frame3)
        self.txtMinimum.setObjectName(_fromUtf8("txtMinimum"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtMinimum)
        self.lblTimeStep = QtGui.QLabel(self.frame3)
        self.lblTimeStep.setObjectName(_fromUtf8("lblTimeStep"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblTimeStep)
        self.txtLengthening = QtGui.QLineEdit(self.frame3)
        self.txtLengthening.setObjectName(_fromUtf8("txtLengthening"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtLengthening)
        self.lblSurface = QtGui.QLabel(self.frame3)
        self.lblSurface.setObjectName(_fromUtf8("lblSurface"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblSurface)
        self.txtSurfaceArea = QtGui.QLineEdit(self.frame3)
        self.txtSurfaceArea.setObjectName(_fromUtf8("txtSurfaceArea"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtSurfaceArea)
        self.lblMaximum = QtGui.QLabel(self.frame3)
        self.lblMaximum.setObjectName(_fromUtf8("lblMaximum"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblMaximum)
        self.sbxTrials = QtGui.QSpinBox(self.frame3)
        self.sbxTrials.setObjectName(_fromUtf8("sbxTrials"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sbxTrials)
        self.lblHead = QtGui.QLabel(self.frame3)
        self.lblHead.setObjectName(_fromUtf8("lblHead"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblHead)
        self.txtTolerance = QtGui.QLineEdit(self.frame3)
        self.txtTolerance.setObjectName(_fromUtf8("txtTolerance"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtTolerance)
        self.lblThreads = QtGui.QLabel(self.frame3)
        self.lblThreads.setObjectName(_fromUtf8("lblThreads"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lblThreads)
        self.cboThreads = QtGui.QComboBox(self.frame3)
        self.cboThreads.setObjectName(_fromUtf8("cboThreads"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cboThreads)
        self.verticalLayout.addWidget(self.frame3)
        self.fraButtons = QtGui.QFrame(self.centralWidget)
        self.fraButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QtGui.QFrame.Raised)
        self.fraButtons.setObjectName(_fromUtf8("fraButtons"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(142, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cmdOK = QtGui.QPushButton(self.fraButtons)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraButtons)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraButtons)
        frmDynamicWave.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmDynamicWave)
        QtCore.QMetaObject.connectSlotsByName(frmDynamicWave)
        frmDynamicWave.setTabOrder(self.cboInertial, self.cboNormal)
        frmDynamicWave.setTabOrder(self.cboNormal, self.cboForce)
        frmDynamicWave.setTabOrder(self.cboForce, self.cbxUseVariable)
        frmDynamicWave.setTabOrder(self.cbxUseVariable, self.sbxAdjusted)
        frmDynamicWave.setTabOrder(self.sbxAdjusted, self.txtMinimum)
        frmDynamicWave.setTabOrder(self.txtMinimum, self.txtLengthening)
        frmDynamicWave.setTabOrder(self.txtLengthening, self.txtSurfaceArea)
        frmDynamicWave.setTabOrder(self.txtSurfaceArea, self.sbxTrials)
        frmDynamicWave.setTabOrder(self.sbxTrials, self.txtTolerance)
        frmDynamicWave.setTabOrder(self.txtTolerance, self.cboThreads)
        frmDynamicWave.setTabOrder(self.cboThreads, self.cmdOK)
        frmDynamicWave.setTabOrder(self.cmdOK, self.cmdCancel)

    def retranslateUi(self, frmDynamicWave):
        frmDynamicWave.setWindowTitle(_translate("frmDynamicWave", "SWMM Dynamic Wave Options", None))
        self.lblInertial.setText(_translate("frmDynamicWave", "Inertial Terms", None))
        self.lblNormal.setText(_translate("frmDynamicWave", "Normal Flow Criterion", None))
        self.lblForce.setText(_translate("frmDynamicWave", "Force Main Equation", None))
        self.cbxUseVariable.setText(_translate("frmDynamicWave", "Use Variable Time Steps", None))
        self.lblAdjusted.setText(_translate("frmDynamicWave", "Adjusted By", None))
        self.lblPercent.setText(_translate("frmDynamicWave", "%", None))
        self.lblMinimum.setText(_translate("frmDynamicWave", "Minimum Variable Time Step (sec)", None))
        self.lblTimeStep.setText(_translate("frmDynamicWave", "Time Step for Conduit Lengthening (sec)", None))
        self.lblSurface.setText(_translate("frmDynamicWave", "Minimum Nodal Surface Area (sq feet)", None))
        self.lblMaximum.setText(_translate("frmDynamicWave", "Maximum Trials Per Time Step", None))
        self.lblHead.setText(_translate("frmDynamicWave", "Head Convergence Tolerance (feet)", None))
        self.lblThreads.setText(_translate("frmDynamicWave", "Number of Threads", None))
        self.cmdOK.setText(_translate("frmDynamicWave", "OK", None))
        self.cmdCancel.setText(_translate("frmDynamicWave", "Cancel", None))
