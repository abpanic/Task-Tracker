## Task Tracker
## Created by dbugr (https://dbugr.vercel.app/)

from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QDialog

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        app_name = QLabel("Task Tracker")
        app_name.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(app_name)

        version = QLabel("Version 1.0")
        layout.addWidget(version)

        author_label = QLabel('Abhilash')
        layout.addWidget(author_label)

        website_label = QLabel('<a href="https://dbugr.vercel.app">dbugr.vercel.app</a>')
        website_label.setOpenExternalLinks(True)
        layout.addWidget(website_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)
        self.setWindowTitle("About Task Tracker")
