from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from datetime import timedelta, datetime
import json


def retrieve_data(filename, sep):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().split(sep)
    return lines


# Constants
WORDS = retrieve_data('dictP_words.txt', ',')
DEFINITIONS = retrieve_data('dictP_defs.txt', '\n\n')


def find_suggestions():
    # Trim data
    suggestions: list = []
    i_word: str = form.lineEdit.text().lower()

    # Find suggestions
    for i in range(len(i_word)):
        for word in WORDS:
            if i_word[:len(i_word) - i] in word.lower():
                # suggestions.append(word)
                suggestions.append(DEFINITIONS[WORDS.index(word)])
        if len(suggestions) != 0:
            break

    # Set label text to first suggestion:

    definition_to_display = suggestions[0] if len(suggestions) != 0 else 'This word doesnt exist in my universe'
    form.suggestionsLabel.setText(f'{definition_to_display}')


# PyQT5
Form, Window = uic.loadUiType("dictP_ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Event handlers
form.lineEdit.textChanged.connect(find_suggestions)

window.show()
app.exec()
