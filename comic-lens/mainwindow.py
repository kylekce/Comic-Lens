# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from pdf_viewer_widget import PDFViewer
from screenshot_widget import ScreenshotArea


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Create an instance of the PDFViewer class
        self.pdf_viewer = PDFViewer()
        self.page_layout.addWidget(self.pdf_viewer)

        # Create an instance of the ScreenshotArea class
        self.screenshot_area = ScreenshotArea(self.pdf_viewer)

        # Action Buttons
        # File
        self.actionOpen_PDF.triggered.connect(
            lambda: self.pdf_viewer.open_pdf(
                self.current_file_label, self.page_label, self.page_line_edit
            )
        )
        # Page
        self.actionNext_Page.triggered.connect(self.pdf_viewer.next_page)
        self.actionPrevious_Page.triggered.connect(self.pdf_viewer.previous_page)
        self.actionStart_Page.triggered.connect(self.pdf_viewer.start_page)
        self.actionLast_Page.triggered.connect(self.pdf_viewer.last_page)
        # View
        self.actionZoom_In.triggered.connect(self.pdf_viewer.zoom_in)
        self.actionZoom_Out.triggered.connect(self.pdf_viewer.zoom_out)
        self.actionFit.triggered.connect(self.pdf_viewer.fit)
        # Translation
        self.actionBox_Screenshot.toggled.connect(self.box_screenshot_toggled)

        # Tool Buttons
        # Page Navigation
        self.next_page.clicked.connect(
            lambda: self.pdf_viewer.next_page(self.page_line_edit)
        )
        self.previous_page.clicked.connect(
            lambda: self.pdf_viewer.previous_page(self.page_line_edit)
        )
        self.start_page.clicked.connect(
            lambda: self.pdf_viewer.start_page(self.page_line_edit)
        )
        self.last_page.clicked.connect(
            lambda: self.pdf_viewer.last_page(self.page_line_edit)
        )
        self.page_line_edit.returnPressed.connect(
            lambda: self.pdf_viewer.page_line_edit_return_pressed(
                int(self.page_line_edit.text())
            )
        )
        # Zoom
        self.zoom_out.clicked.connect(self.pdf_viewer.zoom_out)
        self.zoom_in.clicked.connect(self.pdf_viewer.zoom_in)
        self.fit.clicked.connect(self.pdf_viewer.fit)
        # Screenshot
        self.box_screenshot.toggled.connect(self.box_screenshot_toggled)

    def box_screenshot_toggled(self, checked):
        if checked:
            self.box_screenshot.setChecked(True)
            self.actionBox_Screenshot.setChecked(True)
            self.page_layout.replaceWidget(self.pdf_viewer, self.screenshot_area)
            self.screenshot_area.show()
        else:
            self.box_screenshot.setChecked(False)
            self.actionBox_Screenshot.setChecked(False)
            self.screenshot_area.reset()
            self.page_layout.replaceWidget(self.screenshot_area, self.pdf_viewer)
            self.screenshot_area.hide()

    # If window is resized, disable the screenshot box
    def resizeEvent(self, event):
        if self.box_screenshot.isChecked():
            self.screenshot_area.reset()
            self.box_screenshot.setChecked(False)
            self.actionBox_Screenshot.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
