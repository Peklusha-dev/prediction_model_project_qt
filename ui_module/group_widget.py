from PyQt5 import QtCore, QtWidgets


class UiGroupWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)  # Увеличиваем высоту формы
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # Виджет выбора сотрудников
        self.widget_chose_cust = QtWidgets.QWidget(Form)
        self.widget_chose_cust.setObjectName("widget_chose_cust")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_chose_cust)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Надпись "Выбор сотрудника"
        self.label_chose_cust = QtWidgets.QLabel(self.widget_chose_cust)
        self.label_chose_cust.setObjectName("label_chose_cust")
        self.verticalLayout_2.addWidget(self.label_chose_cust, 0, QtCore.Qt.AlignTop)

        # Поля выбора отдела и должности
        self.widget_with_box = QtWidgets.QWidget(self.widget_chose_cust)
        self.widget_with_box.setObjectName("widget_with_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_with_box)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Dropdown выбора отдела
        self.comboBox_department = QtWidgets.QComboBox(self.widget_with_box)
        self.comboBox_department.setObjectName("comboBox_department")
        self.comboBox_department.setFixedWidth(250)  # Фиксируем ширину
        self.horizontalLayout.addWidget(self.comboBox_department)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        # Отображение должности сотрудника установленного в комбобоксе
        self.label_position = QtWidgets.QLabel(self.widget_with_box)
        self.label_position.setObjectName("label_position")
        self.horizontalLayout.addWidget(self.label_position)

        # Комбобокс поиска сотрудника по ФИО
        self.comboBox_fio = QtWidgets.QComboBox(self.widget_with_box)
        self.comboBox_fio.setObjectName("comboBox_fio")
        self.comboBox_fio.setFixedWidth(250)  # Фиксируем ширину
        self.horizontalLayout.addWidget(self.comboBox_fio)

        self.verticalLayout_2.addWidget(self.widget_with_box, 0, QtCore.Qt.AlignTop)

        # Кнопка "Добавить в группу"
        self.butt_add = QtWidgets.QPushButton("Добавить в группу", self.widget_chose_cust)
        self.butt_add.setObjectName("butt_add")
        self.butt_add.setFixedWidth(300)  # Устанавливаем фиксированную ширину
        self.verticalLayout_2.addWidget(self.butt_add, alignment=QtCore.Qt.AlignRight)

        self.verticalLayout.addWidget(self.widget_chose_cust)

        # Надпись "Выбранные сотрудники (группа)"
        self.label_selected_group = QtWidgets.QLabel(Form)
        self.label_selected_group.setObjectName("label_selected_group")
        self.verticalLayout.addWidget(self.label_selected_group)

        # Таблица с выбранными сотрудниками
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Отдел", "Должность"])
        self.tableWidget.setMinimumHeight(250)  # Увеличиваем минимальную высоту таблицы
        self.verticalLayout.addWidget(self.tableWidget)

        # Кнопка "Выполнить анализ данных"
        self.butt_analize = QtWidgets.QPushButton(self.widget_chose_cust)
        self.butt_analize.setObjectName("butt_analize")
        self.butt_analize.setFixedWidth(300)
        self.verticalLayout.addWidget(self.butt_analize, alignment=QtCore.Qt.AlignRight)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбор группы сотрудников"))
        self.label_chose_cust.setText(_translate("Form", "Выбор сотрудника"))
        self.label_position.setText(_translate("Form", "Должность"))
        self.label_selected_group.setText(_translate("Form", "Выбранные сотрудники (группа)"))
        self.butt_analize.setText(_translate("Form", "Выполнить анализ данных"))
