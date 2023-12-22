import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec() # Start the event loop.