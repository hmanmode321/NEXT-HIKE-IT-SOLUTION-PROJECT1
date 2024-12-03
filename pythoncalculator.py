import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout

def create_buttons(buttons_layout, display):
    buttons = {
        '0': (4, 1),
        '1': (3, 0),
        '2': (3, 1),
        '3': (3, 2),
        '4': (2, 0),
        '5': (2, 1),
        '6': (2, 2),
        '7': (1, 0),
        '8': (1, 1),
        '9': (1, 2),
        '+': (1, 3),
        '-': (2, 3),
        '*': (3, 3),
        '/': (4, 3),
        '=': (4, 2),
        'C': (4, 0),
    }

    for btn_text, pos in buttons.items():
        button = QPushButton(btn_text)
        button.clicked.connect(lambda _, bt=btn_text: on_button_click(bt, display))
        buttons_layout.addWidget(button, pos[0], pos[1])

def on_button_click(sender, display):
    if sender == '=':
        try:
            result = eval(display.text())
            display.setText(str(result))
        except Exception as e:
            display.setText('Error')
    elif sender == 'C':
        display.clear()
    else:
        display.setText(display.text() + sender)

def create_calculator():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle('Calculator')
    window.setGeometry(100, 100, 300, 400)

    central_widget = QWidget(window)
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout(central_widget)

    display = QLineEdit()
    layout.addWidget(display)

    buttons_layout = QGridLayout()
    layout.addLayout(buttons_layout)

    create_buttons(buttons_layout, display)

    window.show()
    sys.exit(app.exec_())

#if _name_ == '_main_':
create_calculator()
