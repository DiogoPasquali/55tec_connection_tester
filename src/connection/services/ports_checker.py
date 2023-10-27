import socket


class PortsChecker:
    """
    Class for checking the status of ports on a specified host.
    """
    def __init__(self, received_ports, host_url="localhost"):
        """
        Initializes an instance of the PortsChecker class.

        Parameters:
            - received_ports (list): List of ports to be checked.
            - host_url (str, optional): Host URL where the ports will be checked. Default is "localhost".
        """
        self.host = host_url
        self.ports = received_ports

    def get_opened_ports(self):
        """
        Checks if the specified ports are open on the host.

        Returns:
            List of open ports.
        """
        opened_ports = []

        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            results = sock.connect_ex((self.host, port))
            if results == 0:
                opened_ports.append(port)
            sock.close()

        return opened_ports

    def get_missing_ports(self):
        """
        Retrieves the list of ports that are not open on the host.

        Returns:
            List of missing ports.
        """
        opened_ports = self.get_opened_ports()
        missing_ports = [port for port in self.ports if port not in opened_ports]
        return missing_ports
