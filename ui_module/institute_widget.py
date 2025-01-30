from PyQt5 import QtCore, QtWidgets


class UiInstituteWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # Текст "Выбрана функция анализа по Институту"
        self.label_institute_analysis = QtWidgets.QLabel(Form)
        self.label_institute_analysis.setObjectName("label_institute_analysis")
        self.verticalLayout.addWidget(self.label_institute_analysis)

        # Кнопка "Выполнить анализ данных"
        self.butt_analize = QtWidgets.QPushButton(Form)
        self.butt_analize.setObjectName("butt_analize")
        self.butt_analize.setFixedWidth(300)
        self.verticalLayout.addWidget(self.butt_analize, alignment=QtCore.Qt.AlignRight)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Анализ Института"))
        self.label_institute_analysis.setText(_translate("Form", "Выбрана функция анализа по Институту"))
        self.butt_analize.setText(_translate("Form", "Выполнить анализ данных"))
