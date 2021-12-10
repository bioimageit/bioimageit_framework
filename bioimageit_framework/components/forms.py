import qtpy.QtCore
from qtpy.QtWidgets import QLineEdit, QSpinBox, QComboBox, QGroupBox, QHBoxLayout, QPushButton, QFileDialog

from bioimageit_framework.framework import BiComponent


class BiLineEdit(BiComponent):
    """Line edit widget"""
    CHANGED = 'changed'
    
    def __init__(self):
        super().__init__()
        self.widget = QLineEdit()
        self.widget.textChanged.connect(self._changed)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)

    def text(self):
        return self.widget.text()    

    def _changed(self, text):
        self.emit(BiLineEdit.CHANGED)   


class BiSpinBox(BiComponent):
    """Spin box widget"""
    def __init__(self, value=0):
        super().__init__()
        self.widget = QSpinBox(value)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)      


class BiSelectorBox(BiComponent):
    """Selector widget"""
    def __init__(self):
        super().__init__()
        self.widget = QComboBox()
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False) 


class BiGroupBox(BiComponent):
    """Group box widget"""
    def __init__(self, title):
        super().__init__(title)
        self.widget = QGroupBox()
        self.setObjectName('bi-group-box')


class BiFileSelector(BiComponent):
    CHANGED = 'changed'

    def __init__(self, is_dir=False):
        super().__init__()

        self.is_dir = is_dir

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)

        self.line_edit = BiLineEdit()
        layout.addWidget(self.line_edit)
        browse_btn = QPushButton('...')
        browse_btn.setObjectName('btn-default')
        layout.addWidget(browse_btn)
        browse_btn.released.connect(self.browse)

    def browse(self):
        if self.is_dir:
            dir = QFileDialog.getExistingDirectory(self, "Open a directory")
            if dir != "":
                self.line_edit.setText(dir)
                self.emit(BiFileSelector.CHANGED)
        else:
            file = QFileDialog.getOpenFileName(self, "Open a file", '', "*.*")
            if file != "":
                self.line_edit.setText(file[0])
                self.emit(BiFileSelector.CHANGED)

    def text(self):
        return self.line_edit.text()
