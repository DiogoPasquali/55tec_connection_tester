import socket


class PortsChecker:
    def __init__(self, received_ports, host_url="localhost"):
        self.host = host_url
        self.ports = received_ports

    def get_opened_ports(self):
        opened_ports = []

        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            results = sock.connect_ex((self.host, port))
            print(results)
            if results == 0:
                opened_ports.append(port)
            sock.close()
        return opened_ports

    def get_missing_ports(self):
        opened_ports = self.get_opened_ports()
        missing_ports = [port for port in self.ports if port not in opened_ports]
        return missing_ports
