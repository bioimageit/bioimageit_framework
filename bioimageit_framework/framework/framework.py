"""BioImageIT framework definition.

This module contains contains the base classes that define the 
GUI framework. The framework allows avent programing using BiActuators that 
exange BiActions. The application states are stored in BiContainers.
BiComponents are particular BiActuators that contains graphical interface
components (or widgets)

Classes
------- 
BiNotification
BiAction
BiContainer
BiActuator
BiConnectomeContainer
BiConnectome

"""

class BiNotification:
    """Definition of a notification

    A notification is a signal emitted by a data container 
    to notify actuator of a data or state change  

    Parameters
    ----------
    name: str
        Unique id of the notification
    emitter: BiContainer
        Container that emitted the notification

    """
    def __init__(self, name='', emitter=None):
        self.name = name
        self.emitter = emitter    


class BiAction:
    """Definition of an action

    An action is en event emitted by an actuator for containers. This event
    contains an task for the container.

    Parameters
    ----------
    name: str
        Unique id of the task to be executed by the container
    emitter: BiActuator
        Actuator that emitted the signal
    """        


class BiContainer:
    """Definition of a container

    A container is an object that store the data of a sub-part
    of the application. A container emit notifications when its
    data are updates, and recieve actions from ACtuators to update
    the data.

    """
    def __init__(self):
        self.name = 'container'
        self._actuators = []

    def connect(self, actuator):
        """Connect a new actuator to this container

        The connected actuator will then recieve the notification
        from this container

        """
        self._actuators.append(actuator)

    def _notify(self, name):
        """Emit notification to the connected actuators

        Parameters
        ----------
        name: str
            Unique id of the notification
        """        
        for actuator in self._actuators:
            actuator.update(BiNotification(name, self))

    def update(self, action, args):
        """Update the data when an action is recieved

        This method call a callback method name similarly to 
        the action name

        Parameters
        ----------
        action: BiAction
            Recieved action

        """         
        method_name = f'action_{action.name}'
        if hasattr(self.__class__, method_name) and callable(getattr(self.__class__, method_name)):
            getattr(self, method_name)(action, *args)


class BiActuator:
    def __init__(self):
        self.name = 'actuator'
        self._containers = []

    def connect(self, container):
        """Connect a new container to the actuator

        The container will the recieve the actions from the 
        actuator

        Parameters
        ----------
        container: BiContainer
            Container to connect

        """
        self._containers.append(container) 

    def _emit(self, name, args):
        """Emit an action to the connected containers

        Parameters
        ----------
        name: str
            Unique ID of the actions
        args: tuple
            List of data to be updated

        """ 
        for container in self._containers:
            container.update(BiAction(name, self), args)

    def update(self, notification):
        """Update the actuator when an notification is recieved

        This method call a callback method name similarly to 
        the notification name

        Parameters
        ----------
        notification: BiNotification
            Recieved notification

        """         
        method_name = f'callback_{notification.name}'
        if hasattr(self.__class__, method_name) and callable(getattr(self.__class__, method_name)):
            getattr(self, method_name)(notification)             


class BiConnectomeContainer:
    """Container for the connectome"""
    def __init__(self, theme_dir=''):
        self.connections = {}  # list of all the connections 

    def connect(self, container, actuator):
        # do the connection
        container.connect(actuator)
        actuator.connect(container)

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
