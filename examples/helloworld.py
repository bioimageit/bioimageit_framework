import os
import sys

from qtpy.QtWidgets import QApplication

from bioimageit_framework.framework import BiComponent
from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiButtonPrimary, BiLineEdit, BiVComposer


class HelloComponent(BiComponent):
    def __init__(self):
        super().__init__()

        composer = BiVComposer()
        self.line_edit = BiLineEdit()
        self.button = BiButtonPrimary('Click to print')
        self.button.connect(BiButtonPrimary.CLICKED, self.clicked)
        composer.add(self.line_edit) 
        composer.add(self.button)
        self.widget = composer.widget

    def clicked(self, origin):
        print('hello pwd', self.line_edit.text())    


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    component = HelloComponent()
    component.widget.show() 
 
    # Run the main Qt loop
    sys.exit(app.exec_())
