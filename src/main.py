import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    app.exec()
    
    print("Application closed")


if __name__ == "__main__":
    main()
