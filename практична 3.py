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

# гаусівська функція
def gauss_function(t, A, mu, sigma):
    return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

# генерація одного циклу ЕКГ
def generate_ECG_component(t, A, mu, sigma_function, duration):
    signal = np.zeros_like(t)
    idx = (t >= mu - duration * sigma_function(mu)) & (t <= mu + duration * sigma_function(mu))
    signal[idx] = gauss_function(t[idx], A, mu, sigma_function(t[idx]))
    # print("Generated component:", signal)
    return signal

# генерація декількох циклів ЕКГ
def generate_ECG(t, A, mu, sigma_function, duration, num_cycles):
    signal = np.zeros_like(t)
    idx = (t >= mu - duration * sigma_function(mu)) & (t <= mu + duration * sigma_function(mu))
    signal[idx] = gauss_function(t[idx], A, mu, sigma_function(t[idx]))
    # signal = np.tile(signal, num_cycles)
    return signal

# функція що забезпечує зміну ширини зубця
def sigma_function(t, mu, sigma_max, sigma_min):
    return np.where(t < mu, sigma_min, sigma_max)

# експоненційне згладжування
def exponential_smoothing(data, alpha):
    smoothed_data = [data[0]]
    for i in range(1, len(data)):
        smoothed_value = alpha * data[i] + (1 - alpha) * smoothed_data[i-1]  # формула експоненційного згладжування
        smoothed_data.append(sgmoothed_value)
    return smoothed_data


