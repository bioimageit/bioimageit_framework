import os
import sys
from bioimageit_framework.framework.framework import BiConnectome

from qtpy.QtWidgets import QApplication

from bioimageit_framework.framework import BiConnectome, BiComponent, BiContainer, BiActuator
from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiButtonPrimary, BiLineEdit, BiVComposer, showInfoBox


class HelloContainer(BiContainer):
    CHANGED = 'changed'
    SAVED = 'saved'

    def __init__(self):
        super().__init__()
        self.text1 = ''
        self.text2 = ''

    def action_change_text(self, action, text1, text2):
        """Action callback to update the text"""
        self.text1 = text1
        self.text2 = text2
        self._notify(HelloContainer.CHANGED) 

    def action_saved(self, action):
        self._notify(HelloContainer.SAVED)            


class HelloModel(BiActuator):
    def __init__(self):
        super().__init__()

    def callback_changed(self, action):
        with open('helloworld.txt', 'w') as output:
            output.write(f'{action.emitter.text1}, {action.emitter.text2}')
        self._emit(HelloContainer.SAVED, ())    


class HelloComponent(BiComponent):
    CHANGE_TEXT = 'change_text'

    def __init__(self):
        super().__init__()

        composer = BiVComposer()
        self.line_edit1 = BiLineEdit()
        self.line_edit2 = BiLineEdit()
        self.button = BiButtonPrimary('Save')
        self.button.connect(BiButtonPrimary.CLICKED, self.clicked)
        composer.add(self.line_edit1)
        composer.add(self.line_edit2)  
        composer.add(self.button)
        self.widget = composer.widget

    def clicked(self, origin): 
        self._emit(HelloComponent.CHANGE_TEXT, (self.line_edit1.text(), self.line_edit2.text()))

    def callback_saved(self, action):
        showInfoBox(f'{action.emitter.text1}, {action.emitter.text2} have been saved')      


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
