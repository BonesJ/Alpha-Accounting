# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeselector.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from itertools import cycle
from PyQt4 import QtCore, QtGui

TRUE_OR_FALSE = cycle([False, True])

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

DB = "Alpha.db"

# ========================================================================
import sys
import icons_rc

class Node(object):

    def __init__(self, name, parent=None):

        self._name = name
        self._flat_price = None
        self._rate_price = None

        self._children = []
        self._parent = parent

        if parent is not None:
            parent.addChild(self)


    def typeInfo(self):
        return "NODE"

    def addChild(self, child):
        self._children.append(child)

    def insertChild(self, position, child):

        if position < 0 or position > len(self._children):
            return False

        self._children.insert(position, child)
        child._parent = self
        return True

    def removeChild(self, position):

        if position < 0 or position > len(self._children):
            return False

        child = self._children.pop(position)
        child._parent = None

        return True


    def name(self):
        return self._name

    def fprice(self):
        return self._flat_price

    def rprice(self):
        return self._rate_price

    def setName(self, name):
        # if section == 0:
        self._name = name

    def setPrice(self, price):
        # if section == 0:
        print "price at setPrice>>", price
        self._flat_price = float(price)


    def setPriceR(self, price):
        # if section == 0:
        print "price at setPriceR>>", price
        self._rate_price = float(price)


    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def log_level(self, tabLevel=-1):

        output = ""
        tabLevel += 1

        for i in range(tabLevel):
            output += "\t"
        # print "before>>", self._name
        if type(self._name) is not type("a"):
            self._name=self._name.toString()
            # print "entered"
            # print "after>>", self._name str(tabLevel) +

        output += self._name #+ "\n"

        for child in self._children:
            output += child.log_level(tabLevel)

        tabLevel -= 1
        output += "\n"

        return output

    def log(self, tabLevel=-1):

        output = ""
        tabLevel += 1

        for i in range(tabLevel):
            output += "\t"
        # print "before>>", self._name
        if type(self._name) is not type("a"):
            self._name=self._name.toString()
            # print "entered"
            # print "after>>", self._name

        output += "|------" + self._name + "\n"

        for child in self._children:
            output += child.log(tabLevel)

        tabLevel -= 1
        output += "\n"

        return output
    #  uncomment to graphically tab separet different levels, need numbers to work
    # def __repr__(self):
    #     return str(self.log())

    # def __repr__(self):
    #     return str(self.log_level())


class TransformNode(Node):

    def __init__(self, name, parent=None):
        super(TransformNode, self).__init__(name, parent)

    def typeInfo(self):
        return "TRANSFORM"


class CameraNode(Node):

    def __init__(self, name, parent=None):
        super(CameraNode, self).__init__(name, parent)

    def typeInfo(self):
        return "CAMERA"


class LightNode(Node):

    def __init__(self, name, parent=None):
        super(LightNode, self).__init__(name, parent)

    def typeInfo(self):
        return "LIGHT"


