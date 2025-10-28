import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Mi primera ventana PyQt6")
ventana.resize(400, 300)
ventana.show()

sys.exit(app.exec())
