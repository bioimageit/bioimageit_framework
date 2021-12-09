from qtpy.QtCore import Signal
from qtpy.QtWidgets import QPushButton, QMessageBox


class BiButtonDefault(QPushButton):
    """Default button

    A button with a default behaviour and appearance
    """
    def __init__(self, title):
        super().__init__(title)
        self.setObjectName('btn-default')


class BiButtonPrimary(QPushButton):
    """Primary button

    A highlighted button
    """
    def __init__(self, title):
        super().__init__(title)
        self.setObjectName('btn-primary')        


class BiButtonDanger(QPushButton):
    validated = Signal()
    
    """Danger button

    Button for a dangereous action.
    This button can open a confirmation popup if the option is activated

    Parameters
    ----------
    popup: boolean
        True to ask for a confirmation before emitting the cliked signal

    """
    def __init__(self, title, popup=False):
        super().__init__(title)
        self.setObjectName('btn-danger') 
        self.popup = popup
        self.confirm_text = 'Confirm ?'
        self.released.connect(self.popup_dialog)

    def popup_dialog(self):
        if self.popup:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(self.confirm_text)
            msgBox.setWindowTitle("Warning")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.validated.emit() 
        else:
            self.validated.emit()             
