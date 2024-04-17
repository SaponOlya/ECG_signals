import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from laba3 import Ui_MainWindow
from laba3window2 import Ui_Dialog
from laba3window3 import Ui_Dialog_1
from PySide6 import QtCharts
from PySide6 import QtCore
import numpy as np
from PySide6.QtGui import QColor

def gauss_function(t, A, mu, sigma):
    return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

def generate_ECG_component(t, A, mu, sigma_function, duration):
    signal = np.zeros_like(t)
    idx = (t >= mu - duration * sigma_function(mu)) & (t <= mu + duration * sigma_function(mu))
    signal[idx] = gauss_function(t[idx], A, mu, sigma_function(t[idx]))
    # print("Generated component:", signal)
    return signal

def generate_ECG(t, A, mu, sigma_function, duration, num_cycles):
    signal = np.zeros_like(t)
    idx = (t >= mu - duration * sigma_function(mu)) & (t <= mu + duration * sigma_function(mu))
    signal[idx] = gauss_function(t[idx], A, mu, sigma_function(t[idx]))
    # signal = np.tile(signal, num_cycles)
    return signal

def sigma_function(t, mu, sigma_max, sigma_min):
    return np.where(t < mu, sigma_min, sigma_max)

class CardioCucle(QMainWindow):
    def __init__(self):
        super(CardioCucle, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Параметри гаусовых функцій для генерації компонентів ЕКГ
        self.parameters = {
            'P': {'A': 0.11, 'mu': 0.18, 'sigma_max': 0.016, 'sigma_min': 0.016, 'duration': 3},
            'Q': {'A': -0.11, 'mu': 0.22, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
            'R': {'A': 1.0, 'mu': 0.27, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
            'S': {'A': -0.18, 'mu': 0.315, 'sigma_max': 0.015, 'sigma_min': 0.015, 'duration': 3},
            'ST': {'A': 0, 'mu': 0.38, 'sigma_max': 0.04, 'sigma_min': 0.04, 'duration': 3},
            'T': {'A': 0.2, 'mu': 0.531, 'sigma_max': 0.05, 'sigma_min': 0.05, 'duration': 3}
        }

        self.ui.radioButton.toggled.connect(lambda: self.update_line_edit('P'))
        self.ui.radioButton_3.toggled.connect(lambda: self.update_line_edit('Q'))
        self.ui.radioButton_5.toggled.connect(lambda: self.update_line_edit('R'))
        self.ui.radioButton_4.toggled.connect(lambda: self.update_line_edit('S'))
        self.ui.radioButton_2.toggled.connect(lambda: self.update_line_edit('ST'))
        self.ui.radioButton_6.toggled.connect(lambda: self.update_line_edit('T'))

        self.ui.pushButton.clicked.connect(self.update_parameters)
        self.ui.pushButton_2.clicked.connect(self.graph)
        self.ui.pushButton_3.clicked.connect(self.open_new_window)

        self.graph()

    def update_line_edit(self, selected_key):
        # Обновление lineEdit с параметрами по умолчанию
        params = self.parameters[selected_key]
        self.ui.lineEdit.setText(str(params['A']))
        self.ui.lineEdit_2.setText(str(params['mu']))
        self.ui.lineEdit_3.setText(str(params['sigma_max']))
        self.ui.lineEdit_4.setText(str(params['sigma_min']))

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.chart_view = self.ui_window.ChartView_2
        self.new_window.show()
        self.ui_window.pushButton_1.clicked.connect(self.graph_2)
        self.ui_window.doubleSpinBox.valueChanged.connect(self.on_scrollbar_changed)
        self.ui_window.doubleSpinBox_2.valueChanged.connect(self.add_noise)
        self.ui_window.pushButton.clicked.connect(self.open_3_window)

    def open_3_window(self):
        self.third_window = QtWidgets.QDialog()
        self.ui_window_3 = Ui_Dialog_1()
        self.ui_window_3.setupUi(self.third_window)
        self.chart_view3 = self.ui_window_3.chartView_3
        self.ui_window_3.setChart(self.chart_view.chart())
        self.third_window.show()
    #_______________________________________________________________________________________
    def on_scrollbar_changed(self, value):
        alternation = self.ui_window.doubleSpinBox.value()
        self.ui_window.doubleSpinBox.setValue(alternation)
        self.graph_2()

    def add_noise(self):
        noise = self.ui_window.doubleSpinBox_2.value()
        self.ui_window.doubleSpinBox_2.setValue(noise)
        self.graph_2()

    def graph_2(self):
        periods_str = self.ui_window.spinBox_cycles.value()
        alternation_str = self.ui_window.doubleSpinBox.value()
        noise_ampl = self.ui_window.doubleSpinBox_2.value()
        if periods_str:
            t = np.linspace(0, 5, 1000)
            rate = 60
            periods = int(periods_str)
            alternation = float(alternation_str)
            t_ampl = self.parameters['T']['A']
            T_amplitude = (1 + (alternation / t_ampl)) * t_ampl
            noise = noise_ampl * np.random.randn(len(t))

            # Создаём пустой график
            chart = QtCharts.QChart()
            chart.createDefaultAxes()
            color = QColor("#FF5733")

            if periods % 2 == 0:
                for i in range(periods):
                    ECG_components = {}
                    for component, params in self.parameters.items():
                        if component == 'T':
                            if i % 2 == 0:
                                params['A'] = T_amplitude
                            else:
                                params['A'] = 0.2
                        ECG_components[component] = generate_ECG(t, params['A'], params['mu'],
                                                                 lambda t: sigma_function(t, params['mu'],
                                                                                          params['sigma_max'],
                                                                                          params['sigma_min']),
                                                                 params['duration'], periods) + noise

                    # Создаём серию данных для текущего цикла
                    series = QtCharts.QLineSeries()
                    series.setColor(color)
                    for j in range(len(t)):
                        ecg_value = sum(ECG_components[component][j] for component in self.parameters.keys())
                        series.append(j + i * len(t), ecg_value)

                    # Добавляем серию данных на график
                    chart.addSeries(series)

                # Устанавливаем график для отображения в представлении
                self.chart_view.setChart(chart)
            else:
                for i in range(periods):
                    ECG_components = {}
                    for component, params in self.parameters.items():
                        if component == 'T' and i % 2 == 0:
                            params['A'] = 0.2
                        elif component == 'T' and i % 2 != 0:
                            params['A'] = T_amplitude
                        ECG_components[component] = generate_ECG(t, params['A'], params['mu'],
                                                                 lambda t: sigma_function(t, params['mu'],
                                                                                          params['sigma_max'],
                                                                                          params['sigma_min']),
                                                                 params['duration'], periods) + noise

                    # Создаём серию данных для текущего цикла
                    series = QtCharts.QLineSeries()
                    series.setColor(color)
                    for j in range(len(t)):
                        ecg_value = sum(ECG_components[component][j] for component in self.parameters.keys())
                        series.append(j + i * len(t), ecg_value)

                    # Добавляем серию данных на график
                    chart.addSeries(series)

                # Устанавливаем график для отображения в представлении
                self.chart_view.setChart(chart)

        self.chart_view.chart().createDefaultAxes()
        self.chart_view.chart().axisX().setGridLineVisible(True)
        self.chart_view.chart().axisY().setGridLineVisible(True)

    def update_parameters(self):
        amplitude_str = self.ui.lineEdit.text()
        time_str = self.ui.lineEdit_2.text()
        width1_str = self.ui.lineEdit_3.text()
        width2_str = self.ui.lineEdit_4.text()

        selected_key = self.get_selected_radio_button()

        if amplitude_str and time_str and width1_str and width2_str and selected_key:
            amplitude = float(amplitude_str)
            time = float(time_str)
            width1 = float(width1_str)
            width2 = float(width2_str)

            self.parameters[selected_key]['A'] = amplitude
            self.parameters[selected_key]['mu'] = time
            self.parameters[selected_key]['sigma_max'] = width1
            self.parameters[selected_key]['sigma_min'] = width2

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
        heart_rate_str = self.ui.lineEdit_5.text()
        if heart_rate_str:
            heart_rate = float(heart_rate_str)
            rate = 60 / heart_rate
            t = np.linspace(0, 2, 1000)
            ECG_components = {}
            for component, params in self.parameters.items():
                ECG_components[component] = generate_ECG_component(t/rate, params['A'], params['mu'],
                                                                   lambda t: sigma_function(t, params['mu'],
                                                                                            params['sigma_max'],
                                                                                             params['sigma_min']),
                                                                   params['duration'])

            ECG_signal = sum(ECG_components.values())

            series = QtCharts.QLineSeries()
            for i in range(len(t)):
                ecg_value = sum(ECG_components[component][i] for component in self.parameters.keys())
                series.append(i, ecg_value)  # Добавляем значения времени t[i] и сигнала ECG_signal[i]

            chart = QtCharts.QChart()
            chart.addSeries(series)

            chart.createDefaultAxes()
            chart.axisX().setGridLineVisible(True)
            chart.axisY().setGridLineVisible(True)

            chart.axisX().setTitleText("Час")
            chart.axisY().setTitleText("Амплітуда")

            self.ui.graphicsView.setChart(chart)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardioCucle()
    window.show()

    sys.exit(app.exec())