class SceneGraphModel(QtCore.QAbstractItemModel):

    """INPUTS: Node, QObject"""
    def __init__(self, root, parent=None):
        super(SceneGraphModel, self).__init__(parent)
        self._rootNode = root

    """INPUTS: QModelIndex"""
    """OUTPUT: int"""
    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()

        return parentNode.childCount()

    """INPUTS: QModelIndex"""
    """OUTPUT: int"""
    def recursiveRowCount(self, parent):

        parentNode = self._rootNode

        return parentNode.childCount()



    """INPUTS: QModelIndex"""
    """OUTPUT: int"""
    def columnCount(self, parent):
        return 3

    """INPUTS: QModelIndex, int"""
    """OUTPUT: QVariant, strings are cast to QString which is a QVariant"""
    def data(self, index, role):

        if not index.isValid():
            return None

        node = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if index.column() == 0:
                return node.name()
            if index.column() == 1:
                return node.fprice()
            if index.column() == 2:
                return node.rprice()

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                typeInfo = node.typeInfo()

                if typeInfo == "LIGHT":
                    return QtGui.QIcon(QtGui.QPixmap(":/Light.png"))

                if typeInfo == "TRANSFORM":
                    return QtGui.QIcon(QtGui.QPixmap(":/Transform.png"))

                if typeInfo == "CAMERA":
                    return QtGui.QIcon(QtGui.QPixmap(":/Camera.png"))

    def fetchData(self, index):

        node = index
        return node.log_level()


    """INPUTS: QModelIndex, QVariant, int (flag)"""
    def setData(self, index, value, role=QtCore.Qt.EditRole):

        if index.isValid():

            if role == QtCore.Qt.EditRole:

                node = index.internalPointer()
                if index.column() == 0:
                    node.setName(value)

                if (index.column() == 1) :
                    node.setPrice(value)

                if (index.column() == 2) :
                    node.setPriceR(value)

                return True
        return False


    """INPUTS: int, Qt::Orientation, int"""
    """OUTPUT: QVariant, strings are cast to QString which is a QVariant"""
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if section == 0:
                return "Services & Products"
            elif section == 1:
                return "Flat rate"
            elif section == 2:
                return "Hourly rate"


    """INPUTS: QModelIndex"""
    """OUTPUT: int (flag)"""
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable


    """INPUTS: QModelIndex"""
    """OUTPUT: QModelIndex"""
    """Should return the parent of the node with the given QModelIndex"""
    def parent(self, index):

        node = self.getNode(index)
        parentNode = node.parent()

        if parentNode == self._rootNode:
            return QtCore.QModelIndex()

        return self.createIndex(parentNode.row(), 0, parentNode)

    """INPUTS: int, int, QModelIndex"""
    """OUTPUT: QModelIndex"""
    """Should return a QModelIndex that corresponds to the given row, column and parent node"""
    # def index(self, row, column, parent):

    #     parentNode = self.getNode(parent)

    #     childItem = parentNode.child(row)


    #     if childItem:
    #         return self.createIndex(row, column, childItem)
    #     else:
    #         return QtCore.QModelIndex()

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if self.hasIndex(row, column, parent):
            parent_node = self.getNode(parent)
            child_item = parent_node.child(row)
            if child_item:
                return self.createIndex(row, column, child_item)
        else:
            return QtCore.QModelIndex()



    """CUSTOM"""
    """INPUTS: QModelIndex"""
    def getNode(self, index, root=None):
        if index.isValid():

            if (root is not None) and (root == True):
                print "Fetching root node for output..."
                return self._rootNode

            node = index.internalPointer()
            if node:
                return node

        return self._rootNode


    """INPUTS: int, int, QModelIndex"""
    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):

        parentNode = self.getNode(parent)

        self.beginInsertRows(parent, position, position + rows - 1)

        for row in range(rows):

            childCount = parentNode.childCount()
            childNode = Node("untitled" + str(childCount))
            success = parentNode.insertChild(position, childNode)

        self.endInsertRows()

        return success

    def insertLights(self, position, rows, parent=QtCore.QModelIndex()):

        parentNode = self.getNode(parent)

        self.beginInsertRows(parent, position, position + rows - 1)

        for row in range(rows):

            childCount = parentNode.childCount()
            childNode = LightNode("light" + str(childCount))
            success = parentNode.insertChild(position, childNode)

        self.endInsertRows()

        return success

    """INPUTS: int, int, QModelIndex"""
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):

        parentNode = self.getNode(parent)
        self.beginRemoveRows(parent, position, position + rows - 1)

        for row in range(rows):
            success = parentNode.removeChild(position)

        self.endRemoveRows()

        return success


def print_tree():
    print rootNode


# ========================================================================


