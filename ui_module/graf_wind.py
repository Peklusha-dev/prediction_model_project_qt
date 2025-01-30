from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWindow(QMainWindow):
    def __init__(self, data=None, context=None, context_data=None):
        """
        Окно для отображения графика анализа данных.

        :param data: Словарь с данными {год: результат, ...}.
        :param context: Контекст вызова окна ('employee', 'group', 'department', 'unit', 'institute').
        :param context_data: Данные для заголовка (разные форматы в зависимости от контекста).
        """
        super().__init__()
        self.setWindowTitle("Результаты анализа")
        self.setGeometry(100, 100, 800, 600)

        self.data = data or {}
        self.context = context
        self.context_data = context_data

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Заголовок
        self.info_label = QLabel(self.get_title_text(), self)
        self.info_label.setStyleSheet("font-size: 14px; margin-bottom: 10px;")
        layout.addWidget(self.info_label)

        # Холст
        self.canvas = FigureCanvas(Figure(figsize=(6, 4)))
        layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

        # Отображаем график
        if self.data:
            self.plot_data()

        # Рекомендации
        self.recommendations_label = QLabel("Рекомендуем повторить материал.")
        self.recommendations_label.setStyleSheet(
            "font-size: 12px; margin-top: 10px; color: #555;"
        )
        layout.addWidget(self.recommendations_label)

    def get_title_text(self):
        """Формирует заголовок окна в зависимости от контекста."""
        if self.context is None:
            return "Анализ данных"

        if self.context == "employee":
            return (f"<b>ФИО:</b> {self.context_data[0].get('ФИО', 'Неизвестно')}<br>"
                    f"<b>Отдел:</b> {self.context_data[0].get('Отдел', 'Неизвестно')}<br>"
                    f"<b>Должность:</b> {self.context_data[0].get('Должность', 'Неизвестно')}")

        if self.context == "group":
            employees_info = "<br>".join(
                f"<b>ФИО:</b> {e['ФИО']} | <b>Отдел:</b> {e['Отдел']} | <b>Должность:</b> {e['Должность']}"
                for e in self.context_data
            )
            return f"Группа сотрудников:<br>{employees_info}"

        if self.context == "department":
            return f"<b>Отдел</b>: {self.context_data}"

        if self.context == "unit":
            return f"<b>Управление</b>: {self.context_data}"

        if self.context == "institute":
            return "Анализ <b>Института</b>"

        return "Анализ данных"

    def plot_data(self):
        """Построение столбчатого графика с задержкой перед отображением предсказанного значения."""
        years = list(self.data.keys())
        results = list(self.data.values())

        if len(years) > 1:
            predicted_year = years[-1]
            predicted_value = results[-1]

            # Убираем последний элемент из первично отображаемых данных
            years = years[:-1]
            results = results[:-1]

            self.ax.bar(years, results)  # Рисуем только фактические данные
            self.canvas.draw()

            # Через 2 секунды добавляем предсказанный результат
            QTimer.singleShot(2000, lambda: self.plot_prediction(predicted_year, predicted_value))
        else:
            self.ax.bar(years, results)
            self.canvas.draw()

    def plot_prediction(self, year, value):
        """Добавляет предсказанный результат после задержки."""
        self.ax.bar([year], [value])
        self.canvas.draw()
