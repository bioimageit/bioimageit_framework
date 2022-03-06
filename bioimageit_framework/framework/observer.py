from qtpy.QtWidgets import QMessageBox


class BiGuiObserver:
    """Observer that display messages in the GUI popup windows

    """

    def __init__(self, debug=True):
        self.jobs_id = []
        self.debug = debug

    def new_job(self, job_id: int):
        """Add a new job id

        Parameters
        ----------
        job_id: int
            unique ID of the new job

        """
        self.jobs_id.append(job_id)

    def notify(self, message: str, job_id: int = 0):
        """Function called by the observable to notify or log any information

        Parameters
        ----------
        message: str
            Information message
        job_id: int
            unique ID of the job. 0 is main app, and positive is a subprocess

        """
        prefix = ''
        if job_id > 0:
            prefix = f'job {job_id}:'

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f'{prefix} {message}')
        msgBox.setWindowTitle("Message")
        msgBox.exec()

    def notify_warning(self, message: str, job_id: int = 0):
        """Function called by the observable to warn

        Parameters
        ----------
        message
            Warning message
        job_id: int
            unique ID of the job. 0 is main app, and positive is a subprocess

        """
        prefix = ''
        if job_id > 0:
            prefix = f'job {job_id}:'

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(f'{prefix} {message}')
        msgBox.setWindowTitle("Warning")
        msgBox.exec()

    def notify_error(self, message: str, job_id: int = 0):
        """Function called by the observable to warn

        Parameters
        ----------
        message
            Warning message
        job_id: int
            unique ID of the job. 0 is main app, and positive is a subprocess

        """
        prefix = ''
        if job_id > 0:
            prefix = f'job {job_id}:'

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(f'{prefix} {message}')
        msgBox.setWindowTitle("Error")
        msgBox.exec()

    def notify_progress(self, progress: int, message: int = '', job_id: int = 0):
        """Function called by the observable to notify progress

        Parameters
        ----------
        progress
            Data describing the progress
        message
            Message to describe the progress step
        job_id: int
            unique ID of the job. 0 is main app, and positive is a subprocess

        """
        pass
