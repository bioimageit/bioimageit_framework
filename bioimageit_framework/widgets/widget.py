"""Define the BiWidget base class

"""

from qtpy.QtWidgets import QMessageBox


class BiWidget:
    """Base widget

    Define the connection and actions for widgets
    
    """
    def __init__(self):
        self.widget = None # QWidget
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


def showInfoBox(text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(text)
    msgBox.setWindowTitle("Message")
    msgBox.exec()