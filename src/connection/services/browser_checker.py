import requests
from user_agent import generate_user_agent
from .logger import Logger


class BrowserInfo:
    """
    Class for extracting browser information.
    """

    def __init__(self, path):
        """
        Initializes an instance of the BrowserInfo class.
        """
        self.user_agent = generate_user_agent()
        self.logger = Logger(path)

    def get_browser_info(self):
        """
        Gets the user's browser information.

        Returns:
            Tuple containing browser name and version.
        """
        browser_info = self.user_agent.split('/')[1].split(' ')
        browser_name = browser_info[0]
        browser_version = browser_info[1]
        self.logger.log("Browser version")
        self.logger.log(f"Browser: {browser_name} version: {browser_version}")
        return browser_name.strip(), browser_version.strip()

    @staticmethod
    def check_latest_version():
        url = "https://www.whatismybrowser.com/guides/the-latest-version/chrome"

        try:
            response = requests.get(url)
            response.raise_for_status()

            latest_version = response.text.strip()
            return latest_version

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
