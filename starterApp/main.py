# Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# Main App objects
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(500,300)

title_text = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

pratchettWords = [
  "Discworld",
  "Ankh-Morpork",
  "witches",
  "wizards",
  "Librarian",
  "banana",
  "Vimes",
  "Carrot",
  "Lancre",
  "golems",
  "Death",
  "Susan",
  "Granny",
  "Nanny",
  "Rincewind",
  "Luggage",
  "Unseen",
  "Assassins",
  "patrician",
  "moist",
  "clacks",
  "gnomes",
  "trolls",
  "dwarfs",
  "narrativium",
  "humour",
  "satire",
  "magic",
  "chaos",
  "bureaucracy",
  "alchemy",
  "postal",
  "time",
  "gods",
  "belief",
  "philosophy",
  "multiverse",
  "sheep",
  "alchemy",
  "octarine",
  "steam",
  "stamps",
  "monkeys",
  "destiny",
  "feet",
  "boots",
  "scrolls",
  "madness",
  "truth",
  "lies"
]

# Design the app
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Create Functions
def random_word1():
  word = choice(pratchettWords)
  text1.setText(word)

def random_word2():
  word = choice(pratchettWords)
  text2.setText(word)

def random_word3():
  word = choice(pratchettWords)
  text3.setText(word)

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

# Show/Run  our App
main_window.show()
app.exec_()