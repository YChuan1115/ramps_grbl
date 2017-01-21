from Ui_serialportform import Ui_SerialPortWindow

from PyQt5 import  QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SerialPortWindow = QtWidgets.QMainWindow()
    ui = Ui_SerialPortWindow()
    ui.setupUi(SerialPortWindow)
    SerialPortWindow.show()
    sys.exit(app.exec_())
