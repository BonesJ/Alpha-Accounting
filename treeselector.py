# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeselector.ui'
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
        layoutWidget.resize(624, 165)
        self.horizontalLayout = QtGui.QHBoxLayout(layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.pushButton_16 = QtGui.QPushButton(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_23.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.horizontalLayout_23.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.horizontalLayout_23.addWidget(self.pushButton_18)
        self.verticalLayout_25.addLayout(self.horizontalLayout_23)
        self.treeView_4 = QtGui.QTreeView(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_4.sizePolicy().hasHeightForWidth())
        self.treeView_4.setSizePolicy(sizePolicy)
        self.treeView_4.setSizeIncrement(QtCore.QSize(0, 1))
        self.treeView_4.setAlternatingRowColors(False)
        self.treeView_4.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.treeView_4.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.treeView_4.setIndentation(20)
        self.treeView_4.setRootIsDecorated(False)
        self.treeView_4.setAnimated(False)
        self.treeView_4.setObjectName(_fromUtf8("treeView_4"))
        self.treeView_4.header().setHighlightSections(False)
        self.verticalLayout_25.addWidget(self.treeView_4)
        self.horizontalLayout.addLayout(self.verticalLayout_25)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.radioButton_7 = QtGui.QRadioButton(layoutWidget)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_8.addWidget(self.radioButton_7)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(layoutWidget)
        self.doubleSpinBox_7.setMaximum(999999999.99)
        self.doubleSpinBox_7.setSingleStep(10000.0)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.horizontalLayout_28.addWidget(self.doubleSpinBox_7)
        self.pushButton_6 = QtGui.QPushButton(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(28, 23))
        self.pushButton_6.setMaximumSize(QtCore.QSize(28, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_28.addWidget(self.pushButton_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.label_20 = QtGui.QLabel(layoutWidget)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_8.addWidget(self.label_20)
        self.radioButton_8 = QtGui.QRadioButton(layoutWidget)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_8.addWidget(self.radioButton_8)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(layoutWidget)
        self.doubleSpinBox_8.setMaximum(999999999.99)
        self.doubleSpinBox_8.setSingleStep(10000.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_29.addWidget(self.doubleSpinBox_8)
        self.pushButton_15 = QtGui.QPushButton(layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(28, 23))
        self.pushButton_15.setMaximumSize(QtCore.QSize(28, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout_29.addWidget(self.pushButton_15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        spacerItem = QtGui.QSpacerItem(88, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(layoutWidget)
        QtCore.QMetaObject.connectSlotsByName(layoutWidget)

    def retranslateUi(self, layoutWidget):
        layoutWidget.setWindowTitle(_translate("layoutWidget", "Form", None))
        self.pushButton_16.setToolTip(_translate("layoutWidget", "Add Cateory or Sub-Cateory", None))
        self.pushButton_16.setText(_translate("layoutWidget", "Add Item", None))
        self.pushButton_17.setToolTip(_translate("layoutWidget", "Add Service or Product", None))
        self.pushButton_17.setText(_translate("layoutWidget", "Add Subitem", None))
        self.pushButton_18.setToolTip(_translate("layoutWidget", "Add Service or Product", None))
        self.pushButton_18.setText(_translate("layoutWidget", "Delete Item", None))
        self.radioButton_7.setText(_translate("layoutWidget", "Unit Price ($/unit)", None))
        self.pushButton_6.setText(_translate("layoutWidget", "Edit", None))
        self.label_20.setText(_translate("layoutWidget", "Or", None))
        self.radioButton_8.setText(_translate("layoutWidget", "Rate ($/hr)", None))
        self.pushButton_15.setText(_translate("layoutWidget", "Edit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    layoutWidget = QtGui.QWidget()
    ui = Ui_layoutWidget()
    ui.setupUi(layoutWidget)
    layoutWidget.show()
    sys.exit(app.exec_())

