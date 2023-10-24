import tkinter as tk


class NotificationScreen:
    def __init__(self, missing_ports):
        self.root = tk.Tk()
        self.root.title("Notificação de possiveis problemas")

        self.label = tk.Label(self.root, text="As seguintes portas estão faltando:")
        self.label.pack(pady=10)

        self.missing_ports = tk.Label(self.root, text=", ".join(map(str, missing_ports)))
        self.missing_ports.pack(pady=10)

        self.close_button = tk.Button(self.root, text="Fechar", command=self.close)
        self.close_button.pack(pady=10)

    def show(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()

