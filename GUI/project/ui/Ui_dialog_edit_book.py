# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\elugo\Documents\GitHub\Full_Stack_Programming_for_Complete_Beginners_in_Python\GUI\project\design\dialog_edit_book.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_edit_book(object):
    def setupUi(self, dialog_edit_book):
        dialog_edit_book.setObjectName("dialog_edit_book")
        dialog_edit_book.resize(573, 421)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dialog_edit_book)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(dialog_edit_book)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.splitter_2 = QtWidgets.QSplitter(dialog_edit_book)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.spin_id = QtWidgets.QSpinBox(self.splitter_2)
        self.spin_id.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spin_id.setFont(font)
        self.spin_id.setMaximum(9999)
        self.spin_id.setObjectName("spin_id")
        self.txt_name = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.txt_description = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_description.setFont(font)
        self.txt_description.setObjectName("txt_description")
        self.txt_isbn = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_isbn.setFont(font)
        self.txt_isbn.setObjectName("txt_isbn")
        self.spin_page_count = QtWidgets.QSpinBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spin_page_count.setFont(font)
        self.spin_page_count.setMaximum(9999)
        self.spin_page_count.setObjectName("spin_page_count")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.rad_yes = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rad_yes.setFont(font)
        self.rad_yes.setObjectName("rad_yes")
        self.rad_no = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rad_no.setFont(font)
        self.rad_no.setObjectName("rad_no")
        self.txt_author = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txt_author.setFont(font)
        self.txt_author.setObjectName("txt_author")
        self.spin_year = QtWidgets.QSpinBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spin_year.setFont(font)
        self.spin_year.setMaximum(9999)
        self.spin_year.setObjectName("spin_year")
        self.horizontalLayout.addWidget(self.splitter_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_edit_book)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(dialog_edit_book)
        self.buttonBox.accepted.connect(dialog_edit_book.accept)
        self.buttonBox.rejected.connect(dialog_edit_book.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_edit_book)

    def retranslateUi(self, dialog_edit_book):
        _translate = QtCore.QCoreApplication.translate
        dialog_edit_book.setWindowTitle(_translate("dialog_edit_book", "Edit Book"))
        self.label_9.setText(_translate("dialog_edit_book", "Edit Book"))
        self.label.setText(_translate("dialog_edit_book", "ID"))
        self.label_2.setText(_translate("dialog_edit_book", "Name"))
        self.label_3.setText(_translate("dialog_edit_book", "Description"))
        self.label_4.setText(_translate("dialog_edit_book", "ISBN"))
        self.label_5.setText(_translate("dialog_edit_book", "Page count"))
        self.label_6.setText(_translate("dialog_edit_book", "Issued"))
        self.label_7.setText(_translate("dialog_edit_book", "Author"))
        self.label_8.setText(_translate("dialog_edit_book", "Year"))
        self.rad_yes.setText(_translate("dialog_edit_book", "Yes"))
        self.rad_no.setText(_translate("dialog_edit_book", "No"))
