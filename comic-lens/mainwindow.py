# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QDesktopServices

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

        # Set the initial window state to maximized
        self.setWindowState(self.windowState() | Qt.WindowMaximized)

        # Get the path to the directory of the current script
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Set the path to the stylesheet
        stylesheet_path = os.path.join(script_dir, "stylesheet.qss")

        # Check if the stylesheet file exists before opening it
        if os.path.isfile(stylesheet_path):
            with open(stylesheet_path) as f:
                self.setStyleSheet(f.read())

        # Create an instance of the PDFViewer class
        self.pdf_viewer = PDFViewer()
        self.page_layout.addWidget(self.pdf_viewer)

        # Create an instance of the ScreenshotArea class
        self.screenshot_area = ScreenshotArea(
            self.pdf_viewer,
            self.input_text_edit,
            self.output_text_edit,
            self.input_combo_box,
            self.output_combo_box,
            self.screenshot_preview_label,
        )

        # If the input_combo_box is changed, rerun the screenshot_area.lang_ocr_translate method
        self.input_combo_box.currentTextChanged.connect(
            self.screenshot_area.lang_ocr_translate
        )
        self.output_combo_box.currentTextChanged.connect(
            self.screenshot_area.lang_ocr_translate
        )

        # File
        self.actionOpen_PDF.triggered.connect(
            lambda: self.pdf_viewer.open_pdf(
                self.current_file_label, self.page_label, self.page_spin_box
            )
        )

        # View
        self.actionZoom_In.triggered.connect(self.zoom_in_event)
        self.actionZoom_Out.triggered.connect(self.zoom_out_event)
        self.actionFit.triggered.connect(self.fit_event)

        self.zoom_out.clicked.connect(self.zoom_out_event)
        self.zoom_in.clicked.connect(self.zoom_in_event)
        self.fit.clicked.connect(self.fit_event)

        # About
        self.actionDocumentation.triggered.connect(self.open_link)

        # Page Navigation
        self.actionNext_Page.triggered.connect(self.next_page_event)
        self.actionPrevious_Page.triggered.connect(self.previous_page_event)
        self.actionStart_Page.triggered.connect(self.start_page_event)
        self.actionLast_Page.triggered.connect(self.last_page_event)

        self.next_page.clicked.connect(self.next_page_event)
        self.previous_page.clicked.connect(self.previous_page_event)
        self.start_page.clicked.connect(self.start_page_event)
        self.last_page.clicked.connect(self.last_page_event)

        self.page_spin_box.lineEdit().returnPressed.connect(self.page_spin_box_changed)

        # Screenshot toggle
        self.box_screenshot.toggled.connect(self.box_screenshot_toggled)

        # Translate button
        self.translate_button.clicked.connect(
            lambda: self.screenshot_area.run_translator(
                self.input_text_edit.toPlainText()
            )
        )

        # Resize factor
        self.resize_factor_slider.sliderReleased.connect(
            self.resize_factor_slider_changed
        )
        self.resize_factor_box.lineEdit().returnPressed.connect(
            self.resize_factor_box_changed
        )

        # Median blur
        self.median_blur_slider.sliderReleased.connect(self.median_blur_slider_changed)
        self.median_blur_box.lineEdit().returnPressed.connect(
            self.median_blur_box_changed
        )

    def box_screenshot_toggled(self, checked):
        """If the box is checked, replace the PDFViewer widget with the ScreenshotArea widget"""
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

    def disable_screenshot_box(self):
        """Disable the screenshot box"""
        if self.box_screenshot.isChecked():
            self.screenshot_area.reset()
            self.box_screenshot.setChecked(False)
            self.actionBox_Screenshot.setChecked(False)

    def resizeEvent(self, event):
        """If window is resized, call the disable_screenshot_box method"""
        self.disable_screenshot_box()

    def zoom_in_event(self):
        """Connect the zoom in action to the zoom in method"""
        self.pdf_viewer.zoom_in()
        self.disable_screenshot_box()

    def zoom_out_event(self):
        """Connect the zoom out action to the zoom out method"""
        self.pdf_viewer.zoom_out()
        self.disable_screenshot_box()

    def fit_event(self):
        """Connect the fit action to the fit method"""
        self.pdf_viewer.fit()
        self.disable_screenshot_box()

    def next_page_event(self):
        """Connect the next page action to the next page method"""
        self.pdf_viewer.next_page(self.page_spin_box)
        self.screenshot_area.reset()

    def previous_page_event(self):
        """Connect the previous page action to the previous page method"""
        self.pdf_viewer.previous_page(self.page_spin_box)
        self.screenshot_area.reset()

    def start_page_event(self):
        """Connect the start page action to the start page method"""
        self.pdf_viewer.start_page(self.page_spin_box)
        self.screenshot_area.reset()

    def last_page_event(self):
        """Connect the last page action to the last page method"""
        self.pdf_viewer.last_page(self.page_spin_box)
        self.screenshot_area.reset()

    def page_spin_box_changed(self):
        """Connect the page line edit return pressed event to the page line edit return pressed method"""
        self.pdf_viewer.page_line_edit_return_pressed(int(self.page_spin_box.value()))
        self.screenshot_area.reset()

    def resize_factor_slider_changed(self):
        """Set the resize factor box value to the slider value"""
        self.resize_factor_box.setValue(self.resize_factor_slider.value())
        self.screenshot_area.resize_factor_changed(self.resize_factor_slider.value())

    def resize_factor_box_changed(self):
        """Set the resize factor slider value to the box value"""
        self.resize_factor_slider.setValue(self.resize_factor_box.value())
        self.screenshot_area.resize_factor_changed(self.resize_factor_box.value())

    def median_blur_slider_changed(self):
        """Set the median blur box value to the slider value"""
        self.median_blur_box.setValue(self.median_blur_slider.value())
        self.screenshot_area.blur_kernel_size_changed(self.median_blur_slider.value())

    def median_blur_box_changed(self):
        """Set the median blur slider value to the box value"""
        self.median_blur_slider.setValue(self.median_blur_box.value())
        self.screenshot_area.blur_kernel_size_changed(self.median_blur_box.value())

    def open_link(self):
        """Open the link in the default web browser"""
        QDesktopServices.openUrl(QUrl("https://github.com/kylekce/Comic-Lens"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the application style to the default system style
    app.setStyle("Fusion")

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
