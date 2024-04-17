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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QVBoxLayout,
    QWidget)

from PySide6.QtCharts import QChartView

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(951, 681)
        self.ChartView_2 = QChartView(Dialog)
        self.ChartView_2.setObjectName(u"ChartView_2")
        self.ChartView_2.setGeometry(QRect(20, 40, 911, 181))
        self.pushButton_1 = QPushButton(Dialog)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(100, 570, 81, 24))
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(40, 510, 205, 46))
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
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setMaximum(1)
        self.doubleSpinBox.setSingleStep(0.1)

        self.verticalLayout_2.addWidget(self.doubleSpinBox)

        self.splitter.addWidget(self.layoutWidget1)
        self.label_noise = QLabel(Dialog)
        self.label_noise.setObjectName(u"label_noise")
        self.label_noise.setGeometry(QRect(339, 500, 91, 16))
        self.doubleSpinBox_2 = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimum(0)
        self.doubleSpinBox_2.setMaximum(1)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setGeometry(QRect(320, 530, 121, 22))
        self.doubleSpinBox_2.setDecimals(3)
        self.ChartView3 = QChartView(Dialog)
        self.ChartView3.setObjectName(u"ChartView3")
        self.ChartView3.setGeometry(QRect(20, 270, 911, 192))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 131, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 240, 121, 16))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(510, 500, 371, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(520, 540, 76, 46))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.verticalLayout_3.addWidget(self.doubleSpinBox_4)

        self.widget2 = QWidget(Dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(730, 540, 98, 46))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimum(0)
        self.doubleSpinBox_3.setMaximum(1)
        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setValue(1)

        self.verticalLayout_4.addWidget(self.doubleSpinBox_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def setChart(self, chart):
        self.ChartView3.setChart(chart)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0441\u0442\u043e\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label_cycles.setText(QCoreApplication.translate("Dialog", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0446\u0438\u043a\u043b\u0456\u0432", None))
        self.label_altern.setText(QCoreApplication.translate("Dialog", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0446\u0456\u0457", None))
        self.label_noise.setText(QCoreApplication.translate("Dialog", u"\u0420\u0456\u0432\u0435\u043d\u044c \u0448\u0443\u043c\u0443", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u0442\u0432\u043e\u0440\u0435\u043d\u0438\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0433\u043b\u0430\u0434\u0436\u0435\u043d\u0438\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0432\u0437\u043d\u0435 \u0441\u0435\u0440\u0435\u0434\u043d\u0454", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u0415\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0456\u0439\u043d\u0435 \u0437\u0433\u043b\u0430\u0434\u0436\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0448\u0438\u0440\u0438\u043d\u0430 \u0432\u0456\u043a\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0410\u041b\u042c\u0424\u0410", None))
    # retranslateUi

