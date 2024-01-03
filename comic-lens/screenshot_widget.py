from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import QRect, Qt
from ocr import OCR
from translation import Translation


class ScreenshotArea(QWidget):
    def __init__(
        self,
        pdf_viewer,
        input_text_edit,
        output_text_edit,
        input_combo_box,
        output_combo_box,
        screenshot_preview_label,
    ):
        super().__init__()

        # PDFViewer
        self.pdf_viewer = pdf_viewer

        # Screenshot
        self.start_pos = None
        self.end_pos = None
        self.screenshot = None
        self.is_selecting = False
        self.screenshot_preview_label = screenshot_preview_label

        # OCR Parameters
        self.resize_factor = 5
        self.blur_kernel_size = 5

        # Input
        self.input_text = None
        self.ocr_language = None
        self.input_language = None
        self.input_combo_box = input_combo_box
        self.input_text_edit = input_text_edit

        # Output
        self.output_text = None
        self.output_language = None
        self.output_combo_box = output_combo_box
        self.output_text_edit = output_text_edit

        # File
        self.filepath = "screenshot.png"

        # Create an instance of the OCR class
        self.ocr = OCR()

        # Create an instance of the Translation class
        self.translation = Translation()

    def paintEvent(self, event):
        """Draw the screenshot area"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.start_pos is not None and self.end_pos is not None:
            rect = self.get_rect()
            painter.fillRect(rect, QColor(0, 255, 0, 50))
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        """Capture the start position of the mouse"""
        self.start_pos = event.pos()
        self.end_pos = None
        self.screenshot = None
        self.update()

    def mouseMoveEvent(self, event):
        """Capture the end position of the mouse while moving"""
        self.end_pos = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        """Capture the end position of the mouse when released"""
        self.end_pos = event.pos()
        self.capture_screenshot()
        self.update()

    def get_rect(self):
        """Get the rectangle area of the screenshot"""
        if self.start_pos is not None and self.end_pos is not None:
            return QRect(self.start_pos, self.end_pos).normalized()
        return QRect()

    def reset(self):
        """Reset the screenshot area"""
        self.start_pos = None
        self.end_pos = None
        self.screenshot = None
        self.is_selecting = False
        self.update()

    def set_image_preview(self, image_path="preprocessed.png"):
        """Set the image preview in the screenshot_preview_label"""
        pixmap = QPixmap(image_path)
        self.screenshot_preview_label.setPixmap(pixmap.scaledToWidth(200))

    def capture_screenshot(self):
        """Capture the screenshot within the selected rectangle"""
        if self.start_pos is not None and self.end_pos is not None:
            rect = self.get_rect()
            screenshot = QPixmap(rect.size())
            screenshot.fill(Qt.white)

            painter = QPainter(screenshot)
            painter.setRenderHint(QPainter.Antialiasing)

            # Get the global position of the top-left corner of the screenshot area
            global_pos = self.mapToGlobal(rect.topLeft())

            # Convert global position to the PDFViewer's coordinate system
            pdf_viewer_global_pos = self.pdf_viewer.mapFromGlobal(global_pos)

            # Capture the content within the selected rectangle from the PDFViewer widget
            source_rect = QRect(pdf_viewer_global_pos, rect.size())
            painter.drawPixmap(screenshot.rect(), self.pdf_viewer.grab(source_rect))
            painter.end()

            # Save the screenshot
            self.screenshot = screenshot
            self.save_screenshot_to_file()

            self.is_selecting = True

            # Perform Language Update, OCR, and Translation
            self.lang_ocr_translate()

    def save_screenshot_to_file(self):
        """Save the screenshot to file"""
        if self.screenshot:
            self.screenshot.save(self.filepath, "PNG")

    def update_input_language(self, language):
        """Update the language"""
        ocr_language_dict = {
            "Chinese - Simplified": "chi_sim",
            "Chinese - Simplified (Vertical)": "chi_sim_vert",
            "Chinese - Traditional": "chi_tra",
            "Chinese - Traditional (Vertical)": "chi_tra_vert",
            "English": "eng",
            "French": "fra",
            "Indonesian": "ind",
            "Japanese": "jpn",
            "Japanese (Vertical)": "jpn_vert",
            "Korean": "kor",
            "Spanish": "spa",
            "Spanish - Old": "spa_old",
        }
        input_language_dict = {
            "Chinese - Simplified": "zh-cn",
            "Chinese - Simplified (Vertical)": "zh-cn",
            "Chinese - Traditional": "zh-tw",
            "Chinese - Traditional (Vertical)": "zh-tw",
            "English": "en",
            "French": "fr",
            "Indonesian": "id",
            "Japanese": "ja",
            "Japanese (Vertical)": "ja",
            "Korean": "ko",
            "Spanish": "es",
            "Spanish - Old": "es",
        }

        self.ocr_language = ocr_language_dict.get(language)
        self.input_language = input_language_dict.get(language)

    def update_output_language(self, language):
        """Update the language"""
        language_dict = {
            "Chinese - Simplified": "zh-cn",
            "Chinese - Traditional": "zh-tw",
            "English": "en",
            "French": "fr",
            "Indonesian": "id",
            "Japanese": "ja",
            "Korean": "ko",
            "Spanish": "es",
        }

        self.output_language = language_dict.get(language)

    def run_ocr(self):
        """Perform OCR and display the result in the input_text_edit widget"""
        self.input_text = self.ocr.image_to_string(
            image_path=self.filepath,
            language=self.ocr_language,
            resize_factor=self.resize_factor,
            blur_kernel_size=self.blur_kernel_size,
        )
        self.input_text_edit.setText(self.input_text)

        # Set the image preview
        self.set_image_preview()

    def run_translator(self, input_text=None):
        """Perform translation and display the result in the output_text_edit widget"""
        try:
            if input_text:
                self.input_text = input_text

            self.output_text = self.translation.translate_to(
                self.input_text, self.output_language, self.input_language
            )

            # Disable the read only mode
            self.input_text_edit.setReadOnly(False)

            # Set the style sheet
            self.input_text_edit.setStyleSheet("color: #e0d7d2;")

            self.output_text_edit.setText(self.output_text)

        except (TypeError, AttributeError):
            # Enable the read only mode
            self.input_text_edit.setReadOnly(True)

            # Set the style sheet
            self.input_text_edit.setStyleSheet("color: red;")

            self.input_text_edit.setText(
                "Character or text not found in the selection."
            )
            self.output_text_edit.setText("")

        except Exception as e:
            # Set the style sheet
            self.input_text_edit.setStyleSheet("color: red;")

            # Enable the read only mode
            self.input_text_edit.setReadOnly(True)

            self.input_text_edit.setText(f"Something went wrong.\n\n{e}")
            self.output_text_edit.setText("")

    def lang_ocr_translate(self):
        """Call Language Update, OCR, and Translation methods"""
        self.update_input_language(self.input_combo_box.currentText())
        self.update_output_language(self.output_combo_box.currentText())

        # If the screenshot selection is active, perform OCR and Translation
        if self.is_selecting:
            self.run_ocr()
            self.run_translator()

    def resize_factor_changed(self, value):
        """Update the resize factor"""
        self.resize_factor = value
        self.capture_screenshot()

    def blur_kernel_size_changed(self, value):
        """Update the blur kernel size"""
        self.blur_kernel_size = value
        self.capture_screenshot()
