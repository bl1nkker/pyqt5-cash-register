# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cr_sales_report_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import timedelta, datetime
import json


# Helper functions
def filter_json(till_date, json_sales):
    # Format to python datetime
    start_date = datetime.strptime(till_date, '%m-%d-%Y') - timedelta(days=1)
    end_date = datetime.strptime(till_date, '%m-%d-%Y')
    result_array = []
    for obj in json_sales:
        # Only object, that have date before selected
        if str(end_date) > obj['date'] > str(start_date):
            result_array.append(obj)
    return result_array


class SalesReport_MainWindow(object):
    def __init__(self, json_items, json_sales):
        self.json_items = json_items
        self.json_sales = json_sales

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Calendar Widget
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.show_date_related_data)
        self.verticalLayout_5.addWidget(self.calendarWidget)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout_4.addWidget(self.dateLabel)
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totalLabel.setFont(font)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout_4.addWidget(self.totalLabel)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.itemsList = QtWidgets.QListWidget(self.centralwidget)
        self.itemsList.setObjectName("itemsList")
        self.verticalLayout.addWidget(self.itemsList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.amountList = QtWidgets.QListWidget(self.centralwidget)
        self.amountList.setObjectName("amountList")
        self.verticalLayout_2.addWidget(self.amountList)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.totalList = QtWidgets.QListWidget(self.centralwidget)
        self.totalList.setObjectName("totalList")
        self.verticalLayout_3.addWidget(self.totalList)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(lambda x: self.close_window(MainWindow))
        self.verticalLayout_5.addWidget(self.closeButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_date_related_data(self, q_date):
        # When user clicks -> global variable changes
        till_date = '{0}-{1}-{2}'.format(q_date.month(), q_date.day(), q_date.year())

        # Set label text
        self.dateLabel.setText(f'Date: {till_date}')

        # Get filtered array
        required_data = filter_json(till_date, self.json_sales)

        # Filter unic items
        items_n_amounts = {}
        items_n_totals = {}
        for obj in required_data:
            for item in obj['items']:
                existing_item = next(
                    (x for x in self.json_items if x['id'] == item['id']),
                    None)
                if existing_item['name'] in items_n_amounts:
                    items_n_amounts[existing_item['name']] += item['amount']
                    items_n_totals[existing_item['name']] += item['amount'] * existing_item['price']
                else:
                    items_n_amounts[existing_item['name']] = item['amount']
                    items_n_totals[existing_item['name']] = item['amount'] * existing_item['price']

        # Show filtered data in the table
        self.itemsList.clear()
        self.amountList.clear()
        self.totalList.clear()
        self.itemsList.addItems(list(items_n_amounts.keys()))
        self.amountList.addItems([str(i) for i in list(items_n_amounts.values())])
        self.totalList.addItems([str(i) for i in list(items_n_totals.values())])

        # Set total text label
        self.totalLabel.setText(f'Total: {str(sum([i for i in list(items_n_totals.values())]))}')

    def close_window(self, MainWindow):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateLabel.setText(_translate("MainWindow", "Date:"))
        self.totalLabel.setText(_translate("MainWindow", "Total:"))
        self.label.setText(_translate("MainWindow", "Items"))
        self.label_2.setText(_translate("MainWindow", "Amount"))
        self.label_3.setText(_translate("MainWindow", "Total"))
        self.closeButton.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys

    JSON_ITEMS = list(json.load(open('cr_items_db.json')))
    JSON_SALES = list(json.load(open('cr_sales_db.json')))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SalesReport_MainWindow(JSON_ITEMS, JSON_SALES)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
