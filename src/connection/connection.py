from .services.ports_checker import PortsChecker
from .services.notification_screen import NotificationScreen
from .services.health_check import HealthCheck


class Connection:
    """
    Class representing a connection for monitoring ports and system health.
    """
    def __init__(self, user, path):
        """
        Initializes an instance of the Connection class.

        Parameters:
            - user (dict): User configuration and monitoring details.
            - path (str): Path to the directory for logs and notifications.
        """
        self.state_user = user
        self.port_checker = None
        self.health_checker = None
        self.path = path
        self.get_monitoring()

    def get_monitoring(self) -> None:
        """
        Sets up the port checker and health checker based on user configuration.
        """
        user_config = self.state_user['config_monitoring']["connection"]
        self.port_checker = PortsChecker(received_ports=user_config["ports"])
        self.health_checker = HealthCheck(self.port_checker, self.path)

    def stop(self):
        """
        Stops the connection and monitoring process.
        """
        if self.port_checker is not None:
            print('Received stop signal')

    def start(self):
        """
        Starts the monitoring process and displays notifications for missing ports.
        """
        missing_ports = self.port_checker.get_missing_ports()
        if len(missing_ports) > 0:
            ns = NotificationScreen(missing_ports=missing_ports)
            ns.show()

        self.health_checker.health_check()
