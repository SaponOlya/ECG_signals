# import numpy as np
# import matplotlib.pyplot as plt
#
# def gauss_function(t, A, mu, sigma):
#     return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
#
# def generate_ECG_component(t, A, mu, sigma):
#     return gauss_function(t, A, mu, sigma)
#
# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma': 0.016},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma': 0.01},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma': 0.01},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma': 0.015},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma': 0.04},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma': 0.023}
# }
#
# # Генерация временных отсчетов
# t = np.linspace(0, 1, 1000)
#
# # Генерация компонентов ЭКГ
# ECG_components = {}
# for component, params in parameters.items():
#     ECG_components[component] = generate_ECG_component(t, params['A'], params['mu'], params['sigma'])
#
# # Получение полного сигнала ЭКГ путем суммирования компонентов
# ECG_signal = sum(ECG_components.values())
#
# # Построение графика
# plt.figure(figsize=(10, 6))
# plt.plot(t, ECG_signal, label='ЭКГ сигнал')
# # for component, signal in ECG_components.items():
# #     plt.plot(t, signal, label=component)
# plt.title('Генерация сигнала ЭКГ')
# plt.xlabel('Время')
# plt.ylabel('Амплитуда')
# plt.legend()
# plt.grid(True)
# plt.show()
#_______________________________________________________________________________________________

# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma_max': 0.016, 'sigma_min': 0.016, 'duration': 3},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma_max': 0.015, 'sigma_min': 0.015, 'duration': 3},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma_max': 0.04, 'sigma_min': 0.04, 'duration': 3},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma_max': 0.01, 'sigma_min': 0.012, 'duration': 3}
# }
#_______________________________________________________________________________________________________________
# import numpy as np
# import matplotlib.pyplot as plt
#
# def gauss_function(t, A, mu, sigma):
#     return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
#
# def generate_ECG_component(t, A, mu, sigma):
#     return gauss_function(t, A, mu, sigma)
#
# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma': 0.016},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma': 0.01},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma': 0.01},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma': 0.015},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma': 0.04},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma': 0.023}
# }
#
# # Генерация временных отсчетов
# t = np.linspace(0, 1, 1000)
#
# # Генерация компонентов ЭКГ
# ECG_components = {}
# for component, params in parameters.items():
#     ECG_components[component] = generate_ECG_component(t, params['A'], params['mu'], params['sigma'])
#
# # Получение полного сигнала ЭКГ путем суммирования компонентов
# ECG_signal = sum(ECG_components.values())
#
# np.random.seed(0)  # Установка seed для воспроизводимости
# noise_amplitude = 0.2  # Амплитуда шума
# noise = noise_amplitude * np.random.randn(len(t))  # Генерация шума
#
# # Добавление шума к сигналу ЭКГ
# ECG_signal_with_noise = ECG_signal + noise
#
# # Применение экспоненциального сглаживания
# def exponential_smoothing(data, alpha):
#     smoothed_data = [data[0]]  # Инициализация первого значения сглаженной последовательности
#     for i in range(1, len(data)):
#         smoothed_data.append(alpha * data[i] + (1 - alpha) * smoothed_data[-1])
#     return np.array(smoothed_data)
#
# alpha = 0.08  # Параметр сглаживания (0 < alpha < 1)
# smoothed_signal = exponential_smoothing(ECG_signal_with_noise, alpha)
#
# # Построение графика
# plt.figure(figsize=(10, 6))
#
# # Построение сигнала с шумом
# plt.plot(t, ECG_signal_with_noise, label='Сигнал с шумом')
#
# # Построение сглаженного сигнала
# plt.plot(t, smoothed_signal, color='red', label='Сглаженный сигнал')
#
# plt.title('Применение экспоненциального сглаживания к сигналу ЭКГ с шумом')
# plt.xlabel('Время')
# plt.ylabel('Амплитуда')
# plt.legend()
# plt.grid(True)
# plt.show()
#________________________________________________________________________________________________________

# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma_max': 0.016, 'sigma_min': 0.016},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma_max': 0.01, 'sigma_min': 0.01},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma_max': 0.01, 'sigma_min': 0.01},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma_max': 0.015, 'sigma_min': 0.015},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma_max': 0.04, 'sigma_min': 0.04},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma_max': 0.05, 'sigma_min': 0.023}
# }
#_______________________________________________________________________________________________________________
# import numpy as np
# import matplotlib.pyplot as plt
#
# def gauss_function(t, A, mu, sigma):
#     return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
#
# def generate_ECG_component(t, A, mu, sigma):
#     return gauss_function(t, A, mu, sigma)
#
# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma': 0.016},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma': 0.01},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma': 0.01},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma': 0.015},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma': 0.04},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma': 0.023}
# }
#
# # Генерация временных отсчетов
# t = np.linspace(0, 1, 1000)
#
# # Генерация компонентов ЭКГ
# ECG_components = {}
# for component, params in parameters.items():
#     ECG_components[component] = generate_ECG_component(t, params['A'], params['mu'], params['sigma'])
#
# # Получение полного сигнала ЭКГ путем суммирования компонентов
# ECG_signal = sum(ECG_components.values())
#
# np.random.seed(0)  # Установка seed для воспроизводимости
# noise_amplitude = 0.2  # Амплитуда шума
# noise = noise_amplitude * np.random.randn(len(t))  # Генерация шума
#
# # Добавление шума к сигналу ЭКГ
# ECG_signal_with_noise = ECG_signal + noise
#
# # Применение экспоненциального сглаживания
# def moving_average(data, window_size):
#     """
#     Вычисляет скользящее среднее для заданного ряда данных.
#
#     Параметры:
#     - data: массив данных
#     - window_size: размер окна для вычисления среднего
#
#     Возвращает:
#     - массив скользящего среднего
#     """
#     # Инициализация массива для скользящего среднего
#     smoothed_data = np.zeros_like(data)
#
#     # Вычисление скользящего среднего
#     for i in range(len(data)):
#         # Установка границы окна
#         lower_bound = max(0, i - window_size // 2)
#         upper_bound = min(len(data), i + window_size // 2 + 1)
#
#         # Вычисление среднего значения внутри окна
#         smoothed_data[i] = np.mean(data[lower_bound:upper_bound])
#
#     return np.array(smoothed_data)
#
#
# window_size = 100  # Параметр сглаживания (0 < alpha < 1)
# smoothed_signal = moving_average(ECG_signal_with_noise, window_size)
#
# # Построение графика
# plt.figure(figsize=(10, 6))
#
# # Построение сигнала с шумом
# plt.plot(t, ECG_signal_with_noise, label='Сигнал с шумом')
#
# # Построение сглаженного сигнала
# plt.plot(t, smoothed_signal, color='red', label='Сглаженный сигнал')
#
# plt.title('Применение экспоненциального сглаживания к сигналу ЭКГ с шумом')
# plt.xlabel('Время')
# plt.ylabel('Амплитуда')
# plt.legend()
# plt.grid(True)
# plt.show()
#_________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt

def gauss_function(t, A, mu, sigma):
    return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))

def generate_ECG_component(t, A, mu, sigma):
    return gauss_function(t, A, mu, sigma)

# Параметры гауссовых функций для генерации компонентов ЭКГ
parameters = {
    'P': {'A': 0.11, 'mu': 0.18, 'sigma': 0.016},
    'Q': {'A': -0.11, 'mu': 0.22, 'sigma': 0.01},
    'R': {'A': 1.0, 'mu': 0.27, 'sigma': 0.01},
    'S': {'A': -0.18, 'mu': 0.315, 'sigma': 0.015},
    'ST': {'A': 0, 'mu': 0.38, 'sigma': 0.04},
    'T': {'A': 0.2, 'mu': 0.531, 'sigma': 0.023}
}

# Генерация временных отсчетов
t = np.linspace(0, 1, 1000)

# Генерация компонентов ЭКГ
ECG_components = {}
for component, params in parameters.items():
    ECG_components[component] = generate_ECG_component(t, params['A'], params['mu'], params['sigma'])

# Получение полного сигнала ЭКГ путем суммирования компонентов
ECG_signal = sum(ECG_components.values())

np.random.seed(0)  # Установка seed для воспроизводимости
noise_amplitude = 0.2  # Амплитуда шума
noise = noise_amplitude * np.random.randn(len(t))  # Генерация шума

# Добавление шума к сигналу ЭКГ
ECG_signal_with_noise = ECG_signal + noise

# Применение экспоненциального сглаживания
def adaptive_smooth(data, window_size, h):
    """
    Вычисляет скользящее среднее для заданного ряда данных.

    Параметры:
    - data: массив данных
    - window_size: размер окна для вычисления среднего

    Возвращает:
    - массив скользящего среднего
    """
    # Инициализация массива для скользящего среднего
    smoothed_data = np.zeros_like(data)
    wk = window_size

    # Вычисление скользящего среднего
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


window_size = 32  # Параметр сглаживания (0 < alpha < 1)
h = 9
smoothed_signal = adaptive_smooth(ECG_signal_with_noise, window_size, h)

# Построение графика
plt.figure(figsize=(10, 6))

# Построение сигнала с шумом
plt.plot(t, ECG_signal_with_noise, label='Сигнал с шумом')

# Построение сглаженного сигнала
plt.plot(t, smoothed_signal, color='red', label='Сглаженный сигнал')

