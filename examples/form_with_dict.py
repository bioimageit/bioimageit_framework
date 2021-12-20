import sys
import os
from qtpy.QtWidgets import QApplication

from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiWidget, BiForm, showInfoBox


class MyForm(BiWidget):
    """Example of creating a form from a dictionnary"""
    def __init__(self):
        self.form = BiForm()
        self.widget = self.form.widget


        form_dict = {'form': [
            {
                'type': 'group_box',
                'title': 'Profile',
                'form': [
                    {
                        'type': 'line_edit',
                        'key': 'firstname',
                        'label': 'Firstname'
                    },
                   {
                        'type': 'line_edit',
                        'key': 'name',
                        'label': 'Name'
                    }, 
                    {
                        'type': 'int_edit',
                        'key': 'age',
                        'label': 'Age'
                    },
                    {
                        'type': 'file_select',
                        'key': 'avatar',
                        'label': 'Avatar'
                    },
                ]
            },
            {
                'type': 'group_box',
                'title': 'Skills',
                'form': [
                    {
                        'type': 'select_box',
                        'key': 'job',
                        'label': 'Job',
                        'items': ['front-end dev', 'back-end dev', 'full-stack dev']
                    },
                ]
            },
            {
                'type': 'validate_button',
                'title': 'Save',
                'callback': self.form_saved
            },
            {
                'type': 'bottom_spacer'
            }
        ]}

        self.form.build(form_dict)

    def form_saved(self, form): 
        print('MyForm got the validated signal')
        showInfoBox(f'you clicked the button open row {form.content}')          


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load and set the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    widget = MyForm()
    widget.widget.show() 
 
    # Run the main Qt loop
    sys.exit(app.exec_())
