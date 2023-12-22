from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGraphicsView,
    QGraphicsScene,
    QPushButton,
    QFileDialog,
    QGraphicsPixmapItem,
)
from PySide6.QtGui import QPixmap, QImage
import fitz


class PDFViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # Create a QGraphicsView to display PDF pages
        self.graphics_view = QGraphicsView(self)
        self.layout.addWidget(self.graphics_view)

        # Create a QGraphicsScene to hold the PDF page
        self.scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.scene)

        # Create a button to open a PDF file
        self.open_button = QPushButton("Open PDF", self)
        self.open_button.clicked.connect(self.open_pdf)
        self.layout.addWidget(self.open_button)

        # Initialize PDF document and page variables
        self.document = None
        self.page = None

    def open_pdf(self):
        # Open a PDF file and load the first page
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getOpenFileName()

        if file_path:
            self.document = fitz.open(file_path)
            self.page = self.document[0]  # Load the first page

            # Render the PDF page to a QPixmap
            pixmap = self.render_page()

            # Display the QPixmap in the QGraphicsView
            self.display_page(pixmap)

    def render_page(self):
        # Render the PDF page to a QPixmap
        image = self.page.get_pixmap(matrix=fitz.Matrix(2, 2))

        qimage = QPixmap.fromImage(
            QImage(
                image.samples,
                image.width,
                image.height,
                image.stride,
                QImage.Format_RGB888,
            )
        )
        return qimage

    def display_page(self, pixmap):
        # Display the QPixmap in the QGraphicsView
        item = QGraphicsPixmapItem(pixmap)
        self.scene.clear()
        self.scene.addItem(item)
        self.graphics_view.setScene(self.scene)
