import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, QFileDialog)

class SimpleTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        save_action = QAction('Save As...', self)
        save_action.triggered.connect(self.save_file)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 800, 800)
        self.show()

    def open_file(self):
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                  'Text Files (*.txt);;All Files (*)', options=options)
        if filepath:
            with open(filepath, mode='r', encoding='utf-8') as input_file:
                text = input_file.read()
                self.text_edit.setPlainText(text)
            self.setWindowTitle(f'Simple Text Editor - {filepath}')

    def save_file(self):
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getSaveFileName(self, 'Save File', '',
                                                  'Text Files (*.txt);;All Files (*)', options=options)
        if filepath:
            with open(filepath, mode='w', encoding='utf-8') as output_file:
                text = self.text_edit.toPlainText()
                output_file.write(text)
            self.setWindowTitle(f'Simple Text Editor - {filepath}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = SimpleTextEditor()
    sys.exit(app.exec_())