# ковзне середнє
def moving_average(data, window_size):
    # Ініціалізація масива для ковзного середнього
    smoothed_data = np.zeros_like(data)

    for i in range(len(data)):
        # встановлення межей вікна
        lower_bound = max(0, int(i - window_size // 2))
        upper_bound = min(len(data), int(i + window_size // 2 + 1))

        # Обчислення середнього значення всередині вікна
        smoothed_data[i] = np.mean(data[lower_bound:upper_bound])

    return smoothed_data

# адаптивне згладжування
def adaptive_smooth(data, window_size, h):
    smoothed_data = np.zeros_like(data)
    wk = window_size

    for i in range(len(data)):
        wk = min(wk, window_size)
        if i > 0:
            delta_Wk = min(max(smoothed_data[i - 1] - data[i - 1], -1), 1)  # Вираховуємо зміну розміру вікна
            wk += delta_Wk

        wk = max(1, wk)

        if np.abs(data[i] - smoothed_data[i-1]) <= h:
            alpha_i = 1 / (1 + wk)
        else:
            alpha_i = wk / (1 + wk)

        if i == 0:
            smoothed_data[i] = data[i]
        else:
            smoothed_data[i] = alpha_i * data[i] + (1 - alpha_i) * smoothed_data[i-1]

    return smoothed_data


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

        # оновлення полів де записані параметри зубців
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

    # оновлення полів, де записані параметри зубців
    def update_line_edit(self, selected_key):
        params = self.parameters[selected_key]
        self.ui.lineEdit.setText(str(params['A']))
        self.ui.lineEdit_2.setText(str(params['mu']))
        self.ui.lineEdit_3.setText(str(params['sigma_max']))
        self.ui.lineEdit_4.setText(str(params['sigma_min']))

    # відкриття нового вікна
    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.chart_view = self.ui_window.ChartView_2
        self.new_window.show()
        self.ui_window.pushButton_1.clicked.connect(self.graph_2)
        self.ui_window.pushButton.clicked.connect(self.open_third_window)
        self.ui_window.doubleSpinBox.valueChanged.connect(self.on_scrollbar_changed)
        self.ui_window.doubleSpinBox_2.valueChanged.connect(self.add_noise)

    # відкриття третього вікна
    def open_third_window(self):
        self.third_window = QtWidgets.QDialog()
        self.ui_window_3 = Ui_Dialog_1()
        self.ui_window_3.setupUi(self.third_window)
        self.third_window.show()
        self.ui_window_3.doubleSpinBox.valueChanged.connect(self.del_noise)
        self.ui_window_3.doubleSpinBox_2.valueChanged.connect(self.del_noise)
        self.ui_window_3.doubleSpinBox_5.valueChanged.connect(self.del_noise)
        self.ui_window_3.radioButton.toggled.connect(self.blocked)
        self.ui_window_3.radioButton_2.toggled.connect(self.blocked)
        self.ui_window_3.radioButton_3.toggled.connect(self.blocked)
    #_______________________________________________________________________________________
    # блокування кнопок
    def blocked(self):
        smooth_type = self.select_smooth()
        if smooth_type == 'exp':
            self.ui_window_3.doubleSpinBox.setEnabled(True)
            self.ui_window_3.doubleSpinBox_2.setEnabled(False)
            self.ui_window_3.spinBox.setEnabled(False)
            self.ui_window_3.doubleSpinBox_5.setEnabled(False)
        elif smooth_type == 'mean':
            self.ui_window_3.doubleSpinBox.setEnabled(False)
            self.ui_window_3.doubleSpinBox_2.setEnabled(True)
            self.ui_window_3.spinBox.setEnabled(False)
            self.ui_window_3.doubleSpinBox_5.setEnabled(False)
        elif smooth_type == 'adaptive':
            self.ui_window_3.doubleSpinBox.setEnabled(False)
            self.ui_window_3.doubleSpinBox_2.setEnabled(False)
            self.ui_window_3.spinBox.setEnabled(True)
            self.ui_window_3.doubleSpinBox_5.setEnabled(True)

    # зміна альтернації
    def on_scrollbar_changed(self, value):
        alternation = self.ui_window.doubleSpinBox.value()
        self.ui_window.doubleSpinBox.setValue(alternation)
        self.graph_2()

    # додавання шуму
    def add_noise(self):
        noise = self.ui_window.doubleSpinBox_2.value()
        self.ui_window.doubleSpinBox_2.setValue(noise)
        self.graph_2()

    # видалення шуму
    def del_noise(self):
        alpha = self.ui_window_3.doubleSpinBox.value()
        self.ui_window_3.doubleSpinBox.setValue(alpha)
        window_size = self.ui_window_3.doubleSpinBox_2.value()
        self.ui_window_3.doubleSpinBox_2.setValue(window_size)
        max_window = self.ui_window_3.spinBox.value()
        self.ui_window_3.spinBox.setValue(max_window)
        threshold = self.ui_window_3.doubleSpinBox_5.value()
        self.ui_window_3.doubleSpinBox_5.setValue(threshold)
        smooth_type = self.select_smooth()
        self.graph_2(smooth=True, smooth_type=smooth_type, alpha=alpha, window_size=window_size, max_wind=max_window, therehold=threshold)

    # вибір типу згладжування
    def select_smooth(self):
        if self.ui_window_3.radioButton.isChecked():
            return 'exp'
        elif self.ui_window_3.radioButton_2.isChecked():
            return 'mean'
        elif self.ui_window_3.radioButton_3.isChecked():
            return 'adaptive'
        else:
            return None

#___________________________________________________________________________________________________________________
    # побудова графіку
    def graph_2(self, smooth=False, smooth_type=None, alpha=1, window_size=1, max_wind=0, therehold=0):
        periods_str = self.ui_window.spinBox_cycles.value()   # кількість циклів
        alternation_str = self.ui_window.doubleSpinBox.value()   # рівень альтернації
        noise_ampl = self.ui_window.doubleSpinBox_2.value()   # амплітуда шуму
        if periods_str:
            t = np.linspace(0, 1, 1000)
            rate = 60
            periods = int(periods_str)
            alternation = float(alternation_str)
            t_ampl = self.parameters['T']['A']
            # амплітуда зубця Т з врахуванням альтернації
            T_amplitude = (1 + (alternation / t_ampl)) * t_ampl
            # генерація шуму
            noise = noise_ampl * np.random.randn(len(t))

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

                    # згладжування в залежності від типу
                    if smooth_type == 'exp':
                        smoothed_signal = exponential_smoothing(sum(ECG_components.values()), alpha)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    elif smooth_type == 'mean':
                        smoothed_signal = moving_average(sum(ECG_components.values()), window_size)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    elif smooth_type == 'adaptive':
                        smoothed_signal = adaptive_smooth(sum(ECG_components.values()), max_wind, therehold)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    else:
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        series2 = QtCharts.QLineSeries()
                        series2.setColor(color)
                        for j in range(len(t)):
                            ecg_value = sum(ECG_components[component][j] for component in self.parameters.keys())
                            series.append(j + i * len(t), ecg_value)
                            series2.append(j + i * len(t), ecg_value)

                    # Додаємо серію даних на графік
                    chart.addSeries(series)

                # Відображення графіка
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

                    if smooth_type == 'exp':
                        smoothed_signal = exponential_smoothing(sum(ECG_components.values()), alpha)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    elif smooth_type == 'mean':
                        smoothed_signal = moving_average(sum(ECG_components.values()), window_size)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    elif smooth_type == 'adaptive':
                        smoothed_signal = adaptive_smooth(sum(ECG_components.values()), max_wind, therehold)
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            series.append(j + i * len(t), smoothed_signal[j])
                    else:
                        series = QtCharts.QLineSeries()
                        series.setColor(color)
                        for j in range(len(t)):
                            ecg_value = sum(ECG_components[component][j] for component in self.parameters.keys())
                            series.append(j + i * len(t), ecg_value)

                    chart.addSeries(series)

                self.chart_view.setChart(chart)

        # наносимо сітку на графік
        self.chart_view.chart().createDefaultAxes()
        self.chart_view.chart().axisX().setGridLineVisible(True)
        self.chart_view.chart().axisY().setGridLineVisible(True)
#__________________________________________________________________________________________________________________
    # оновлення параметрів зубців
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

    # вибір зубця для зміни параметрів
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

    # побудова циклу екг
    def graph(self):
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
                series.append(i, ecg_value)  # Додаємо значення часу і сигналу

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