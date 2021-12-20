from PySide2.QtWidgets import QVBoxLayout
import qtpy.QtCore
from qtpy.QtWidgets import (QLineEdit, QSpinBox, QComboBox, QGroupBox, 
                            QHBoxLayout, QPushButton, QFileDialog,
                            QWidget, QGridLayout, QLabel, QGroupBox)

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

        self.widget.setStyleSheet(".QWidget{background-color: transparent;}")

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
        self._group_boxes = []
        self._group_row_count = -1
        self.widgets = {}

        # main widget
        self.widget = QWidget()

        self.layout = QGridLayout()
        
        _global_layout = QVBoxLayout()
        _global_layout.setContentsMargins(0, 0, 0, 0)
        self._widget = QWidget()
        self._widget.setLayout(self.layout)
        self.widget.setLayout(_global_layout)
        _global_layout.addWidget(self._widget, 0, qtpy.QtCore.Qt.AlignHCenter)

        

    def set_maximum_width(self, width):
        self._widget.setMaximumWidth(width)

    def add_group_box(self, title):
        group_box = QGroupBox(title)
        group_box_layout = QGridLayout()
        group_box.setLayout(group_box_layout)
        self._group_boxes.append(group_box_layout)
        self._row_count += 1
        self.layout.addWidget(group_box, self._row_count, 0, 1, 2)
        self._group_row_count = -1


    def _next_row_idx(self):
        """Calculate the next row index

        Return
        ------
        The next row index for the groupbox or main layout

        """
        if len(self._group_boxes) > 0:
            self._group_row_count += 1
            return self._group_row_count
        else:    
            self._row_count += 1
            return self._row_count

    def _layout(self):
        if len(self._group_boxes) > 0:
            return self._group_boxes[len(self._group_boxes)-1]
        else:
            return self.layout     

    def _new_label(self, title):
        label = QLabel(title)
        if len(self._group_boxes) > 0:
            label.setObjectName('bi-label-groupbox')
        return label    

    def add_line_edit(self, key, label):
        """Add a line edit entry to the form

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user  

        """
        row = self._next_row_idx()
        self._layout().addWidget(self._new_label(label), row, 0)
        line_edit = QLineEdit()
        line_edit.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        line_edit.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)
        self.widgets[key] = line_edit
        self._layout().addWidget(line_edit, row, 1)

    def add_int_edit(self, key, label):
        """Add a spin box entry to the form for integers

        Parameters
        ----------
        key: str
            Key to identify the entry
        label: str
            Label printed to the user   

        """
        row = self._next_row_idx()
        self._layout().addWidget(self._new_label(label), row, 0)
        edit = QSpinBox()
        edit.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        edit.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)
        self.widgets[key] = edit
        self._layout().addWidget(edit, row, 1)

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
        row = self._next_row_idx()
        self._layout().addWidget(self._new_label(label), row, 0)
        edit = QComboBox()
        edit.addItems(items)
        self.widgets[key] = edit
        self._layout().addWidget(edit, row, 1)

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
        row = self._next_row_idx()
        self._layout().addWidget(self._new_label(label), row, 0, 1, 1, qtpy.QtCore.Qt.AlignTop)
        edit = BiFileSelector()
        self.widgets[key] = edit
        self._layout().addWidget(edit.widget, row, 1, 1, 1, qtpy.QtCore.Qt.AlignTop)        

    def add_validate_button(self, title, callback):
        self._row_count += 1
        btn = QPushButton(title)
        btn.setObjectName('btn-primary')
        btn.released.connect(self._emit_validate)
        self.layout.addWidget(btn, self._row_count, 0, 1, 2, qtpy.QtCore.Qt.AlignRight)  
        self.connect(BiForm.VALIDATED, callback)

    def add_bottom_spacer(self):
        self._row_count += 1
        widget = QWidget()
        widget.setSizePolicy(qtpy.QtWidgets.QSizePolicy.Expanding, qtpy.QtWidgets.QSizePolicy.Expanding)
        self.layout.addWidget(widget, self._row_count, 0, 1, 2) 

    def _emit_validate(self):
        # fill content and emit validated
        print('fill content')
        for key in self.widgets:
            widget = self.widgets[key]
            if isinstance(widget, QLineEdit):
                self.content[key] = widget.text()
            elif isinstance(widget, QSpinBox):
                self.content[key] = widget.value()
            elif isinstance(widget, QComboBox):
                self.content[key] = widget.currentText()
            elif isinstance(widget, BiFileSelector):
                self.content[key] = widget.text()   
        print('BiForm emit validated')
        self.emit(BiForm.VALIDATED)