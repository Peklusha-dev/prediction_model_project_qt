from PyQt5 import QtCore, QtWidgets


class UiUnitWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # Надпись "Выбор управления"
        self.label_chose_cust = QtWidgets.QLabel(Form)
        self.label_chose_cust.setObjectName("label_chose_cust")
        self.verticalLayout.addWidget(self.label_chose_cust)

        # Dropdown выбора управления
        self.comboBox_department = QtWidgets.QComboBox(Form)
        self.comboBox_department.setObjectName("comboBox_department")
        self.comboBox_department.setFixedWidth(250)
        self.verticalLayout.addWidget(self.comboBox_department)

        # Кнопка "Выполнить анализ данных"
        self.butt_analize = QtWidgets.QPushButton(Form)
        self.butt_analize.setObjectName("butt_analize")
        self.butt_analize.setFixedWidth(300)
        self.verticalLayout.addWidget(self.butt_analize, alignment=QtCore.Qt.AlignRight)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбор управления"))
        self.label_chose_cust.setText(_translate("Form", "Выбор управления"))
        self.butt_analize.setText(_translate("Form", "Выполнить анализ данных"))
