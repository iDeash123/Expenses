# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 329)
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,\n"
"    stop:0 rgba(10, 10, 40, 255),\n"
"    stop:0.3 rgba(30, 0, 60, 255),\n"
"    stop:0.6 rgba(0, 70, 100, 255),\n"
"    stop:1 rgba(0, 150, 160, 255));\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_transaction = QFrame(Dialog)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_transaction.setFrameShape(QFrame.Shape.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_new_transaction = QLabel(self.new_transaction)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        font1 = QFont()
        font1.setFamilies([u"Sansation"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        self.lbl_new_transaction.setFont(font1)
        self.lbl_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"font: 700 22pt \"Sansation\";\n"
"background-color: none;\n"
"border: none;")
        self.lbl_new_transaction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.lbl_new_transaction)

        self.cb_choose_category = QComboBox(self.new_transaction)
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.setObjectName(u"cb_choose_category")
        self.cb_choose_category.setStyleSheet(u"QComboBox {\n"
"    font-size: 16pt;\n"
"    color: white;\n"
"	font: 17pt \"Sansation\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2c2c2c; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 \u0444\u043e\u043d \u0441\u043f\u0438\u0441\u043a\u0443 */\n"
"    color: white; /* \u043a\u043e\u043b\u0456\u0440 \u0442\u0435\u043a\u0441\u0442\u0443 \u0432 \u0441\u043f\u0438\u0441\u043a\u0443 */\n"
"    selection-background-color: #444444; /* \u0444\u043e\u043d \u0432\u0438\u0431\u0440\u0430\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0443 */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: white; /* \u043a\u043e\u043b\u0456\u0440 \u043f\u0443\u043d\u043a\u0442\u0456\u0432 \u0441\u043f\u0438\u0441\u043a\u0443 */\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.cb_choose_category)

        self.dateEdit = QDateEdit(self.new_transaction)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"font: 16pt \"Sansation\";")
        self.dateEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(14, 0, 0)))
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.verticalLayout_21.addWidget(self.dateEdit)

        self.le_description = QLineEdit(self.new_transaction)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"	font: 17pt \"Sansation\";")
        self.le_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_21.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.new_transaction)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"	font: 17pt \"Sansation\";")
        self.le_balance.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_21.addWidget(self.le_balance)

        self.cb_status = QComboBox(self.new_transaction)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")
        self.cb_status.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"font: 17pt \"Sansation\";\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: black;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2c2c2c; /* \u0442\u0435\u043c\u043d\u043e-\u0441\u0456\u0440\u0438\u0439 \u0444\u043e\u043d \u0441\u043f\u0438\u0441\u043a\u0443 */\n"
"    color: white; /* \u043a\u043e\u043b\u0456\u0440 \u0442\u0435\u043a\u0441\u0442\u0443 \u0432 \u0441\u043f\u0438\u0441\u043a\u0443 */\n"
"    selection-background-color: #444444; /* \u0444\u043e\u043d \u0432\u0438\u0431\u0440\u0430\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0443 */\n"
"    selection-color: white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.cb_status)

        self.btn_new_transaction = QPushButton(self.new_transaction)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font2 = QFont()
        font2.setFamilies([u"Sansation"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_new_transaction.setFont(font2)
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"	font: 700 20pt \"Sansation\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_new_transaction.setIconSize(QSize(32, 32))
        self.btn_new_transaction.setCheckable(False)

        self.verticalLayout_21.addWidget(self.btn_new_transaction)


        self.verticalLayout.addWidget(self.new_transaction)


        self.retranslateUi(Dialog)

        self.cb_choose_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New\u2795 & \u270f\ufe0fEdit transaction", None))
        self.cb_choose_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u2692\ufe0f Work", None))
        self.cb_choose_category.setItemText(1, QCoreApplication.translate("Dialog", u"\ud83d\ude97 Auto", None))
        self.cb_choose_category.setItemText(2, QCoreApplication.translate("Dialog", u"\ud83e\udde9 Other", None))
        self.cb_choose_category.setItemText(3, QCoreApplication.translate("Dialog", u"\ud83d\uded2 Grocery", None))
        self.cb_choose_category.setItemText(4, QCoreApplication.translate("Dialog", u"\ud83c\udfae Entertainment", None))

        self.cb_choose_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\ud83d\udccd Choose category", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("Dialog", u"\u2b07\ufe0f Income", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("Dialog", u"\u2b06\ufe0f Outcome", None))

        self.cb_status.setPlaceholderText(QCoreApplication.translate("Dialog", u"\ud83d\udccd Choose status", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"\ud83d\udcbe Save  transaction", None))
    # retranslateUi

