import qtpy.QtCore
from qtpy.QtWidgets import (QLineEdit, QSpinBox, QComboBox, QGroupBox, 
                            QHBoxLayout, QPushButton, QFileDialog,
                            QWidget, QGridLayout, QLabel)

from .widget import BiWidget


class BiLineEdit(BiWidget):
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


class BiSpinBox(BiWidget):
    """Spin box widget"""
    def __init__(self, value=0):
        super().__init__()
        self.widget = QSpinBox(value)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)      


class BiSelectorBox(BiWidget):
    """Selector widget"""
    def __init__(self):
        super().__init__()
        self.widget = QComboBox()
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        self.widget.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False) 


class BiGroupBox(BiWidget):
    """Group box widget"""
    def __init__(self, title):
        super().__init__(title)
        self.widget = QGroupBox()
        self.setObjectName('bi-group-box')


class BiFileSelector(BiWidget):
    """File or directory selection
    
    Display a line edit and a button to select a file or 
    a directory

    Parameters
    ----------
    is_dir: bool
        True to select a directory, False to select a file
    
    """
    CHANGED = 'changed'

    def __init__(self, is_dir=False):
        super().__init__()


        self.widget = QWidget()
        self.is_dir = is_dir

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        self.widget.setLayout(layout)

        self.line_edit = BiLineEdit()
        layout.addWidget(self.line_edit.widget)
        browse_btn = QPushButton('...')
        browse_btn.setObjectName('btn-default')
        layout.addWidget(browse_btn)
        browse_btn.released.connect(self.browse)

    def browse(self):
        if self.is_dir:
            dir = QFileDialog.getExistingDirectory(self.widget, "Open a directory")
            if dir != "":
                self.line_edit.setText(dir)
                self.emit(BiFileSelector.CHANGED)
        else:
            file = QFileDialog.getOpenFileName(self.widget, "Open a file", '', "*.*")
            if file != "":
                self.line_edit.widget.setText(file[0])
                self.emit(BiFileSelector.CHANGED)

    def text(self):
        return self.line_edit.text()


class BiForm(BiWidget):
    VALIDATED = 'validated'

    def __init__(self):
        super().__init__()
        self.name = 'form'
        self._row_count = -1
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)
        self.widgets = {}

    def add_line_edit(self, key, label):
        """Add a line edit entry to the form

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user  

        """
        self._row_count += 1
        self.layout.addWidget(QLabel(label), self._row_count, 0)
        line_edit = QLineEdit()
        line_edit.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        line_edit.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)
        self.widgets[key] = line_edit
        self.layout.addWidget(line_edit, self._row_count, 1)

    def add_int_edit(self, key, label):
        """Add a spin box entry to the form for integers

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user   

        """
        self._row_count += 1
        self.layout.addWidget(QLabel(label), self._row_count, 0)
        edit = QSpinBox()
        edit.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        edit.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)
        self.widgets[key] = edit
        self.layout.addWidget(edit, self._row_count, 1)

    def add_select_box(self, key, label, items):
        """Add a select box (combobox) entry to the form

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user 
        items: list
            List of items in the select widget  

        """
        self._row_count += 1
        self.layout.addWidget(QLabel(label), self._row_count, 0)
        edit = QComboBox()
        edit.addItems(items)
        self.layout.addWidget(edit, self._row_count, 1)

    def add_file_select(self, key, label):
        """Add a select box (combobox) entry to the form

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user 
        items: list
            List of items in the select widget  

        """
        self._row_count += 1
        self.layout.addWidget(QLabel(label), self._row_count, 0, 1, 1, qtpy.QtCore.Qt.AlignTop)
        edit = BiFileSelector()
        self.widgets[key] = edit
        self.widgets[key] = edit
        self.layout.addWidget(edit.widget, self._row_count, 1, 1, 1, qtpy.QtCore.Qt.AlignTop)        

    def add_validate_button(self, title, callback):
        self._row_count += 1
        btn = QPushButton(title)
        btn.setObjectName('btn-primary')
        btn.released.connect(self._emit_validate)
        self.layout.addWidget(btn, self._row_count, 0, 1, 2, qtpy.QtCore.Qt.AlignLeft)  
        self.connect(BiForm.VALIDATED, callback)

    def add_bottom_spacer(self):
        self._row_count += 1
        widget = QWidget()
        widget.setSizePolicy(qtpy.QtWidgets.QSizePolicy.Expanding, qtpy.QtWidgets.QSizePolicy.Expanding)
        self.layout.addWidget(widget, self._row_count, 0, 1, 2) 

    def _emit_validate(self):
        # fill content and emit validated
        print('BiForm emit validated')
        self.emit(BiForm.VALIDATED)