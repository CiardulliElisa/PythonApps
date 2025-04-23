# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(550,650)

# All objects/widgets
text_box = QLineEdit()
grid = QGridLayout()

buttons = [
  "7", "8", "9", "/", 
  "4", "5", "6", "*", 
  "1", "2", "3", "-",
  "0", ".", "=", "+"]

clear = QPushButton("Clear")
delete = QPushButton("DEL")

row = 0
col = 0

for text in buttons:
  button = QPushButton(text)
  #button.clicked.connect(None)
  grid.addWidget(button, row, col)
  col += 1

  if col > 3:
    col = 0
    row += 1

# Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

#Show/Run
main_window.show()
app.exec_()