plt.title('Применение экспоненциального сглаживания к сигналу ЭКГ с шумом')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)
plt.show()
#____________________________________________________________________________________
# import numpy as np
# import matplotlib.pyplot as plt
#
# def gauss_function(t, A, mu, sigma):
#     return A * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
#
# def generate_ECG_component(t, A, mu, sigma_function, duration, num_cycles, alternation=None):
#     signal = np.zeros_like(t)
#
#     for i in range(num_cycles):
#         if alternation is not None and i % 2 != 0:
#             A = (1 + alternation) * A
#             idx = (t >= mu - duration * sigma_function(mu)) & (t <= mu + duration * sigma_function(mu))
#             signal[idx] += gauss_function(t[idx], A, mu, sigma_function(t[idx]))
#     signal = np.tile(signal, num_cycles)
#
#     return signal
#
# # Параметры гауссовых функций для генерации компонентов ЭКГ
# parameters = {
#     'P': {'A': 0.11, 'mu': 0.18, 'sigma_max': 0.016, 'sigma_min': 0.016, 'duration': 3},
#     'Q': {'A': -0.11, 'mu': 0.22, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
#     'R': {'A': 1.0, 'mu': 0.27, 'sigma_max': 0.01, 'sigma_min': 0.01, 'duration': 3},
#     'S': {'A': -0.18, 'mu': 0.315, 'sigma_max': 0.015, 'sigma_min': 0.015, 'duration': 3},
#     'ST': {'A': 0, 'mu': 0.38, 'sigma_max': 0.04, 'sigma_min': 0.04, 'duration': 3},
#     'T': {'A': 0.2, 'mu': 0.531, 'sigma_max': 0.05, 'sigma_min': 0.023, 'duration': 3}
# }
#
# # Функция для генерации несимметричной сигмы
# def sigma_function(t, mu, sigma_max, sigma_min):
#     return np.where(t < mu, sigma_min, sigma_max)
#
# # Генерация временных отсчетов
# rate = 60
# num_samples = 1000
# t = np.linspace(0, 1 * num_samples / rate, num_samples)
#
# # Альтернация зубца T
# alternation = 0.5  # Новое значение амплитуды зубца T через каждый второй цикл
# noise_ampl = 0.1
# noise = noise_ampl * np.random.random(len(t))
#
# # Генерация шума для каждого компонента сигнала ЭКГ
# noise_components = {}
# for component in parameters:
#     noise_components[component] = noise_ampl * np.random.random(len(t))
#
# # Создание компонентов сигнала ЭКГ с учетом шума
# ECG_components = {}
# for component, params in parameters.items():
#     if component == 'T':
#         ECG_components[component] = generate_ECG_component(t / rate, params['A'], params['mu'],
#                                                            lambda t: sigma_function(t, params['mu'],
#                                                                                     params['sigma_max'],
#                                                                                     params['sigma_min']),
#                                                            params['duration'], num_cycles=1, alternation=alternation)
#     else:
#         ECG_components[component] = generate_ECG_component(t / rate, params['A'], params['mu'],
#                                                            lambda t: sigma_function(t, params['mu'],
#                                                                                     params['sigma_max'],
#                                                                                     params['sigma_min']),
#                                                            params['duration'], num_cycles=1, alternation=0)
#
# # Создание сигнала ЭКГ
# ECG_signal = sum(ECG_components.values())
#
# # Добавление шума к каждому компоненту сигнала ЭКГ
# ECG_signal_with_noise = ECG_signal.copy()  # Создание копии сигнала ЭКГ
# for component in noise_components:
#     ECG_signal_with_noise += noise_components[component]
#
# # Применение экспоненциального сглаживания
# def exponential_smoothing(data, alpha):
#     smoothed_data = [data[0]]  # Инициализация первого значения сглаженной последовательности
#     for i in range(1, len(data)):
#         smoothed_data.append(alpha * data[i] + (1 - alpha) * smoothed_data[-1])
#     return np.array(smoothed_data)
#
# alpha = 0.01  # Параметр сглаживания (0 < alpha < 1)
# smoothed_signal = exponential_smoothing(ECG_signal_with_noise, alpha)
#
# # Построение графика
# plt.figure(figsize=(10, 6))
#
# plt.plot(t, ECG_signal)
#
# # # Построение сигнала с шумом
# # plt.plot(t, ECG_signal_with_noise, label='Сигнал с шумом', alpha=0.5)
# #
# # # Построение сглаженного сигнала
# # plt.plot(t, smoothed_signal, color='red', label='Сглаженный сигнал')
#
# plt.title('Применение экспоненциального сглаживания к сигналу ЭКГ с шумом')
# plt.xlabel('Время')
# plt.ylabel('Амплитуда')
# plt.legend()
# plt.grid(True)
# plt.show()
