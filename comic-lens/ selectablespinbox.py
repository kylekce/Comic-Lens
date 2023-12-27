from PySide6.QtWidgets import QApplication, QSpinBox, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys


class SelectableSpinBox(QSpinBox):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.selectAll()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Create an instance of the SelectableSpinBox
        selectable_spinbox = SelectableSpinBox(self)
        layout.addWidget(selectable_spinbox)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
