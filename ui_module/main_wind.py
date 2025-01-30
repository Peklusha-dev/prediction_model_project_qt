from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Модель оценки научных сотрудников")
        mainWindow.resize(1200, 1200)  # Фиксированный размер окна
        mainWindow.setMinimumSize(1200, 1200)
        mainWindow.setMaximumSize(1200, 1200)

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Создаем Scroll Area
        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area.setWidgetResizable(True)  # Позволяет масштабировать содержимое
        self.verticalLayout_2.addWidget(self.scroll_area)

        # Внутренний виджет Scroll Area
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_content.setObjectName("scroll_content")
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_layout.setObjectName("scroll_layout")

        # Надпись "Файл не указан"
        self.label_file_path = QtWidgets.QLabel(self.scroll_content)
        self.label_file_path.setObjectName("label_file_path")
        self.scroll_layout.addWidget(self.label_file_path, 0, QtCore.Qt.AlignTop)

        # Кнопка "Загрузить файл"
        self.load_file_button = QtWidgets.QPushButton(self.scroll_content)
        self.load_file_button.setObjectName("load_file_button")
        self.scroll_layout.addWidget(self.load_file_button, 0, QtCore.Qt.AlignTop)

        # Основной контейнер
        self.main_widget = QtWidgets.QWidget(self.scroll_content)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Заголовок
        self.widget_lable_main = QtWidgets.QWidget(self.main_widget)
        self.widget_lable_main.setObjectName("widget_lable_main")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_lable_main)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_main = QtWidgets.QLabel(self.widget_lable_main)
        self.label_main.setObjectName("label_main")
        self.verticalLayout_4.addWidget(self.label_main)
        self.verticalLayout.addWidget(self.widget_lable_main, 0, QtCore.Qt.AlignTop)

        # Разделительная линия
        self.line_up = QtWidgets.QFrame(self.main_widget)
        self.line_up.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_up.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_up.setObjectName("line_up")
        self.verticalLayout.addWidget(self.line_up, 0, QtCore.Qt.AlignTop)

        # Радио-кнопки
        self.widget_with_case_butts = QtWidgets.QWidget(self.main_widget)
        self.widget_with_case_butts.setObjectName("widget_with_case_butts")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_with_case_butts)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.butt_customer = QtWidgets.QRadioButton(self.widget_with_case_butts)
        self.butt_customer.setObjectName("butt_customer")
        self.verticalLayout_3.addWidget(self.butt_customer)

        self.butt_group = QtWidgets.QRadioButton(self.widget_with_case_butts)
        self.butt_group.setObjectName("butt_group")
        self.verticalLayout_3.addWidget(self.butt_group)

        self.butt_department = QtWidgets.QRadioButton(self.widget_with_case_butts)
        self.butt_department.setObjectName("butt_department")
        self.verticalLayout_3.addWidget(self.butt_department)

        self.butt_unit = QtWidgets.QRadioButton(self.widget_with_case_butts)
        self.butt_unit.setObjectName("butt_unit")
        self.verticalLayout_3.addWidget(self.butt_unit)

        self.butt_institute = QtWidgets.QRadioButton(self.widget_with_case_butts)
        self.butt_institute.setObjectName("butt_institute")
        self.verticalLayout_3.addWidget(self.butt_institute)

        self.verticalLayout.addWidget(self.widget_with_case_butts, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # Кнопка "Выбрать"
        self.widget_butt_chose = QtWidgets.QWidget(self.main_widget)
        self.widget_butt_chose.setObjectName("widget_butt_chose")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_butt_chose)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Spacer для выравнивания кнопки вправо
        spacerItem = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.butt_chose = QtWidgets.QPushButton(self.widget_butt_chose)
        self.butt_chose.setObjectName("butt_chose")
        self.horizontalLayout.addWidget(self.butt_chose)

        self.verticalLayout.addWidget(self.widget_butt_chose)

        # Нижняя линия
        self.line_ground = QtWidgets.QFrame(self.main_widget)
        self.line_ground.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ground.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ground.setObjectName("line_ground")
        self.verticalLayout.addWidget(self.line_ground)

        # Заполнитель для прокрутки вниз
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        # Добавляем главный виджет в прокручиваемую область
        self.scroll_layout.addWidget(self.main_widget)
        self.scroll_area.setWidget(self.scroll_content)

        # Устанавливаем центральный виджет
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Модель оценки научных сотрудников"))
        self.load_file_button.setText(_translate("mainWindow", "Загрузить файл"))
        self.label_file_path.setText(_translate("mainWindow", "Файл не указан"))
        self.label_main.setText(_translate("mainWindow", "Выбор объекта исследования"))
        self.butt_customer.setText(_translate("mainWindow", "Сотрудник"))
        self.butt_group.setText(_translate("mainWindow", "Группа сотрудников"))
        self.butt_department.setText(_translate("mainWindow", "Отдел"))
        self.butt_unit.setText(_translate("mainWindow", "Управление"))
        self.butt_institute.setText(_translate("mainWindow", "Институт"))
        self.butt_chose.setText(_translate("mainWindow", "Выбрать"))
