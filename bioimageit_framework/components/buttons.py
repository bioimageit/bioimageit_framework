from qtpy.QtWidgets import QPushButton, QMessageBox

from bioimageit_framework.framework import BiComponent


class BiButtonDefault(BiComponent):
    CLICKED = 'clicked'
    """Default button

    A button with a default behaviour and appearance
    """

    def __init__(self, title=''):
        super().__init__()
        self.name = "BiButtonDefault"
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-default')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
        self.emit(BiButtonDefault.CLICKED) 

        
class BiButtonPrimary(BiComponent):
    CLICKED = 'clicked'
    """Primary button

    A highlighted button
    """
    
    def __init__(self, title=''):
        super().__init__()
        self.name = "BiButtonPrimary"
        self.widget = QPushButton(title)
        self.widget.setObjectName('btn-primary')
        self.widget.clicked.connect(self._clicked)

    def _clicked(self):
        self.emit(BiButtonPrimary.CLICKED)    
  
     
class BiButtonDanger(BiComponent):
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
