from PyQt6.QtWidgets import QWidget as Widget, QApplication as App, QPushButton as Button, QLabel as Label
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from types import SimpleNamespace as namespace


class ZxColors:
    def __init__(self):
        self.primary = QColor(54, 54, 54)
        self.secondary = QColor(48, 48, 48)
        self.highlight = QColor(100, 100, 100)
        self.shadow = QColor(38, 38, 38)

        self.info = QColor(144, 144, 144)
        self.warning = QColor(219, 172, 61)
        self.danger = QColor(205, 92, 92)
        self.success = QColor(124, 205, 124)
        self.failure = QColor(205, 124, 124)
    def Apply(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, self.primary)
        pallet.setColor(QPalette.ColorRole.WindowText, self.secondary)
        palette.setColor(QPalette.ColorRole.Active, self.secondary)
        palette.setColor(QPalette.ColorRole.Highlight, self.highlight)
        palette.setColor(QPalette.ColorRole.HighlightedText, self.shadow)
        palette.setColor(QPalette.ColorRole.Button, self.primary)
        palette.setColor(QPalette.ColorRole.Shadow, self.shadow)
        palette.setColor(QPalette.ColorRole.Light, self.shadow)
        palette.setColor(QPalette.ColorRole.Midlight, self.shadow)
        palette.setColor(QPalette.ColorRole.Dark, self.primary)
        palette.setColor(QPalette.ColorRole.Mid, self.primary)
        palette.setColor(QPalette.ColorRole.Text, self.secondary)
        
        palette.setColor(QPalette.ColorRole.ButtonText, self.secondary)
        palette.setColor(QPalette.ColorRole.Disabled, self.secondary)
        palette.setColor(QPalette.ColorRole.ToolTipText, self.secondary)
        

        # set brush
        palette.setBrush(QPalette.ColorRole.Window, self.primary)
        palette.setBrush(QPalette.ColorRole.Base, self.primary)
        palette.setBrush(QPalette.ColorRole.Text, self.secondary)
        palette.setBrush(QPalette.ColorRole.Button, self.primary)
        palette.setBrush(QPalette.ColorRole.ButtonText, self.secondary)
        palette.setBrush(QPalette.ColorRole.Shadow, self.shadow)
        palette.setBrush(QPalette.ColorRole.Highlight, self.highlight)
        palette.setBrush(QPalette.ColorRole.Light, self.highlight)
        palette.setBrush(QPalette.ColorRole.Midlight, self.shadow)
        palette.setBrush(QPalette.ColorRole.Mid, self.secondary)
        palette.setBrush(QPalette.ColorRole.Dark, self.primary)
        palette.setBrush(QPalette.ColorRole.WindowText, self.secondary)
        App.setPalette(palette)






class ZxToolbar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setSpacing(8)
        self.mainLayout.setContentsMargins(0,0,0,0)

    def addWidget(self, widget):
        self.mainLayout.addWidget(widget)
        widget.installEventFilter(self)

if __name__ == "__main__":
    app = App([])
    toolbar = ZxToolbar()
    toolbar.addWidget(Button("Click me!123"))
