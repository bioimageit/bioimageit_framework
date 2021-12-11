import os
import sys
from bioimageit_framework.framework.framework import BiConnectome

from qtpy.QtWidgets import QApplication

from bioimageit_framework.framework import BiComponent, BiContainer, BiActuator
from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiButtonPrimary, BiLineEdit, BiVComposer, showInfoBox


class HelloContainer(BiContainer):
    CHANGED = 'changed'
    SAVED = 'saved'

    def __init__(self):
        super().__init__()
        self.text = ''


class HelloModel(BiActuator):
    def __init__(self):
        super().__init__()

    def callback_changed(self, action):
        with open('helloworld.txt', 'w') as output:
            output.write(action.container.text)
        action.container.emit(HelloContainer.SAVED)    


class HelloComponent(BiComponent):
    def __init__(self):
        super().__init__()

        composer = BiVComposer()
        self.line_edit = BiLineEdit()
        self.button = BiButtonPrimary('Save')
        self.button.connect(BiButtonPrimary.CLICKED, self.clicked)
        composer.add(self.line_edit) 
        composer.add(self.button)
        self.widget = composer.widget

    def clicked(self, origin): 
        self.container.text = self.line_edit.text()
        self.container.emit(HelloContainer.CHANGED)

    def callback_saved(self, action):
        showInfoBox(f'{self.container.text} have been saved')      


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    container = HelloContainer()
    model = HelloModel()
    component = HelloComponent()

    BiConnectome.connect(container, model)
    BiConnectome.connect(container, component)

    component.widget.show() 
 
    # Run the main Qt loop
    sys.exit(app.exec_())