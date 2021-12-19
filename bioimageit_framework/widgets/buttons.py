from qtpy.QtWidgets import QPushButton, QMessageBox

from bioimageit_framework.framework import BiComponent
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
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-default')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
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
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-primary')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
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
