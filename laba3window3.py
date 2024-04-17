# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laba3_window3.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog_1(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(603, 245)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(380, 130, 161, 46))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout.addWidget(self.doubleSpinBox_5, 1, 1, 1, 1)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(61, 90, 470, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(220, 130, 98, 46))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setMaximum(1)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setValue(1)

        self.verticalLayout.addWidget(self.doubleSpinBox)

        self.widget2 = QWidget(Dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(80, 130, 78, 46))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0435 \u0432\u0456\u043a\u043d\u043e", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u0456\u0433", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0432\u0437\u043d\u0435 \u0441\u0435\u0440\u0435\u0434\u043d\u0454", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u0415\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0456\u0439\u043d\u0435 \u0437\u0433\u043b\u0430\u0434\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u0430\u043f\u0442\u0438\u0432\u043d\u0435 \u0437\u0433\u043b\u044f\u0434\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0410\u041b\u042c\u0424\u0410", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0432\u0456\u043a\u043d\u0430", None))
    # retranslateUi

