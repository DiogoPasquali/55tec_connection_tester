import tkinter as tk


class NotificationScreen:
    """
    Class for displaying a notification screen with information about missing ports.
    """
    def __init__(self, missing_ports=None, browser_version=None):
        """
        Initializes an instance of the NotificationScreen class.

        Parameters:
            - missing_ports (list): List of missing ports to be displayed.
        """
        self.root = tk.Tk()
        self.root.title("Notification of Possible Issues")

        self.label = tk.Label(self.root, text="The following ports are missing:")
        self.label.pack(pady=10)

        self.missing_ports = tk.Label(self.root, text=", ".join(map(str, missing_ports)))
        self.missing_ports.pack(pady=10)

        if browser_version:
            self.label = tk.Label(self.root, text="The browser is incorrect version:")
            self.label.pack(pady=10)

            self.missing_ports = tk.Label(self.root, text=", ".join(map(str, browser_version)))
            self.missing_ports.pack(pady=10)

        self.close_button = tk.Button(self.root, text="Close", command=self.close)
        self.close_button.pack(pady=10)

    def show(self):
        """
        Displays the notification screen.
        """
        self.root.mainloop()

    def close(self):
        """
        Closes the notification screen.
        """
        self.root.destroy()
