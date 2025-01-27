from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWindow(QMainWindow):
    def __init__(self, data=None, fio=None, department=None, position=None):
        """
        Окно для отображения графика анализа данных.
        :param data: Список словарей с данными {'Год тестирования': год, 'Результаты': результат}.
        :param fio: ФИО сотрудника.
        :param department: Отдел сотрудника.
        :param position: Должность сотрудника.
        """
        super().__init__()
        self.setWindowTitle("Результаты анализа")
        self.setGeometry(100, 100, 800, 600)

        self.data = data  # Данные для графика
        self.fio = fio
        self.department = department
        self.position = position

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Информация о сотруднике
        if self.fio and self.department and self.position:
            self.info_label = QLabel(
                f"<b>ФИО:</b> {self.fio}<br>"
                f"<b>Отдел:</b> {self.department}<br>"
                f"<b>Должность:</b> {self.position}"
            )
            self.info_label.setStyleSheet("font-size: 14px; margin-bottom: 10px;")
            layout.addWidget(self.info_label)

        # Создаем холст для matplotlib
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(111)

        # Отображаем данные на графике
        if self.data:
            self.plot_data()

        # Рекомендации
        self.recommendations_label = QLabel("Рекомендуем повторить материал.")
        self.recommendations_label.setStyleSheet(
            "font-size: 12px; margin-top: 10px; color: #555;"
        )
        layout.addWidget(self.recommendations_label)

    def plot_data(self):
        """Рисуем график на основе данных."""
        # Проверяем, что данные содержат "Год тестирования" и "Результаты"
        years = [item["Год тестирования"] for item in self.data]
        results = [float(item["Результаты"]) for item in self.data]

        self.ax.bar(years, results, color="skyblue", label="Результаты")
        self.ax.set_title("Результаты тестирования по годам")
        self.ax.set_xlabel("Год")
        self.ax.set_ylabel("Результаты")
        self.ax.legend()
        self.canvas.draw()
