# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardio_cycle_updated.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(940, 140, 61, 41))
        self.graphicsView = QChartView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(60, 110, 650, 400))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 51, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(940, 190, 43, 152))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.radioButton_3)

        self.radioButton_5 = QRadioButton(self.widget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.widget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.radioButton_4)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.radioButton_2)

        self.radioButton_6 = QRadioButton(self.widget)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.radioButton_6)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(750, 100, 118, 276))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.verticalLayout)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.widget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_5.setGeometry(QRect(100, 350, 50, 27))

        self.pushButton_1 = QPushButton(self.widget1)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.verticalLayout.addWidget(self.pushButton_1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sapon", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Зубець", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Графік", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"ST", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Амплітуда", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Час", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ширина", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ЧСС", None))
    # retranslateUi
