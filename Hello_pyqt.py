import sys
import pyqt_method as pm

if __name__ == "__main__":
    App = pm.QApplication(sys.argv)
    Root = pm.MainWindow()
    Root.show()
    sys.exit(App.exec())