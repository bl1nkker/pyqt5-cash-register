from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from cr_cash_register import CashRegister_MainWindow
import json
import sys

# PyQT5
MainScreenForm, MainScreenWindow = uic.loadUiType("a.ui")


def open_cash_register_screen():
    JSON_ITEMS = list(json.load(open('cr_items_db.json')))
    JSON_SALES = list(json.load(open('cr_sales_db.json')))
    CashRegister_MW = QtWidgets.QMainWindow()
    ui = CashRegister_MainWindow(JSON_ITEMS, JSON_SALES)
    ui.setupUi(CashRegister_MW)
    CashRegister_MW.show()


def open_sales_report_screen():
    pass


app = QApplication([])
main_screen_window = MainScreenWindow()
main_screen_form = MainScreenForm()
main_screen_form.setupUi(main_screen_window)

# Event handlers
main_screen_form.goToCashRegisterButton.clicked.connect(open_cash_register_screen)
# main_screen_form.goToReportButton.clicked.connect(open_sales_report_screen())

main_screen_window.show()
app.exec()
