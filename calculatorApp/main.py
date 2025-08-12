# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# App Settings
app = QApplication([])

#Style
app.setStyleSheet("""
QLineEdit {
    background-color: #D3D3D3;
    border-radius: 5px; 
    padding: 20px;
    font-size: 40px;
}
                  """)

main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(550,650)

# All objects/widgets
text_box = QLineEdit()
text_box.setAlignment(Qt.AlignRight)
font = QFont("Courier New Bold", 40)
text_box.setFont(font)
grid = QGridLayout()

buttons = [
  "7", "8", "9", "/", 
  "4", "5", "6", "*", 
  "1", "2", "3", "-",
  "0", ".", "=", "+"]

clear = QPushButton("Clear")
clear.setStyleSheet("""
    QPushButton {
    background-color: #D3D3D3;
    border-radius: 10px;
    padding: 10px;
    font-size: 30px;
    }
    QPushButton:hover {
        background-color: #FFFFE0;
    }
    """)
delete = QPushButton("DEL")
delete.setStyleSheet("""
    QPushButton {
    background-color: #D3D3D3;
    border-radius: 10px;
    padding: 10px;
    font-size: 30px;
    }
    QPushButton:hover {
        background-color: #FFCCCC;
    }
    """)

row = 0
col = 0

for text in buttons:
  button = QPushButton(text)

  button.setStyleSheet("""
    QPushButton {
    background-color: #D3D3D3;
    border-radius: 10px;
    padding: 10px;
    font-size: 30px;
    }
    QPushButton:hover {
        background-color: #ADD8E6;
    }
    """)
  
  try:
    int(text)
  except ValueError:
    button.setStyleSheet("""
            QPushButton {
              background-color: #B3B3B3;
              border-radius: 10px;
              padding: 10px;
              font-size: 30px;
              font-weight: 450;
            }
            QPushButton:hover {
              background-color: #7FB3D5;
            }
        """)

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