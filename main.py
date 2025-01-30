from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
import sys
import traceback  # Для детального вывода ошибок

from ui_module.main_wind import UiMainWindow
from ui_module.employee_widget import UiEmployeeWidget
from ui_module.group_widget import UiGroupWidget
from ui_module.department_widget import UiDepartmentWidget
from ui_module.unit_widget import UiUnitWidget
from ui_module.institute_widget import UiInstituteWidget
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
            self.file_path = None  # Путь к файлу Excel
            self.data_buff = []

            self.load_file_button.clicked.connect(self.load_file)
            self.butt_chose.clicked.connect(self.handle_choose)

        except Exception as e:
            self.show_error_message("Ошибка при инициализации", e)

    def load_file(self):
        """Открывает диалог выбора файла и сохраняет путь"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите xlsx-файл", "", "XLSX Files (*.xlsx);;All Files (*)")
        if file_path:
            self.file_path = file_path  # Сохраняем путь к файлу
            self.label_file_path.setText(f"Выбран файл:\n{file_path}")  # Обновляем текст

    def handle_choose(self):
        """Обрабатываем выбор типа данных для отображения."""
        try:
            if self.current_widget:
                self.main_widget.layout().removeWidget(self.current_widget)
                self.current_widget.deleteLater()
                self.current_widget = None

            if self.butt_customer.isChecked():
                self.statusBar().showMessage("Вы выбрали: Сотрудник", 5000)
                self.add_employee_widget()
            elif self.butt_group.isChecked():
                self.statusBar().showMessage("Вы выбрали: Группа", 5000)
                self.add_group_widget()
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
            # Обновление информации о должности сотрудника выбранного в комбобоксе
            self.employee_widget.comboBox_fio.currentTextChanged.connect(self.update_employee_position)
            self.update_fio_list(self.employee_widget.comboBox_department.currentText())

            self.employee_widget.comboBox_fio.setEditable(True)
            self.employee_widget.butt_analize.clicked.connect(self.display_candidate_data)

        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Сотрудник>", e)

    def add_group_widget(self):
        """Добавляем виджет с выбором сотрудников для добавления в группу."""
        try:
            self.current_widget = QWidget()
            self.group_widget = UiGroupWidget()
            self.group_widget.setupUi(self.current_widget)

            layout = self.main_widget.layout()
            spacer_index = layout.count() - 1
            layout.insertWidget(spacer_index, self.current_widget)

            departments = get_unique_departments(self.file_path)
            self.group_widget.comboBox_department.addItems(departments)

            self.group_widget.comboBox_department.currentTextChanged.connect(self.update_group_fio_list)
            self.group_widget.comboBox_fio.currentTextChanged.connect(self.update_group_employee_position)
            self.update_group_fio_list(self.group_widget.comboBox_department.currentText())

            self.group_widget.comboBox_fio.setEditable(True)

            self.group_widget.butt_add.clicked.connect(self.add_to_group)
            self.group_widget.butt_analize.clicked.connect(self.display_group_data)

        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Группа>", e)

    def add_department_widget(self):
        """Добавляем виджет с выбором отдела."""
        try:
            self.current_widget = QWidget()
            self.department_widget = UiDepartmentWidget()
            self.department_widget.setupUi(self.current_widget)

            layout = self.main_widget.layout()
            spacer_index = layout.count() - 1
            layout.insertWidget(spacer_index, self.current_widget)

            departments = get_unique_departments(self.file_path)
            self.department_widget.comboBox_department.addItems(departments)

            self.department_widget.butt_analize.clicked.connect(self.display_department_data)
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Отдел>", e)

    def add_unit_widget(self):
        """Добавляем виджет с выбором управления."""
        try:
            self.current_widget = QWidget()
            self.unit_widget = UiUnitWidget()
            self.unit_widget.setupUi(self.current_widget)

            layout = self.main_widget.layout()
            spacer_index = layout.count() - 1
            layout.insertWidget(spacer_index, self.current_widget)

            units = ["Управление 1", "Управление 2", "Управление 3"]  # Пока моковые
            self.unit_widget.comboBox_department.addItems(units)

            self.unit_widget.butt_analize.clicked.connect(self.display_unit_data)
        except Exception as e:
            self.show_error_message("Ошибка при добавлении виджета <Управление>", e)

    def add_institute_widget(self):
        """Добавляем текст о том, что выбран анализ по институту."""
        try:
            self.current_widget = QWidget()
            self.institute_widget = UiInstituteWidget()
            self.institute_widget.setupUi(self.current_widget)

            layout = self.main_widget.layout()
            spacer_index = layout.count() - 1
            layout.insertWidget(spacer_index, self.current_widget)

            self.institute_widget.butt_analize.clicked.connect(self.display_institute_data)
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
            # После обновления списка сотрудников сразу обновляем должность
            self.update_employee_position()
        except Exception as e:
            self.show_error_message("Ошибка при обновлении списка сотрудников", e)

    def update_group_fio_list(self, department):
        """Обновляем список сотрудников для выбора группы."""
        try:
            self.group_widget.comboBox_fio.blockSignals(True)
            employees = get_employees_by_department(self.file_path, department)
            self.group_widget.comboBox_fio.clear()
            if employees:
                self.group_widget.comboBox_fio.addItems(employees)
            self.group_widget.comboBox_fio.blockSignals(False)
            # После обновления списка сразу обновляем должность
            self.update_group_employee_position()
        except Exception as e:
            self.show_error_message("Ошибка при обновлении списка сотрудников", e)

    def update_employee_position(self):
        """Обновление должности для выбираемого сотрудника."""
        try:
            selected_fio = self.employee_widget.comboBox_fio.currentText()
            selected_department = self.employee_widget.comboBox_department.currentText()
            if not selected_fio or not selected_department:
                self.employee_widget.label_position.setText("Должность: неизвестна")
                return

            candidate_data = get_employee_by_fio_department(self.file_path, selected_department, selected_fio)
            if candidate_data and "Должность" in candidate_data:
                position = candidate_data["Должность"]
                self.employee_widget.label_position.setText(f"Должность: {position}")
            else:
                self.employee_widget.label_position.setText("Должность: неизвестна")
        except Exception as e:
            self.show_error_message("Ошибка при обновлении должности сотрудника", e)

    def update_group_employee_position(self):
        """Обновление должности для выбираемого в группу сотрудника."""
        try:
            selected_fio = self.group_widget.comboBox_fio.currentText()
            selected_department = self.group_widget.comboBox_department.currentText()

            if not selected_fio or not selected_department:
                self.group_widget.label_position.setText("Должность: неизвестна")
                return

            candidate_data = get_employee_by_fio_department(self.file_path, selected_department, selected_fio)
            if candidate_data and "Должность" in candidate_data:
                position = candidate_data["Должность"]
                self.group_widget.label_position.setText(f"Должность: {position}")
            else:
                self.group_widget.label_position.setText("Должность: неизвестна")
        except Exception as e:
            self.show_error_message("Ошибка при обновлении должности сотрудника в группе", e)

    def add_to_group(self):
        """Добавляем выбранного сотрудника в таблицу группы."""
        try:
            selected_fio = self.group_widget.comboBox_fio.currentText()
            selected_department = self.group_widget.comboBox_department.currentText()
            if not selected_fio or not selected_department:
                self.statusBar().showMessage("Не выбраны ФИО или отдел", 5000)
                return

            # Проверяем дублирование
            for row in range(self.group_widget.tableWidget.rowCount()):
                if self.group_widget.tableWidget.item(row, 0).text() == selected_fio:
                    self.statusBar().showMessage("Сотрудник уже добавлен в группу", 5000)
                    return

            # Получаем данные сотрудника
            candidate_data = get_employee_by_fio_department(self.file_path, selected_department, selected_fio)
            position = candidate_data["Должность"] if candidate_data else "Должность неизвестна"

            # Добавляем сотрудника в таблицу
            row_count = self.group_widget.tableWidget.rowCount()
            self.group_widget.tableWidget.insertRow(row_count)
            self.group_widget.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(selected_fio))
            self.group_widget.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(selected_department))
            self.group_widget.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(position))
        except Exception as e:
            self.show_error_message("Ошибка при добавлении сотрудника в группу", e)

    def display_candidate_data(self):
        try:
            user_data = []
            selected_fio = self.employee_widget.comboBox_fio.currentText()
            selected_department = self.employee_widget.comboBox_department.currentText()

            # Получаем данные сотрудника
            candidate_data = get_employee_by_fio_department(self.file_path, selected_department, selected_fio)

            if not candidate_data:
                self.statusBar().showMessage("Нет данных для выбранного сотрудника", 5000)
                return

            # Моки для проверки отрисовки
            graph_data = {
                2020: 75,
                2021: 80,
                2022: 85,
                2023: 90,
                2024: 88,
                2025: 100  # Предсказанный результат
            }

            # Открываем окно с графиком
            position = candidate_data.get("Должность", "Должность неизвестна")
            user_data.append({"ФИО": selected_fio, "Отдел": selected_department, "Должность": position})
            self.graph_window = GraphWindow(
                data=graph_data,
                context='employee',
                context_data=user_data,
            )
            self.graph_window.show()

        except Exception as e:
            self.show_error_message("Ошибка при отображении данных кандидата", e)

    def display_group_data(self):
        """Показываем данные выбранной группы."""
        try:
            row_count = self.group_widget.tableWidget.rowCount()
            if row_count == 0:
                self.statusBar().showMessage("Группа пуста", 5000)
                return

            # Получаем данные группы сотрудников
            group_data = []
            for row in range(row_count):
                fio = self.group_widget.tableWidget.item(row, 0).text()
                department = self.group_widget.tableWidget.item(row, 1).text()
                position = self.group_widget.tableWidget.item(row, 2).text()  # Должность

                group_data.append({"ФИО": fio, "Отдел": department, "Должность": position})

            # Открываем окно с графиком
            self.graph_window = GraphWindow(
                data=None,
                context='group',
                context_data=group_data,
            )
            self.graph_window.show()
        except Exception as e:
            self.show_error_message("Ошибка при анализе данных группы", e)

    def display_department_data(self):
        """Показываем данные выбранного отдела."""
        try:
            selected_department = self.department_widget.comboBox_department.currentText()
            if not selected_department:
                self.statusBar().showMessage("Выберите отдел для анализа", 5000)
                return

            # Открываем окно с графиком
            self.graph_window = GraphWindow(
                data=None,
                context='department',
                context_data=selected_department,
            )
            self.graph_window.show()
        except Exception as e:
            self.show_error_message("Ошибка при анализе данных отдела", e)

    def display_unit_data(self):
        """Показываем данные выбранного управления."""
        try:
            selected_unit = self.unit_widget.comboBox_department.currentText()
            if not selected_unit:
                self.statusBar().showMessage("Выберите управление для анализа", 5000)
                return

            # Открываем окно с графиком
            self.graph_window = GraphWindow(
                data=None,
                context='unit',
                context_data=selected_unit,
            )
            self.graph_window.show()
        except Exception as e:
            self.show_error_message("Ошибка при анализе данных управления", e)

    def display_institute_data(self):
        """Показываем данные по институту."""
        try:
            # Открываем окно с графиком
            self.graph_window = GraphWindow(
                data=None,
                context='institute',
            )
            self.graph_window.show()
        except Exception as e:
            self.show_error_message("Ошибка при анализе данных института", e)

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
