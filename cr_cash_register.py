# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cr_cash_register_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_MainWindow(object):
    def __init__(self):
        self.is_calculate_pressed = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        # Form Layout
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")

        # Combo Box
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.comboBox.addItems(list(map(lambda item: item['name'], JSON_ITEMS)))
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox)

        # Spin Box
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.verticalLayout_3.addLayout(self.formLayout_2)

        # Add Field Button
        self.addFieldButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFieldButton.setObjectName("addFieldButton")
        self.addFieldButton.clicked.connect(self.add_field)
        self.verticalLayout_3.addWidget(self.addFieldButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
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

        # Items List
        self.itemsList = QtWidgets.QListWidget(self.centralwidget)
        self.itemsList.setObjectName("itemsList")
        self.itemsList.addItems(list(map(lambda item: item['name'], JSON_ITEMS)))
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

        # Prices List
        self.pricesList = QtWidgets.QListWidget(self.centralwidget)
        self.pricesList.setObjectName("pricesList")
        self.pricesList.addItems(list(map(lambda item: str(item['price']), JSON_ITEMS)))
        self.verticalLayout_2.addWidget(self.pricesList)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Calculate Button
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.clicked.connect(lambda x: self.calculate_and_write(MainWindow))
        self.horizontalLayout_2.addWidget(self.calculateButton)

        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        # Total Label
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setObjectName("totalLabel")
        self.horizontalLayout_2.addWidget(self.totalLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Button handler
    def add_field(self):
        current_row = self.formLayout_2.rowCount()
        new_combo_box = QtWidgets.QComboBox(self.centralwidget)
        new_combo_box.addItems(list(map(lambda item: item['name'], JSON_ITEMS)))

        new_spin_box = QtWidgets.QSpinBox(self.centralwidget)
        self.formLayout_2.setWidget(current_row, QtWidgets.QFormLayout.LabelRole,
                                    new_combo_box)
        self.formLayout_2.setWidget(current_row, QtWidgets.QFormLayout.FieldRole,
                                    new_spin_box)

    # Button handler
    def calculate_and_write(self, MainWindow):
        if self.is_calculate_pressed:
            # Redirect to the main screen
            print('Close the screen')
            MainWindow.close()
        else:
            # Set is_calculate_pressed to True
            self.is_calculate_pressed = True

            # Change button text
            self.retranslateUi(MainWindow)

            # Private Variables
            total_price = 0
            items = []

            # Calculate total price + add all items to the list
            for i in range(self.formLayout_2.rowCount()):
                item = next(
                    (x for x in JSON_ITEMS if x['name'] == self.formLayout_2.itemAt(i * 2).widget().currentText()),
                    None)
                total_price += item['price'] * int(self.formLayout_2.itemAt(i * 2 + 1).widget().text())
                items.append({"id": item["id"], "amount": int(self.formLayout_2.itemAt(i * 2 + 1).widget().text())})

            # Create sales instance
            sale_instance = {
                "date": "",
                "items": items,
                "total": total_price
            }

            # Rewrite JSON file
            JSON_SALES.append(sale_instance)
            with open("cr_sales_db.json", "w") as f:
                json.dump(JSON_SALES, f)

            # Set totalLabel text
            self.totalLabel.setText(f'Total price: {total_price}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Choose your items"))
        self.addFieldButton.setText(_translate("MainWindow", "Add field"))
        self.label.setText(_translate("MainWindow", "Available Items"))
        self.label_2.setText(_translate("MainWindow", "Prices"))
        self.calculateButton.setText(_translate("MainWindow", "Close" if self.is_calculate_pressed else 'Buy'))
        self.totalLabel.setText(_translate("MainWindow", "Total price: "))


if __name__ == "__main__":
    import sys

    JSON_ITEMS = list(json.load(open('cr_items_db.json')))
    JSON_SALES = list(json.load(open('cr_sales_db.json')))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
