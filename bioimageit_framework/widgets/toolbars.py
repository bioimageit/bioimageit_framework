from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget, QHBoxLayout, QToolButton

from bioimageit_framework.theme import BiThemeAccess
from bioimageit_framework.framework import BiComponent
from .widget import BiWidget


class QIdToolButton(QToolButton):
    pushed = Signal(str)

    def __init__(self, id=''):
        super().__init__()
        self.id = id
        self.released.connect(self.emit_id)

    def emit_id(self):
        self.pushed.emit(self.id)


class BiToolBar(BiWidget):
    def __init__(self):
        super().__init__()
        self.name = 'toolbar'
        self.widget = QWidget()
        self.widget.setObjectName('BiToolBar')
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)

    def add_toolbutton(self, action='', icon='', tooltip=''):
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
        button = QIdToolButton(action)
        if icon != '':
            button.setIcon(BiThemeAccess.instance().icon(icon))
        button.setToolTip(tooltip)
        button.pushed.connect(self.emit_clicked)
        self.layout.addWidget(button, 0)

    def emit_clicked(self, action):
        self.emit(action)

    def add_spacer(self):
        self.layout.addWidget(QWidget(), 1)

    def add(self, component):
        self.layout.addWidget(component.widget)    
