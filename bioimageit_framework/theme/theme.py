import os.path


class BiThemeIcons:
    """Define all the GUI icons names

    This is a static list of all the logo available your theme

    """
    LOGO = 'logo'


class BiThemeSheets:
    """Define all the qss filenames

    These are all the qss filenames available in the style
    
    """
    MAIN = 'main'
    BUTTONS = 'buttons'
    FORMS = 'forms'

    @staticmethod
    def sheets():
        return [BiThemeSheets.BUTTONS, 
                BiThemeSheets.FORMS,
                BiThemeSheets.MAIN
               ]


class BiTheme:
    """Utilisies for GUI theme"""
    def __init__(self, theme_dir=''):
        self.theme_dir =  theme_dir   

    def icon(self, name):
        """Get the URL of a svg icon

        Return
        ------
        path: str
            Path to the icon (SVG format)
        """
        return os.path.join(self.theme_dir, f'{name}.svg')  

    def style(self, name):
        """Load a stylesheet from a qss file

        Parameters
        ----------
        name: str
            Name of the qss file without extension

        """
        return os.path.join(self.theme_dir, f'{name}.qss')

    def set_style(self, widget, name):
        """Set a style to a specific widget

        Parameters
        ----------
        widget: QWidget
            Widget to style
        name: str
            Name of the stylesheet qss file

        """
        widget.setStyleSheet(self.style(name))

    def set_stylesheet(self, app, sheet_names):
        style_str = ''
        for sheet_name in sheet_names:
            file = open(self.style(sheet_name),mode='r')
            style_str += file.read()
            file.close()

        app.setStyleSheet(style_str)    


class BiThemeAccess:
    """Singleton to access the theme

    Parameters
    ----------
    config_file
        JSON file where the config is stored

    Raises
    ------
    Exception: if multiple instantiation of the Config is tried

    """

    __instance = None

    def __init__(self, theme_dir=''):
        """ Virtually private constructor. """
        BiThemeAccess.__instance = BiTheme(theme_dir)

    @staticmethod
    def instance():
        """ Static access method to the Config. """
        if BiThemeAccess.__instance is None:
            BiThemeAccess.__instance = BiTheme()
        return BiThemeAccess.__instance   
     