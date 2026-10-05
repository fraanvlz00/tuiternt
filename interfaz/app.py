import tkinter as tk

from interfaz.login_interfaz import Login_interfaz
from interfaz.dashboard_interfaz import Dashboard_interfaz


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("tuitern't")
        self.geometry("850x650")

        self.usuario_id = None
        self.usuario = None

        self.mostrar_login()

    def limpiar(self):

        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_login(self):

        self.limpiar()

        login = Login_interfaz(
            self,
            self.iniciar_sesion
        )

        login.pack(
            fill="both",
            expand=True
        )

    def iniciar_sesion(self, usuario_id, usuario):

        self.usuario_id = usuario_id
        self.usuario = usuario

        self.mostrar_dashboard()

    def mostrar_dashboard(self):

        self.limpiar()

        dashboard = Dashboard_interfaz(
            self,
            self.usuario_id,
            self.usuario,
            self.cerrar_sesion
        )

        dashboard.pack(
            fill="both",
            expand=True
        )

    def cerrar_sesion(self):

        self.usuario_id = None
        self.usuario = None

        self.mostrar_login()