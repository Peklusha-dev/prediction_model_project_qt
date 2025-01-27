from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
import traceback  # Для детального вывода ошибок

from ui_module.main_wind import UiMainWindow
from ui_module.employee_widget import UiEmployeeWidget
from ui_module.graf_wind import GraphWindow
from read_xlsx_module.file_handler import (get_employee_by_fio_department,
                                           get_unique_departments,
                                           get_employees_by_department)
from config import xlsx_path


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.setupUi(self)  # Инициализация интерфейса
            self.current_widget = None  # Ссылка на текущий добавленный виджет
            self.file_path = xlsx_path  # Путь к файлу Excel
            self.butt_chose.clicked.connect(self.handle_choose)

        except Exception as e:
            self.show_error_message("Ошибка при инициализации", e)

    def handle_choose(self):
        """Обрабатываем выбор типа данных для отображения."""
        try:
            if self.current_widget:
                self.main_widget.layout().removeWidget(self.current_widget)
                self.current_widget.deleteLater()
                self.current_widget = None
            elif self.butt_customer.isChecked():
                self.statusBar().showMessage("Вы выбрали: Сотрудник", 5000)
                self.add_employee_widget()
            elif self.butt_group.isChecked():
                self.statusBar().showMessage("Вы выбрали: Группа", 5000)
                self.add_employee_widget()
            elif self.butt_department.isChecked():
                self.statusBar().showMessage("Вы выбрали: Отдел", 5000)
                self.add_department_widget()
            elif self.butt_unit.isChecked():
                self.statusBar().showMessage("Вы выбрали: Управление", 5000)
                self.add_unit_widget()
            elif self.butt_institute.isChecked():
                self.statusBar().showMessage("Вы выбрали: Институт", 5000)
                self.add_institute_widget()
            else:
                self.statusBar().showMessage("Вы ничего не выбрали", 5000)
        except Exception as e:
            self.show_error_message("Ошибка при обработке выбора", e)

    def add_employee_widget(self):
        """Добавляем виджет с выбором сотрудников."""
        try:
            self.current_widget = QWidget()
            self.employee_widget = UiEmployeeWidget()  # Инициализация интерфейса виджета
            self.employee_widget.setupUi(self.current_widget)

            layout = self.main_widget.layout()
            spacer_index = layout.count() - 1
            layout.insertWidget(spacer_index, self.current_widget)

            departments = get_unique_departments(self.file_path)
            self.employee_widget.comboBox_department.addItems(departments)

            self.employee_widget.comboBox_department.currentTextChanged.connect(self.update_fio_list)
            self.update_fio_list(self.employee_widget.comboBox_department.currentText())

            self.employee_widget.comboBox_fio.setEditable(True)
            self.employee_widget.butt_analize.clicked.connect(self.display_candidate_data)

        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Сотрудник>", e)

    def add_group_widget(self):
        """Добавляем виджет с выбором сотрудников для добавления в группу."""
        try:
            print("Добавление виджета <Группа>...")
            pass
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Группа>", e)

    def add_department_widget(self):
        """Добавляем виджет с выбором отдела."""
        try:
            print("Добавление виджета <Отдел>...")
            pass
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Отдел>", e)

    def add_unit_widget(self):
        """Добавляем виджет с выбором управления."""
        try:
            print("Добавление виджета <Управление>...")
            pass
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Управление>", e)

    def add_institute_widget(self):
        """Добавляем текст о том, что выбран анализ по институту."""
        try:
            print("Добавление виджета <Институт>...")
            pass
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Институт>", e)

    def update_fio_list(self, department):
        """Обновляем список сотрудников на основе выбранного отдела."""
        try:
            self.employee_widget.comboBox_fio.blockSignals(True)
            employees = get_employees_by_department(self.file_path, department)
            self.employee_widget.comboBox_fio.clear()
            if employees:
                self.employee_widget.comboBox_fio.addItems(employees)
            self.employee_widget.comboBox_fio.blockSignals(False)
        except Exception as e:
            self.show_error_message("Ошибка при обновлении списка сотрудников", e)


    def display_candidate_data(self):
        try:
            selected_fio = self.employee_widget.comboBox_fio.currentText()
            selected_department = self.employee_widget.comboBox_department.currentText()

            # Получаем данные кандидата
            candidate_data = get_employee_by_fio_department(self.file_path, selected_department, selected_fio)
            print(candidate_data)

            if not candidate_data:
                self.statusBar().showMessage("Нет данных для выбранного сотрудника", 5000)
                return

            # Извлекаем нужную информацию для графика
            graph_data = []
            for result in candidate_data["Результаты"]:
                year = result["Год тестирования"]
                criteria = result["Критерии"]
                total_score = result["Сумма баллов"]

                # Преобразуем данные в формат для графика
                graph_data.append({
                    "Год тестирования": year,
                    "Результаты": total_score
                })

            if not graph_data:
                self.statusBar().showMessage("Нет корректных данных для графика", 5000)
                return

            # Открываем окно с графиком
            position = candidate_data.get("Должность", "Должность неизвестна")
            self.graph_window = GraphWindow(
                data=graph_data,
                fio=selected_fio,
                department=selected_department,
                position=position,
            )
            self.graph_window.show()

        except Exception as e:
            self.show_error_message("Ошибка при отображении данных кандидата", e)

    def show_error_message(self, context, exception):
        """Отображаем сообщение об ошибке."""
        error_message = f"{context}: {str(exception)}"
        self.statusBar().showMessage("Произошла ошибка: " + error_message, 5000)
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText("Произошла ошибка")
        msg_box.setInformativeText(error_message)
        msg_box.setDetailedText(traceback.format_exc())
        msg_box.exec_()
        print(f"Ошибка: {context}")
        print(traceback.format_exc())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("Фатальная ошибка при запуске приложения:")
        print(traceback.format_exc())
