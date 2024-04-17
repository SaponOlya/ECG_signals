import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from cardio_cycle_updated import Ui_MainWindow
from PySide6 import QtCharts
from PySide6 import QtCore
import numpy as np
import matplotlib.pyplot

def gaussian_function(t, A, mu, b):
    return A * np.exp(-((t - mu)**2) / (2 * b**2))

def ecg_cycle(t, parameters):
    ecg_val = 0
    for key in parameters:
        A, mu, b = parameters[key]
        ecg_val += gaussian_function(t, A, mu, b)
    return ecg_val

class CardioCucle(QMainWindow):
    def __init__(self):
        super(CardioCucle, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ecg_parameters = {
            'P': (0.11, 0.18, 0.016),
            'Q': (-0.11, 0.22, 0.01),
            'R': (1, 0.27, 0.01),
            'S': (-0.18, 0.315, 0.015),
            'ST': (0, 0.38, 0.04),
            'T': (0.2, 0.531, 0.023)
        }

        self.ui.pushButton.clicked.connect(self.update_parameters)

        self.graph()

    def update_parameters(self):
        amplitude_str = self.ui.lineEdit.text()
        time_str = self.ui.lineEdit_2.text()
        width_str = self.ui.lineEdit_3.text()

        selected_key = self.get_selected_radio_button()

        if amplitude_str and time_str and width_str and selected_key:
            amplitude = float(amplitude_str)
            time = float(time_str)
            width = float(width_str)

            self.ecg_parameters[selected_key] = (amplitude, time, width)
            self.graph()

    def get_selected_radio_button(self):
        if self.ui.radioButton.isChecked():
            return 'P'
        elif self.ui.radioButton_3.isChecked():
            return 'Q'
        elif self.ui.radioButton_5.isChecked():
            return 'R'
        elif self.ui.radioButton_4.isChecked():
            return 'S'
        elif self.ui.radioButton_2.isChecked():
            return 'ST'
        elif self.ui.radioButton_6.isChecked():
            return 'T'
        else:
            return None

    def graph(self):
        # Обновляем график ЭКГ
        t = np.linspace(0, 1, 1000)
        ecg_values = [ecg_cycle(t_i, self.ecg_parameters) for t_i in t]

        series = QtCharts.QLineSeries()
        for i in range(len(t)):
            series.append(i, ecg_values[i])

        chart = QtCharts.QChart()
        chart.addSeries(series)

        self.ui.graphicsView.setChart(chart)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardioCucle()
    window.show()

    sys.exit(app.exec())