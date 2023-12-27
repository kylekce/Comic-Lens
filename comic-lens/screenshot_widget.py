from PySide6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import QRect, Qt


class ScreenshotArea(QWidget):
    def __init__(self, pdf_viewer):
        super().__init__()
        self.pdf_viewer = pdf_viewer
        self.start_pos = None
        self.end_pos = None
        self.screenshot = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.start_pos is not None and self.end_pos is not None:
            rect = self.get_rect()
            painter.fillRect(rect, QColor(0, 255, 0, 50))
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        self.start_pos = event.pos()
        self.end_pos = None
        self.screenshot = None
        self.update()

    def mouseMoveEvent(self, event):
        self.end_pos = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end_pos = event.pos()
        self.capture_screenshot()
        self.update()

    def get_rect(self):
        if self.start_pos is not None and self.end_pos is not None:
            return QRect(self.start_pos, self.end_pos).normalized()
        return QRect()

    def reset(self):
        self.start_pos = None
        self.end_pos = None
        self.screenshot = None
        self.update()

    def capture_screenshot(self):
        if self.start_pos is not None and self.end_pos is not None:
            rect = self.get_rect()
            screenshot = QPixmap(rect.size())
            screenshot.fill(Qt.white)

            painter = QPainter(screenshot)
            painter.setRenderHint(QPainter.Antialiasing)

            # Get the global position of the top-left corner of the screenshot area
            global_pos = self.mapToGlobal(rect.topLeft())

            # Capture the content within the selected rectangle from the PDFViewer widget
            source_rect = QRect(
                global_pos - self.pdf_viewer.mapToGlobal(self.pdf_viewer.pos()),
                rect.size(),
            )
            painter.drawPixmap(screenshot.rect(), self.pdf_viewer.grab(source_rect))

            painter.end()
            self.screenshot = screenshot
            self.save_screenshot_to_file()

    def save_screenshot_to_file(self, filename="screenshot.png"):
        if self.screenshot:
            self.screenshot.save(filename, "PNG")

    def get_screenshot(self):
        return self.screenshot
