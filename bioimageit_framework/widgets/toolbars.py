import qtpy.QtCore
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget, QHBoxLayout, QToolButton, QPushButton

from bioimageit_framework.theme import BiThemeAccess
from .widget import BiWidget

class QIdPushButton(QPushButton):
    pushed = Signal(str)

    def __init__(self, id='', title=''):
        super().__init__(title)
        self.id = id
        self.released.connect(self.emit_id)

    def emit_id(self):
        self.pushed.emit(self.id)

class QIdToolButton(QToolButton):
    pushed = Signal(str)

    def __init__(self, id=''):
        super().__init__()
        self.id = id
        self.released.connect(self.emit_id)

    def emit_id(self):
        self.pushed.emit(self.id)


class BiToolBar(BiWidget):
    def __init__(self, align='left'):
        super().__init__()
        self.name = 'toolbar'
        self.widget = QWidget()
        self.widget.setObjectName('bi-toolbar')
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.align = align  
        self.active_item = ''
        if self.align == 'left':
            spacer_w = QWidget()
            spacer_w.setObjectName('bi-toolbar-spacer')
            self.layout.addWidget(spacer_w, 1) 
        self._buttons = []     

    def add_pushbutton(self, action='', icon='', tooltip=''):
        """Add a button to the toolbar

        Parameters
        ----------
        action: str
            Name of the action triggered by the button
        icon: str
            Name of the icon discplayed in the button
        tooltip: str
            Text of the button tooltip  
              
        """   
        button = QIdPushButton(action, action)
        button.setCheckable(True)
        button.setAutoExclusive(True)
        button.setObjectName('bi-toolbar-button')
        if icon != '':
            button.setIcon(BiThemeAccess.instance().icon(icon))
        button.setToolTip(tooltip)
        button.pushed.connect(self.emit_clicked)
        if self.align == 'left':
            self.layout.insertWidget(self.layout.count()-1, button, 0, qtpy.QtCore.Qt.AlignLeft)
        else:
            self.layout.addWidget(button)      
        self._buttons.append(button)

    def add_toolbutton(self, action='', icon='', tooltip=''):
        """Add a tool button to the toolbar

        Parameters
        ----------
        action: str
            Name of the action triggered by the button
        icon: str
            Name of the icon discplayed in the button
        tooltip: str
            Text of the button tooltip  

        """    
        button = QIdToolButton(action)
        button.setObjectName('bi-tool-button')
        if icon != '':
            button.setIcon(BiThemeAccess.instance().icon(icon))
        button.setToolTip(tooltip)
        button.pushed.connect(self.emit_clicked)
        self.layout.addWidget(button, 0)

    def switch(self, id):
        for button in self._buttons:
            if button.id == id:
                button.setChecked(True)

    def emit_clicked(self, action):
        self.active_item = action
        self.emit(action)

    def add_spacer(self):
        self.layout.addWidget(QWidget(), 1) 

    def add(self, component):
        self.layout.addWidget(component.widget)    