class Ui_(QtGui.QWidget):

    def __init__(self, parent=None):
        super(QtGui.QWidget,self).__init__(parent)

        def lock_unlock_tree():
            global TRUE_OR_FALSE
            # toggle_switch = cycle(TRUE_OR_FALSE)
            boolean = TRUE_OR_FALSE.next()
            print boolean
            # self.pushButton_14.setEnabled(boolean)
            self.pushButton_16.setEnabled(boolean)
            self.pushButton_17.setEnabled(boolean)
            self.pushButton_18.setEnabled(boolean)


        self.layoutWidget = QtGui.QWidget()
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 624, 165))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))

        self.pushButton_14 = QtGui.QPushButton("Lock/Unlock")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout_23.addWidget(self.pushButton_14)

        self.pushButton_16 = QtGui.QPushButton("Add Item")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_23.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton("Add Subitem")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.horizontalLayout_23.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton("Delete Item")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.horizontalLayout_23.addWidget(self.pushButton_18)
        self.verticalLayout_25.addLayout(self.horizontalLayout_23)
        self.productStructView = QtGui.QTreeView(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productStructView.sizePolicy().hasHeightForWidth())
        self.productStructView.setSizePolicy(sizePolicy)
        self.productStructView.setSizeIncrement(QtCore.QSize(0, 1))
        self.productStructView.setAlternatingRowColors(False)
        # self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.productStructView.setObjectName(_fromUtf8("productStructView"))
        self.productStructView.header().setStretchLastSection(False)
        # self.productStructView.setEditTriggers(self.productStructView.NoEditTriggers)
        # self.productStructView.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.productStructView.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.verticalLayout_25.addWidget(self.productStructView)
        self.horizontalLayout.addLayout(self.verticalLayout_25)
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.radioButton_7 = QtGui.QRadioButton("Unit Price ($/unit)")
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_8.addWidget(self.radioButton_7)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_7.setMaximum(999999999.99)
        self.doubleSpinBox_7.setSingleStep(10000.0)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.horizontalLayout_28.addWidget(self.doubleSpinBox_7)
        self.btnEdit1 = QtGui.QPushButton("Edit")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEdit1.sizePolicy().hasHeightForWidth())
        self.btnEdit1.setSizePolicy(sizePolicy)
        self.btnEdit1.setMinimumSize(QtCore.QSize(28, 23))
        self.btnEdit1.setMaximumSize(QtCore.QSize(28, 23))
        self.btnEdit1.setObjectName(_fromUtf8("btnEdit1"))
        self.horizontalLayout_28.addWidget(self.btnEdit1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_8.addWidget(self.label_20)
        self.radioButton_8 = QtGui.QRadioButton("Rate ($/hr)")
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_8.addWidget(self.radioButton_8)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_8.setMaximum(999999999.99)
        self.doubleSpinBox_8.setSingleStep(10000.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_29.addWidget(self.doubleSpinBox_8)
        self.btnEdit2 = QtGui.QPushButton("Edit")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEdit2.sizePolicy().hasHeightForWidth())
        self.btnEdit2.setSizePolicy(sizePolicy)
        self.btnEdit2.setMinimumSize(QtCore.QSize(28, 23))
        self.btnEdit2.setMaximumSize(QtCore.QSize(28, 23))
        self.btnEdit2.setObjectName(_fromUtf8("btnEdit2"))
        self.horizontalLayout_29.addWidget(self.btnEdit2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        spacerItem = QtGui.QSpacerItem(88, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.setLayout(self.horizontalLayout)
        # print "\n<<Successfully Added Tree selector>>\n"

        self.pushButton_14.clicked.connect(lock_unlock_tree)
        self.pushButton_14.setIcon(QtGui.QIcon(':/icons/Lock_2_Filled.png'))
        self.pushButton_14.setIconSize(QtCore.QSize(24,24))

        # self.pushButton_18.clicked.connect()


class Ui_layoutWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(QtGui.QWidget,self).__init__(parent)

        self.layoutWidget = QtGui.QWidget()
        self.layoutWidget.setObjectName(_fromUtf8("self.layoutWidget"))
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.resize(711, 266)
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))

        # self.productStructView = QtGui.QTreeView(self.layoutWidget)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.productStructView.sizePolicy().hasHeightForWidth())
        # self.productStructView.setSizePolicy(sizePolicy)
        # self.productStructView.setSizeIncrement(QtCore.QSize(0, 1))
        # self.productStructView.setAlternatingRowColors(False)
        # self.productStructView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        # self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        # self.productStructView.setIndentation(20)
        # self.productStructView.setRootIsDecorated(False)
        # self.productStructView.setAnimated(False)
        # self.productStructView.setObjectName(_fromUtf8("productStructView"))
        # self.productStructView.header().setHighlightSections(False)
        self.productStructView = QtGui.QTreeView(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productStructView.sizePolicy().hasHeightForWidth())
        self.productStructView.setSizePolicy(sizePolicy)
        self.productStructView.setSizeIncrement(QtCore.QSize(0, 1))
        self.productStructView.setAlternatingRowColors(False)
        # self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.productStructView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.productStructView.setObjectName(_fromUtf8("productStructView"))
        self.productStructView.header().setStretchLastSection(False)

        self.verticalLayout_25.addWidget(self.productStructView)
        self.horizontalLayout.addLayout(self.verticalLayout_25)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.radioButton_7 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_8.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_8.addWidget(self.radioButton_8)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_8.addWidget(self.checkBox)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_8.setAccelerated(False)
        self.doubleSpinBox_8.setPrefix(_fromUtf8(""))
        self.doubleSpinBox_8.setMaximum(999999999.99)
        self.doubleSpinBox_8.setSingleStep(1.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_29.addWidget(self.doubleSpinBox_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        spacerItem1 = QtGui.QSpacerItem(88, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_8.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(88, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.layoutWidget.setWindowTitle(_translate("layoutWidget", "Form", None))
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
        QtCore.QMetaObject.connectSlotsByName(self.layoutWidget)
        self.setLayout(self.horizontalLayout)

        # connection = sqlite3.connect(DB)
        # cursor = connection.cursor()
        # # # UNCOMMENT SECTION FOR DEBUGGING /START/
        # # cursor.execute("""SELECT * FROM client""")
        # # result_all = cursor.fetchall()
        # # print "result all:", result_all
        # # # UNCOMMENT SECTION FOR DEBUGGING /END/

        # cursor.execute("""SELECT DISTINCT "Code Client" FROM client""")
        # result_key = cursor.fetchall()
        # connection.close()
        # # clients table ...
        # cursor.execute("""
        #     CREATE TABLE if not exisits "PRODUCTS STRUCT" (
        #     "key" INTEGER PRIMARY KEY AUTOINCREMENT,
        #     "Code Client" VARCHAR(30),
        #     "Nom" VARCHAR(30),
        #     "Societe" VARCHAR(30),
        #     "Telephone" VARCHAR(30),
        #     "Factures Payees" INTEGER(1),
        #     "Factures Recues" INTEGER(1),
        #     "Email" VARCHAR(40),
        #     UNIQUE ("key") );""")

        # # Populate db with some data ...
        # cursor = connection.cursor()
        # staff_data = [
        #     (55, "James", "kaloumba", "021 69 74 49", 5, 8, "ceemss.saiatgmail"),
        #     (7, "WilliamNOT", "sadoomba", "021 69 74 49", 5, 8, "cf.saiatgmail"),
        #     (7, "William", "badoomba", "021 69 74 49", 5, 8, "ceems.saiatgmail"),
        #     (7, "Williwas", "frambounda", "021 69 74 49", 5, 8, "ceemssatgmail")
        # ]
        # cursor.executemany("""
        #     INSERT INTO client ("key","Code Client", "Nom", "Societe", "Telephone",
        #         "Factures Payees", "Factures Recues", "Email")
        #     VALUES(NULL,?,?,?,?,?,?,?)""", staff_data)
        # connection.commit()
        # print "\n<<Successfully Created `PRODUCTS STRUCT` table>>\n"
