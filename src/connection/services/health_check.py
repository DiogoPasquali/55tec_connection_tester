import time
from .logger import Logger


class HealthCheck:
    """
    Class that performs periodic health checks on system ports.
    """

    def __init__(self, checker, path):
        """
        Initializes an instance of the HealthCheck class.

        Parameters:
            - checker (object): Object responsible for checking the ports.
            - path (str): Path to the directory where the error log file will be created.
        """
        self.ports_checker = checker
        self.path = path
        self.logger = Logger(path)

    def health_check(self):
        """
        Performs periodic health checks on the ports.

        Operation:
            1. Sets up the logging system to record error messages in a file at the specified path.
            2. In an infinite loop:
                - Retrieves the list of open ports and missing ports using the 'checker' object.
                - Logs the open ports in the log file.
                - If there are missing ports, logs an error in the log file. Otherwise, logs an informative message.
                - Waits for 5 minutes before performing the next check.

        Exceptions:
            - Any exception raised within the 'try' block is logged as an error in the log file.
        """

        while True:
            try:
                opened_ports = self.ports_checker.get_opened_ports()
                missing_ports = self.ports_checker.get_missing_ports()
                self.logger.log(f'Open ports: {opened_ports}')

                if missing_ports:
                    self.logger.error(f'Missing ports: {missing_ports}')
                else:
                    self.logger.log('All ports are present in the list.')

                time.sleep(300)

            except Exception as e:
                self.logger.exception(f'Unexpected error: {str(e)}')
