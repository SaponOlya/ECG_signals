# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laba3_window2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QSplitter,
    QVBoxLayout, QWidget)

from PySide6.QtCharts import QChartView

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(951, 452)
        self.ChartView_2 = QChartView(Dialog)
        self.ChartView_2.setObjectName(u"ChartView_2")
        self.ChartView_2.setGeometry(QRect(20, 40, 911, 251))
        self.pushButton_1 = QPushButton(Dialog)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(111, 390, 81, 24))
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(51, 330, 205, 46))
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_cycles = QLabel(self.layoutWidget)
        self.label_cycles.setObjectName(u"label_cycles")

        self.verticalLayout.addWidget(self.label_cycles)

        self.spinBox_cycles = QSpinBox(self.layoutWidget)
        self.spinBox_cycles.setObjectName(u"spinBox_cycles")

        self.verticalLayout.addWidget(self.spinBox_cycles)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_altern = QLabel(self.layoutWidget1)
        self.label_altern.setObjectName(u"label_altern")

        self.verticalLayout_2.addWidget(self.label_altern)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.verticalLayout_2.addWidget(self.doubleSpinBox)

        self.splitter.addWidget(self.layoutWidget1)
        self.label_noise = QLabel(Dialog)
        self.label_noise.setObjectName(u"label_noise")
        self.label_noise.setGeometry(QRect(350, 320, 91, 16))
        self.doubleSpinBox_2 = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(331, 350, 121, 22))
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setSingleStep(0.001000000000000)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 131, 16))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 350, 111, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0441\u0442\u043e\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label_cycles.setText(QCoreApplication.translate("Dialog", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0446\u0438\u043a\u043b\u0456\u0432", None))
        self.label_altern.setText(QCoreApplication.translate("Dialog", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0446\u0456\u0457", None))
        self.label_noise.setText(QCoreApplication.translate("Dialog", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0448\u0443\u043c\u0443", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0433\u043b\u0430\u0434\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
    # retranslateUi

