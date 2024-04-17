# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGraphicsView,
    QLabel, QRadioButton, QScrollBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1047, 559)
        Dialog.setStyleSheet(u"font-size: 12pt")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 51, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(930, 120, 61, 31))
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(50, 90, 591, 381))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(720, 120, 181, 301))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalScrollBar = QScrollBar(self.widget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalScrollBar)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalScrollBar_3 = QScrollBar(self.widget)
        self.horizontalScrollBar_3.setObjectName(u"horizontalScrollBar_3")
        self.horizontalScrollBar_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalScrollBar_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalScrollBar_2 = QScrollBar(self.widget)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        self.horizontalScrollBar_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalScrollBar_2)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(930, 170, 43, 152))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_2)

        self.radioButton_5 = QRadioButton(self.widget1)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.widget1)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.widget1)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.radioButton_3)

        self.radioButton_6 = QRadioButton(self.widget1)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.radioButton_6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0446\u0438\u043a\u043b \u043a\u0430\u0440\u0434\u0456\u043e\u0433\u0440\u0430\u043c\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0417\u0443\u0431\u0435\u0446\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0410\u043c\u043f\u043b\u0456\u0442\u0443\u0434\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0427\u0430\u0441", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"P", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Q", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"R", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"S", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"ST", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"T", None))
    # retranslateUi

