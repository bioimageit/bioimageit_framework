import qtpy.QtCore
from qtpy.QtCore import Signal
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout

from bioimageit_framework.theme import BiThemeAccess
from .widget import BiWidget


class BiButtonDefault(BiWidget):
    CLICKED = 'clicked'
    """Default button

    A button with a default behaviour and appearance
    """

    def __init__(self, title=''):
        super().__init__()
        self.name = "BiButtonDefault"
        self.content = {}
        self.id = 0
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-default')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
        print('button default emit clicked with id=', self.id)
        self.emit(BiButtonDefault.CLICKED) 

        
class BiButtonPrimary(BiWidget):
    CLICKED = 'clicked'
    """Primary button

    A highlighted button

    """
    def __init__(self, title=''):
        super().__init__()
        self.name = "BiButtonPrimary"
        self.content = {}
        self.id = 0
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-primary')
        self.widget.clicked.connect(self.emit_clicked)

    def emit_clicked(self):
        print('button emit clicked with id=', self.id)
        self.emit(BiButtonPrimary.CLICKED)    
  
     
class BiButtonDanger(BiWidget):
    CLICKED = 'clicked'
    
    """Danger button

    Button for a dangereous action.
    This button can open a confirmation popup if the option is activated

    Parameters
    ----------
    popup: boolean
        True to ask for a confirmation before emitting the cliked signal

    """
    def __init__(self, title='', popup=True):
        super().__init__(title)
        self.name = "BiButtonDanger"
        self.content = {}
        self.id = 0
        self.popup = popup
        self.confirm_text = 'Are you sure ?'

        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-danger')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
        if self.popup:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(self.confirm_text)
            msgBox.setWindowTitle("Warning")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.emit(BiButtonPrimary.CLICKED)
        else:
            self.emit(BiButtonPrimary.CLICKED)


class BiClosableButton(QPushButton):
    clicked = Signal(int)
    closed = Signal(int)

    def __init__(self, closable: bool = True,  parent: QWidget = None):
        super().__init__(parent)
        self._id = -1
        if closable:
            layout = QVBoxLayout()
            layout.setContentsMargins(0,0,0,0)
            closeButton = QPushButton()
            closeButton.setObjectName("bi-close-button")
            closeButton.setIcon(QIcon(BiThemeAccess.instance().icon('close')))
            closeButton.setFixedSize(12,12)
            layout.addWidget(closeButton, 1, qtpy.QtCore.Qt.AlignTop | qtpy.QtCore.Qt.AlignRight)
            self.setLayout(layout)
            closeButton.pressed.connect(self.emitClosed)
        self.pressed.connect(self.emitClicked)    

    def id(self) -> int:
        return self._id

    def setId(self, id: int):
        self._id = id

    def emitClicked(self):
        self.clicked.emit(self._id)

    def emitClosed(self):
        self.closed.emit(self._id)