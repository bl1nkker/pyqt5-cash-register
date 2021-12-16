from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from datetime import timedelta, datetime
import json

# PyQT5
MainScreenForm, MainScreenWindow = uic.loadUiType("a.ui")


def open_cash_register_screen():
    pass


def open_sales_report_screen():
    pass


app = QApplication([])
main_screen_window = MainScreenWindow()
main_screen_form = MainScreenForm()
main_screen_form.setupUi(main_screen_window)

# Event handlers
# main_screen_form.goToCashRegisterButton.clicked.connect(open_cash_register_screen)
# main_screen_form.goToReportButton.clicked.connect(open_sales_report_screen())

main_screen_window.show()
app.exec()
