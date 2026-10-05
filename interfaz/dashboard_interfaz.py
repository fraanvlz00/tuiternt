from tkinter import ttk

from interfaz.feed_interfaz import Feed_interfaz
from interfaz.tweets_interfaz import Tweets_interfaz
from interfaz.seguidores_interfaz import Seguidores_interfaz


class Dashboard_interfaz(ttk.Frame):

    def __init__(
        self,
        parent,
        usuario_id,
        usuario,
        cerrar_sesion
    ):
        super().__init__(parent)

        self.usuario_id = usuario_id

        # Cabecera
        cabecera = ttk.Frame(self)
        cabecera.pack(
            fill="x",
            padx=15,
            pady=10
        )

        nombre = usuario.get(
            "nombre_usuario",
            f"Usuario {usuario_id}"
        )

        ttk.Label(
            cabecera,
            text=f"tuitern't   |   @{nombre}",
            font=("Arial", 16, "bold")
        ).pack(side="left")

        ttk.Button(
            cabecera,
            text="Cerrar sesión",
            command=cerrar_sesion
        ).pack(side="right")

        # Pestañas
        notebook = ttk.Notebook(self)

        feed = Feed_interfaz(
            notebook,
            usuario_id
        )

        tweets = Tweets_interfaz(
            notebook,
            usuario_id
        )

        seguimiento = Seguidores_interfaz(
            notebook,
            usuario_id
        )

        notebook.add(
            feed,
            text="Feed"
        )

        notebook.add(
            tweets,
            text="Mis Tweets"
        )

        notebook.add(
            seguimiento,
            text="Siguiendo"
        )

        notebook.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )