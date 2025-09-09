import sys
from PySide6.QtWidgets import QApplication
from controllers.main_window_controller import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
    
    print("Application closed")


if __name__ == "__main__":
    main()
