"""BioImageIT framework definition.

This module contains contains the base classes that define the 
GUI framework. The framework allows avent programing using BiActuators that 
exange BiActions. The application states are stored in BiContainers.
BiComponents are particular BiActuators that contains graphical interface
components (or widgets)

Classes
------- 
BiActuator
BiContainer
BiAction
BiComponent
BiConnectome
"""

class BiActuator:
    """Actuator base class

    An actuator is an object that can emit and receive actions.
    The update method is called when a action is recived 
    
    """
    def __init__(self):
        super().__init__()
        self.name = 'BiActuator'
        self.container = None

    def update(self, action):
        """Implements the actions to perform

        All the actions should be implemented as callback function whose
        names are '{action.emitter.name}_{action.name}'

        Parameters
        ----------
        action: BiAction
            catched action
        
        """
        method_name = f'{action.emitter.name}_{action.name}'
        if hasattr(self.__class__, method_name) and callable(getattr(self.__class__, method_name)):
            getattr(self, method_name)(action)
                            

class BiContainer:
    """Container of states

    This object allows to store a component states and possible actions

    Actions names should be defined as class string attributes and states data as
    object attributes

    Attributes
    ----------
    name: str
        Unique name to identify the container
    
    """  
    def __init__(self):
        self.name = 'BiContainer'
        self.actuators = []

    def actions(self):
        dict_actions = self.__class__.__dict__
        actions = {}
        for key in dict_actions:
            if not key.startswith('__') and isinstance(dict_actions[key], str):
                actions[key] = dict_actions[key]
        return actions 

    def register(self, obj):
        """Register an Actuator to this Actionable

        Parameters
        ----------
        obj: BiActuator
            Actuator to register

        """
        self.actuators.append(obj)

    def emit(self, action_name, state=None, emitter=None):
        """Emit an action

        Parameters
        ----------
        state: BiContainer
            State of the actionable
        action_name: str
            Unique name of the action
        
        """
        _emitter = emitter
        if emitter is None:
            _emitter = self

        action = BiAction(action_name, state, _emitter)
        for actuator in self.actuators:
            if isinstance(actuator, BiActuator):
                print('comes from an actuator call update')
                actuator.update(action)
            else:
                print('is not an actuator call as a method')    
                actuator(action)     


class BiAction:
    """Action container

    An action is an object emitter by Actuators

    Attributes
    ----------
    state: BiContainer
        Modified state
    name: str
        Name of the action. It identify the action

    """
    def __init__(self, name, state):
        self.name = name
        self.state = state 


class BiComponent(BiActuator):
    """Base GUI component
    
    Components are actionable widgets for the graphical interface

    """
    def __init__(self):
        super().__init__()
        self.name = 'BiWidget'    
        self.widget = None # QWidget

    def get_widget(self):  
        return self.widget   


class BiConnectomeContainer:
    """Container fot the connectome"""
    def __init__(self, theme_dir=''):
        self.connections = {}   

    def connect(self, container, actuator):
        # do the connection
        container.register(actuator)
        actuator.container = container

        # add to the list
        if container in self.connections:
            self.connections[container].append(actuator) 
        else:
            self.connections[container] = [actuator]          


class BiConnectome:
    """Singleton to access the connectome"""
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        BiConnectome.__instance = BiConnectomeContainer()

    @staticmethod
    def instance():
        """ Static access method to the Config. """
        if BiConnectome.__instance is None:
            BiConnectome.__instance = BiConnectomeContainer()
        return BiConnectome.__instance  

    @staticmethod
    def connect(container, actuator):
        BiConnectome.instance().connect(container, actuator)
