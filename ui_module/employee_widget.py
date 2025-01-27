from PyQt5 import QtCore, QtGui, QtWidgets


class UiEmployeeWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_chose_cust = QtWidgets.QWidget(Form)
        self.widget_chose_cust.setObjectName("widget_chose_cust")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_chose_cust)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_chose_cust = QtWidgets.QLabel(self.widget_chose_cust)
        self.label_chose_cust.setObjectName("label_chose_cust")
        self.verticalLayout_2.addWidget(self.label_chose_cust, 0, QtCore.Qt.AlignTop)
        self.widget_with_box = QtWidgets.QWidget(self.widget_chose_cust)
        self.widget_with_box.setObjectName("widget_with_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_with_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_department = QtWidgets.QComboBox(self.widget_with_box)
        self.comboBox_department.setObjectName("comboBox_department")
        self.horizontalLayout.addWidget(self.comboBox_department)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lable_position = QtWidgets.QLabel(self.widget_with_box)
        self.lable_position.setObjectName("lable_position")
        self.horizontalLayout.addWidget(self.lable_position)
        self.comboBox_fio = QtWidgets.QComboBox(self.widget_with_box)
        self.comboBox_fio.setObjectName("comboBox_fio")
        self.horizontalLayout.addWidget(self.comboBox_fio)
        self.verticalLayout_2.addWidget(self.widget_with_box, 0, QtCore.Qt.AlignTop)
        self.butt_analize = QtWidgets.QPushButton(self.widget_chose_cust)
        self.butt_analize.setObjectName("butt_analize")
        self.verticalLayout_2.addWidget(self.butt_analize)
        self.verticalLayout.addWidget(self.widget_chose_cust)
        self.comboBox_department.setFixedWidth(200)  # Устанавливаем фиксированную ширину
        self.comboBox_fio.setFixedWidth(200)  # Устанавливаем фиксированную ширину
        self.butt_analize.setFixedWidth(300)
        self.verticalLayout_2.addWidget(self.butt_analize, alignment=QtCore.Qt.AlignRight)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_chose_cust.setText(_translate("Form", "Выбор сотрудника"))
        self.lable_position.setText(_translate("Form", "Должность"))
        self.butt_analize.setText(_translate("Form", "Выполнить анализ данных"))


