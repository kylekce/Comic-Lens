from PySide6.QtCore import Qt, QFileInfo, QDir
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGraphicsView,
    QGraphicsScene,
    QFileDialog,
    QGraphicsPixmapItem,
)
from PySide6.QtGui import QPixmap, QImage, QPainter
import fitz


class PDFViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # Create a QGraphicsView to display PDF pages
        self.graphics_view = QGraphicsView(self)
        self.layout.addWidget(self.graphics_view)

        # Set the style sheet
        self.graphics_view.setStyleSheet("border: none; background-color: #343434")

        # Create a QGraphicsScene to hold the PDF page
        self.scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.scene)

        # Initialize PDF document and page variables
        self.document = None
        self.page = None

    def open_pdf(self, current_file_label, page_label, page_line_edit):
        """Open a PDF file and load the first page"""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("PDF files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.Detail)

        # Set the initial directory to the user's home directory
        file_dialog.setDirectory(QDir.homePath())

        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                self.document = fitz.open(file_path)
                self.page = self.document[0]  # Load the first page

                # Render the PDF page to a QPixmap
                pixmap = self.render_page()

                # Display the QPixmap in the QGraphicsView
                self.display_page(pixmap)

                # Update the current file label with the name of the PDF file
                file_name = QFileInfo(file_path).fileName().split(".")[0]
                current_file_label.setText(file_name)

                # Update the page label with the total number of pages
                page_label.setText(f"of {self.document.page_count}")

                # Update the page line edit
                self.change_page_line_edit(page_line_edit)

                return True

        # If a PDF file already exists
        if self.document:
            return True

        # Remove the widget from the layout if the PDF file fails to open
        self.layout.removeWidget(self.graphics_view)

        return False

    def render_page(self):
        """Render the PDF page to a QPixmap with improved rendering quality"""
        image = self.page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=True)

        # Convert the fitz pixmap to a QImage
        qimage = QImage(
            image.samples,
            image.width,
            image.height,
            image.stride,
            QImage.Format_RGBA8888,  # Use RGBA format for alpha channel
        )

        # Set the DPI
        dpi = 350
        qimage.setDotsPerMeterX(dpi * 100 / 2.54)
        qimage.setDotsPerMeterY(dpi * 100 / 2.54)

        # Convert the QImage to a QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # Create a painter and enable anti-aliasing
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the image on the pixmap
        painter.drawImage(0, 0, qimage)

        # End the painting
        painter.end()

        return pixmap

    def display_page(self, pixmap):
        """Display the QPixmap in the QGraphicsView"""
        item = QGraphicsPixmapItem(pixmap)
        self.scene.clear()
        self.scene.addItem(item)
        self.graphics_view.setScene(self.scene)

        # Fit the PDF page to the QGraphicsView height
        self.fit()

    def zoom_in(self):
        """Zoom in by 10%"""
        self.graphics_view.scale(1.1, 1.1)

    def zoom_out(self):
        """Zoom out by 10%"""
        self.graphics_view.scale(0.9, 0.9)

    def fit(self):
        """Fit the PDF page to the QGraphicsView"""
        scene_rect = self.scene.itemsBoundingRect()
        self.graphics_view.setSceneRect(scene_rect)
        self.graphics_view.fitInView(scene_rect, Qt.KeepAspectRatio)

    def next_page(self, line_edit):
        """Go to the next page"""
        try:
            if self.page.number + 1 < self.document.page_count:
                self.page = self.document[self.page.number + 1]
                pixmap = self.render_page()
                self.display_page(pixmap)

            # Update the page line edit
            self.change_page_line_edit(line_edit)
        except AttributeError:
            pass

    def previous_page(self, line_edit):
        """Go to the previous page"""
        try:
            if self.page.number > 0:
                self.page = self.document[self.page.number - 1]
                pixmap = self.render_page()
                self.display_page(pixmap)

            # Update the page line edit
            self.change_page_line_edit(line_edit)
        except AttributeError:
            pass

    def start_page(self, line_edit):
        """Go to the start page"""
        try:
            self.page = self.document[0]
            pixmap = self.render_page()
            self.display_page(pixmap)

            # Update the page line edit
            self.change_page_line_edit(line_edit)
        except (AttributeError, TypeError):
            pass

    def last_page(self, line_edit):
        """Go to the last page"""
        try:
            self.page = self.document[self.document.page_count - 1]
            pixmap = self.render_page()
            self.display_page(pixmap)

            # Update the page line edit
            self.change_page_line_edit(line_edit)
        except AttributeError:
            pass

    def page_line_edit_return_pressed(self, page_number):
        """Go to the page number entered in the line edit"""
        if page_number > 0 and page_number <= self.document.page_count:
            self.page = self.document[page_number - 1]
            pixmap = self.render_page()
            self.display_page(pixmap)

        # Remove focus from the line edit
        self.focusNextChild()

    def change_page_line_edit(self, line_edit):
        """Change page number entered in the line edit"""
        line_edit.setValue(self.page.number + 1)
