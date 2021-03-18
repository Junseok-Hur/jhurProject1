from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog, QAction, QMainWindow
from PyQt5.QtGui import QIcon
import school_api
import sys
import os
from pathlib import Path


class Ui_MainWindow(QMainWindow):
    def update_data(self, filename):
        conn, cursor = school_api.open_db("school_db.sqlite")
        school_api.save_excel_db(filename, conn)
        # school_api.setup_db(cursor)
        query = "SELECT * FROM states"
        result = conn.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.commit()
        conn.close()

    def update_file(self):
        # fname = (QFileDialog.getOpenFileName(self, "Choose the file", "", "Excel(*.xls *.xlsx)"))
        # self.update_data(fname)

        file, _ = QFileDialog.getOpenFileName(self, "Choose an excel file", "", "Excel(*.xls *.xlsx)")
        # print(file)
        filename = Path(file).name
        self.update_data(filename)

    def setup_ui(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1401, 1053)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 650, 521))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(10, 540, 111, 41))
        self.btn_update.setObjectName("btn_update")
        self.btn_update.clicked.connect(self.update_file)

        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_update.setText(_translate("MainWindow", "Update"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
