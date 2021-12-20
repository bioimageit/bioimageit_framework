import sys
import os
from qtpy.QtWidgets import QApplication

from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiWidget, BiForm, showInfoBox


class MyForm(BiWidget):
    """Create a table with an open button in the first row

    Parameters
    ----------
    header: list
        List of the header labels
    data: ndarray
        data matrix    
    """
    def __init__(self):
        self.form = BiForm()
        self.widget = self.form.widget

        self.form.add_group_box('Profile')
        self.form.add_line_edit('firstname', 'Firstname')
        self.form.add_line_edit('name', 'Name') # key, label
        self.form.add_int_edit('age', 'Age')
        self.form.add_file_select('avatar', 'Avatar')

        self.form.add_group_box('Skills')
        self.form.add_select_box('job', 'Job', ['front-end dev', 'back-end dev', 'full-stack dev'])
        
        self.form.add_validate_button('Save', self.form_saved)
        self.form.add_bottom_spacer()
        self.form.set_maximum_width(500)

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
