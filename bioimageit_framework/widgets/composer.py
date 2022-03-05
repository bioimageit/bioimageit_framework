"""Composer module

Composer are Graphical interface layers to compose widgets 


"""
import qtpy.QtCore
from qtpy.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSplitter


class BiVComposer:
    """Composer with a vertical layout"""
    def __init__(self):
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_contents_margins(self, left, top, right, bottom):
        self.layout.setContentsMargins(left, top, right, bottom)

    def set_spacing(self, value):
        self.layout.setSpacing(value)    

    def add(self, component):
        self.layout.addWidget(component.widget)


class BiHComposer:
    """Composer with a horizontal layout"""
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_contents_margins(self, left, top, right, bottom):
        self.layout.setContentsMargins(left, top, right, bottom)

    def set_spacing(self, value):
        self.layout.setSpacing(value)    

    def add(self, component):
        self.layout.addWidget(component.widget)      


class BiGridComposer:
    """Composer with a grid layout"""
    def __init__(self):
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_contents_margins(self, left, top, right, bottom):
        self.layout.setContentsMargins(left, top, right, bottom)

    def set_spacing(self, value):
        self.layout.setSpacing(value)    

    def add(self, component, row, col, row_span, col_span):
        self.layout.addWidget(component.widget, row, col, row_span, col_span)            


class BiSplittercomposer:
    """Composer with a splitter as a layout"""
    def __init__(self, orientation="horizontal"):
        self.widget = QSplitter()
        if orientation == 'vertical':
            self.widget.setOrientation(qtpy.QtCore.Qt.Vertical)
        elif orientation == 'horizontal':    
            self.widget.setOrientation(qtpy.QtCore.Qt.Horizontal)

    def add(self, component):
        self.widget.addWidget(component.widget)        
