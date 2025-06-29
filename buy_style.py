# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'styles/buy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 820)
        Dialog.setMinimumSize(QtCore.QSize(590, 820))
        Dialog.setMaximumSize(QtCore.QSize(590, 820))
        Dialog.setStyleSheet("")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("*{\n"
"border : none;\n"
"}\n"
"\n"
"#widget{\n"
"background-color: rgb(29, 35, 50)\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgb(227, 227, 227);\n"
"width: 150px;\n"
"height: 50px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px; \n"
"font: 63 18pt \"Bahnschrift SemiBold Condensed\";\n"
"margin-right: 5px\n"
"}\n"
"\n"
"#tab{\n"
"background-color: rgb(227, 227, 227)\n"
"}\n"
"\n"
"QPushButton, QLineEdit, QSpinBox, QDoubleSpinBox, QPlainTextEdit{\n"
"padding: 8px;\n"
"background-color: white;\n"
"color: rgb(29, 35, 50);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit, QSpinBox, QDoubleSpinBox, QPlainTextEdit{\n"
"border: 1px solid rgb(29, 35, 50);\n"
"}\n"
"\n"
"QPushButton{\n"
"color: white\n"
"}\n"
"\n"
"#enregistrerButton{\n"
"background-color: rgb(30, 255, 30);\n"
"\n"
"}\n"
"\n"
"#annulerButton{\n"
"background-color : rgb(255, 29, 29)\n"
"}\n"
"\n"
"#imageLabel{\n"
"border: 3px dashed rgb(29, 35, 50);\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.categorieLabel = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categorieLabel.setFont(font)
        self.categorieLabel.setObjectName("categorieLabel")
        self.horizontalLayout_4.addWidget(self.categorieLabel)
        self.verticalLayout_3.addWidget(self.widget_8, 0, QtCore.Qt.AlignHCenter)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.nomProduitLabel = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nomProduitLabel.setFont(font)
        self.nomProduitLabel.setObjectName("nomProduitLabel")
        self.horizontalLayout_3.addWidget(self.nomProduitLabel)
        self.verticalLayout_3.addWidget(self.widget_7, 0, QtCore.Qt.AlignHCenter)
        self.imageLabel = QtWidgets.QLabel(self.widget_3)
        self.imageLabel.setMaximumSize(QtCore.QSize(200, 200))
        self.imageLabel.setText("")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_3.addWidget(self.imageLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.fournisseurlineEdit = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fournisseurlineEdit.setFont(font)
        self.fournisseurlineEdit.setObjectName("fournisseurlineEdit")
        self.gridLayout_2.addWidget(self.fournisseurlineEdit, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.dateEntreeLineEdit = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEntreeLineEdit.setFont(font)
        self.dateEntreeLineEdit.setReadOnly(False)
        self.dateEntreeLineEdit.setObjectName("dateEntreeLineEdit")
        self.gridLayout_2.addWidget(self.dateEntreeLineEdit, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.quantiteAchatSpinBox = QtWidgets.QSpinBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantiteAchatSpinBox.setFont(font)
        self.quantiteAchatSpinBox.setMaximum(999999)
        self.quantiteAchatSpinBox.setObjectName("quantiteAchatSpinBox")
        self.gridLayout_2.addWidget(self.quantiteAchatSpinBox, 0, 1, 1, 1)
        self.prixAchatDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prixAchatDoubleSpinBox.setFont(font)
        self.prixAchatDoubleSpinBox.setDecimals(1)
        self.prixAchatDoubleSpinBox.setMaximum(999999.0)
        self.prixAchatDoubleSpinBox.setObjectName("prixAchatDoubleSpinBox")
        self.gridLayout_2.addWidget(self.prixAchatDoubleSpinBox, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 4, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.tab)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.enregistrerButton = QtWidgets.QPushButton(self.widget_5)
        self.enregistrerButton.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enregistrerButton.setFont(font)
        self.enregistrerButton.setObjectName("enregistrerButton")
        self.horizontalLayout_2.addWidget(self.enregistrerButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.annulerButton = QtWidgets.QPushButton(self.widget_5)
        self.annulerButton.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.annulerButton.setFont(font)
        self.annulerButton.setObjectName("annulerButton")
        self.horizontalLayout_2.addWidget(self.annulerButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_14.setText(_translate("Dialog", "Categorie :"))
        self.categorieLabel.setText(_translate("Dialog", "Braclets"))
        self.label_12.setText(_translate("Dialog", "Nom Produit :"))
        self.nomProduitLabel.setText(_translate("Dialog", "Green Braclet 3245"))
        self.label_8.setText(_translate("Dialog", "Prix d\'Achat (dt) :"))
        self.label_10.setText(_translate("Dialog", "Date d\'Entrée :"))
        self.label_9.setText(_translate("Dialog", "Fournisseur :"))
        self.label_11.setText(_translate("Dialog", "Notes :"))
        self.label_7.setText(_translate("Dialog", "Quantité Achetée :"))
        self.enregistrerButton.setText(_translate("Dialog", "Enregistrer"))
        self.annulerButton.setText(_translate("Dialog", "Annuler"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Achetée"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
