# Import the necessary classes: Add the following imports at the beginning of your script:

from PyQt6.QtWidgets import QFontDialog, QColorDialog

# Add a new method to open the font dialog:

def open_font_dialog(self):
    font, ok = QFontDialog.getFont(self.font(), self, "Choose Font")
    if ok:
        self.change_font(font)

# Add a new method to open the color dialog:

def open_color_dialog(self):
    color = QColorDialog.getColor(self.palette().windowText().color(), self, "Choose Color")
    if color.isValid():
        self.change_color(color)

# Add new methods to change the font and color:

def change_font(self, font):
    self.setFont(font)
    self.statusBar().setFont(font)

def change_color(self, color):
    palette = self.palette()
    palette.setColor(palette.ColorRole.WindowText, color)
    self.setPalette(palette)

# Modify the `__init__` method to add the "Customize" menu and its actions:
# Add the following lines after setting up the help menu:
customize_menu = menubar.addMenu("&Customize")
font_action = QWidgetAction(self)
font_action.setText("Font")
font_action.triggered.connect(self.open_font_dialog)
customize_menu.addAction(font_action)

color_action = QWidgetAction(self)
color_action.setText("Color")
color_action.triggered.connect(self.open_color_dialog)
customize_menu.addAction(color_action)
