import tkinter as tk
from tkinter import ttk, scrolledtext

from service.usuario_service import listar_tweets_siguiendo


class Feed_interfaz(ttk.Frame):

    def __init__(self, parent, usuario_id):
        super().__init__(parent)

        self.usuario_id = usuario_id

        ttk.Label(
            self,
            text="Tu Feed",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Actualizar",
            command=self.actualizar
        ).pack(pady=5)

        self.salida = scrolledtext.ScrolledText(
            self,
            height=25
        )

        self.salida.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.actualizar()

    def actualizar(self):

        tweets = listar_tweets_siguiendo(
            self.usuario_id
        )

        self.salida.delete(
            "1.0",
            tk.END
        )

        if not tweets:
            self.salida.insert(
                tk.END,
                "No hay tweets en tu feed."
            )
            return

        for tweet in tweets:

            self.salida.insert(
                tk.END,
                f'Usuario {tweet["usuario_id"]}\n'
                f'{tweet["mensaje"]}\n'
                f'{tweet["fecha"]}\n'
                f'-------------------------\n'
            )