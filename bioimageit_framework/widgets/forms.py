from PySide2.QtWidgets import QHBoxLayout, QPushButton
import qtpy.QtCore
from qtpy.QtCore import Signal
from qtpy.QtWidgets import (QWidget, QLineEdit, QSpinBox, QComboBox,
                            QHBoxLayout, QFileDialog, QGroupBox)

from .buttons import BiButtonDefault


class BiLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)


class BiSpinBox(QSpinBox):
    def __init__(self):
        super().__init__()
        self.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)      


class BiComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False) 


class BiGroupBox(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        #self.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.setObjectName('bi-group-box')
                  

class BiFileSelector(QWidget):
    text_changed = Signal()

    def __init__(self, is_dir=False):
        super().__init__()

        self.is_dir = is_dir

        #self.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)

        self.line_edit = BiLineEdit()
        layout.addWidget(self.line_edit)
        browse_btn = BiButtonDefault('...')
        layout.addWidget(browse_btn)
        browse_btn.released.connect(self.browse)

    def browse(self):
        if self.is_dir:
            dir = QFileDialog.getExistingDirectory(self, "Open a directory")
            if dir != "":
                self.line_edit.setText(dir)
                self.text_changed.emit()
        else:
            file = QFileDialog.getOpenFileName(self, "Open a file", '', "*.*")
            if file != "":
                self.line_edit.setText(file[0])
                self.text_changed.emit()

    def text(self):
        return self.line_edit.text()
