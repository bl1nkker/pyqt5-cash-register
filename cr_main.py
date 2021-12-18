from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from cr_cash_register import CashRegister_MainWindow
from cr_sales_report import SalesReport_MainWindow
import json
import sys

# PyQT5
MainScreenForm, MainScreenWindow = uic.loadUiType("a.ui")
JSON_ITEMS = list(json.load(open('cr_items_db.json')))
JSON_SALES = list(json.load(open('cr_sales_db.json')))


def open_sales_report_screen():
    SalesReport_MW = QtWidgets.QMainWindow()
    _ui = SalesReport_MainWindow(JSON_ITEMS, JSON_SALES)
    _ui.setupUi(SalesReport_MW)
    SalesReport_MW.show()


def open_cash_register_screen():
    CashRegister_MW = QtWidgets.QMainWindow()
    ui = CashRegister_MainWindow(JSON_ITEMS, JSON_SALES)
    ui.setupUi(CashRegister_MW)
    CashRegister_MW.show()


app = QApplication([])
main_screen_window = MainScreenWindow()
main_screen_form = MainScreenForm()
main_screen_form.setupUi(main_screen_window)

# Event handlers
main_screen_form.goToCashRegisterButton.clicked.connect(open_cash_register_screen)
main_screen_form.goToReportButton.clicked.connect(open_sales_report_screen)

main_screen_window.show()
app.exec()
