from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from datetime import timedelta, datetime
import json

# PyQT5
Form, Window = uic.loadUiType("dictP_ui.ui")


def open_cash_register_screen():
    pass


def open_sales_report_screen():
    pass


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Event handlers
form.goToCashRegisterButton.clicked.connect(open_cash_register_screen)
form.goToReportButton.clicked.connect(open_sales_report_screen())

window.show()
app.exec()
