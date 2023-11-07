import speedtest
from .logger import Logger


class InternetSpeedTester:
    """
    Class for measuring internet speed using speedtest-cli.
    """

    def __init__(self, path):
        """
        Initializes an instance of the InternetSpeedTester class.
        """
        self.st = speedtest.Speedtest()
        self.logger = Logger(path)

    def measure_speed(self):
        """
        Measures internet speed and returns download and upload speeds in Mbps.

        Returns:
            Tuple containing download speed and upload speed (in Mbps).
        """
        download_speed = self.st.download() / (1024 * 1024)
        upload_speed = self.st.upload() / (1024 * 1024)

        self.logger.log("Internet speed")
        self.logger.log(f"Download speed: {download_speed}")
        self.logger.log(f"Upload speed: {upload_speed}")
