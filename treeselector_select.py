# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeselector_select.ui'
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

class Ui_layoutWidget(object):
    def setupUi(self, layoutWidget):
        layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        layoutWidget.setEnabled(True)
        layoutWidget.resize(711, 266)
        self.horizontalLayout = QtGui.QHBoxLayout(layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.productStructView = QtGui.QTreeView(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productStructView.sizePolicy().hasHeightForWidth())
        self.productStructView.setSizePolicy(sizePolicy)
        self.productStructView.setSizeIncrement(QtCore.QSize(0, 1))
        self.productStructView.setAlternatingRowColors(False)
        self.productStructView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.productStructView.setIndentation(20)
        self.productStructView.setRootIsDecorated(False)
        self.productStructView.setAnimated(False)
        self.productStructView.setObjectName(_fromUtf8("productStructView"))
        self.productStructView.header().setHighlightSections(False)
        self.verticalLayout_25.addWidget(self.productStructView)
        self.horizontalLayout.addLayout(self.verticalLayout_25)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label = QtGui.QLabel(layoutWidget)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.radioButton_7 = QtGui.QRadioButton(layoutWidget)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_8.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(layoutWidget)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_8.addWidget(self.radioButton_8)
        self.checkBox = QtGui.QCheckBox(layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_8.addWidget(self.checkBox)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(layoutWidget)
        self.doubleSpinBox_8.setAccelerated(False)
        self.doubleSpinBox_8.setPrefix(_fromUtf8(""))
        self.doubleSpinBox_8.setMaximum(999999999.99)
        self.doubleSpinBox_8.setSingleStep(1.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_29.addWidget(self.doubleSpinBox_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        spacerItem1 = QtGui.QSpacerItem(88, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(88, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        layoutWidget.setWindowTitle(_translate("layoutWidget", "Form", None))
        self.label.setText(_translate("layoutWidget", "Selectionner méthode de facturation (a la tâche ou de l\'heure):", None))
        self.radioButton_7.setText(_translate("layoutWidget", "Prix Unitaire (DA/unité)", None))
        self.radioButton_8.setText(_translate("layoutWidget", "Prix Horaire (DA/h)", None))
        self.checkBox.setText(_translate("layoutWidget", "Marge Supplémentaire or Réduction", None))
        self.doubleSpinBox_8.setSuffix(_translate("layoutWidget", "%", None))
        self.label_2.setText(_translate("layoutWidget", "Article:", None))
        self.label_3.setText(_translate("layoutWidget", "PRODUIT OU SERVICE", None))
        self.label_5.setText(_translate("layoutWidget", "Prix à afficher:", None))
        self.label_4.setText(_translate("layoutWidget", "PRODUIT OU SERVICE", None))
        self.pushButton.setText(_translate("layoutWidget", "Valider", None))
        QtCore.QMetaObject.connectSlotsByName(layoutWidget)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    layoutWidget = QtGui.QWidget()
    ui = Ui_layoutWidget()
    ui.setupUi(layoutWidget)
    layoutWidget.show()
    sys.exit(app.exec_())

