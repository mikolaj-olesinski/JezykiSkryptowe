from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QFileDialog, QLabel, QDateEdit, QVBoxLayout, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt, QDate
from constants import (FILE_SELECTOR_LABEL_WIDTH, 
                       FILE_SELECTOR_LABEL_HEIGHT, 
                       FILE_SELECTOR_BUTTON_WIDTH, 
                       FILE_SELECTOR_BUTTON_HEIGHT)
from help_func.read_http_log import read_l

import sys

class FileSelectionWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


        self.file_label = QLabel("Brak wybranego pliku")
        self.file_label.setFixedSize(FILE_SELECTOR_LABEL_WIDTH, FILE_SELECTOR_LABEL_HEIGHT)
        self.file_label.setStyleSheet("border: 1px solid grey;")
        layout.addWidget(self.file_label)

        self.select_button = QPushButton("Wybierz plik")
        self.select_button.setFixedSize(FILE_SELECTOR_BUTTON_WIDTH, FILE_SELECTOR_BUTTON_HEIGHT)
        layout.addWidget(self.select_button)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Pliki tekstowe (*.txt) ;; Wszystkie pliki (*)")
        if file_path:
            self.file_label.setText(file_path)

            return file_path
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano pliku")

    def get_file_path(self):
        return self.file_label.text()


class DateSelectionWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd")  
        self.date_edit.setDate(QDate.currentDate())    
        layout.addWidget(self.date_edit)

    def setDate(self, date):
        self.date_edit.setDate()

class LabelForForm(QWidget):
    def __init__(self, text, width, height, border=True):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.label = QLabel(text)
        layout.addWidget(self.label)

        self.label_with_info = QLabel()
        self.label_with_info.setFixedSize(width, height)
        if border:
            self.label_with_info.setStyleSheet("border: 1px solid grey;")

        layout.addWidget(self.label_with_info)

    def set_info(self, info):
        self.label_with_info.setText(info)

# class QListItem(QWidget):
#     def __init__(self, display_text, info_text):
#         super().__init__()

#         self.display_text = display_text
#         self.info_text = info_text

#         layout = QHBoxLayout()
#         layout.setContentsMargins(0, 0, 0, 0)
#         self.setLayout(layout)


#         self.display_label = QLabel(display_text)

#     def get_info(self):
#         return self.info_text
    
#     def set_display_text(self, text):
#         self.display_label.setText(text)


class QListItem():
    def __init__(self, display_text, info_text):
        self.display_text = display_text
        self.info_text = info_text
        