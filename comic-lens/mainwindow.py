# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from pdf_viewer import PDFViewer


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create an instance of the PDFViewer class
        self.pdf_viewer = PDFViewer()

        # Add the PDFViewer widget to the central widget of the main window
        self.ui.horizontalLayout_2.addWidget(self.pdf_viewer)

        # Create a button to open a PDF file
        open_button = QPushButton("Open PDF", self)
        open_button.clicked.connect(self.pdf_viewer.open_pdf)
        self.ui.verticalLayout.addWidget(open_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
