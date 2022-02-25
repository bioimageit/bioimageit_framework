"""Define the BiWidget base class

"""
from qtpy.QtWidgets import QWidget, QMessageBox


class BiWidget:
    """Base widget

    Define the connection and actions for widgets
    
    """
    def __init__(self):
        self.widget = QWidget()
        self.content = {}
        self.connections = {}

    def connect(self, signal, method):
        if signal in self.connections:
            self.connections[signal].append(method)
        else:
            self.connections[signal] = [method]

    def emit(self, signal):    
        if signal in self.connections:
            for connection in self.connections[signal]:
                connection(self)

    def set_visible(self, value):
        """Show or hide a widget
        
        Parameters
        ----------
        value: bool
            True to set the widget visible, False otherwise

        """
        self.widget.setVisible(value)            


def showInfoBox(text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle("Message")
    msgBox.exec()
