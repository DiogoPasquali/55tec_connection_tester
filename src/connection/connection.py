from .services.ports_checker import PortsChecker
from .services.notification_screen import NotificationScreen


class Connection:
    def __init__(self, user):
        self.state_user = user
        self.port_checker = None
        self.get_monitoring()

    def get_monitoring(self) -> None:
        user_config = self.state_user['config_monitoring']["connection"]
        self.port_checker = PortsChecker(received_ports=user_config["ports"])

    def stop(self):
        if self.port_checker is not None:
            print('recebi sinal de parada')

    def start(self):
        missing_ports = self.port_checker.get_missing_ports()
        if len(missing_ports) > 0:
            ns = NotificationScreen(missing_ports=missing_ports)
            ns.show()
