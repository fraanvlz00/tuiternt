import tkinter as tk
from tkinter import ttk, messagebox

from service.tweet_service import (
    publicar_tweet,
    eliminar_tweet
)

from service.usuario_service import (
    listar_tweets_propios
)


class Tweets_interfaz(ttk.Frame):

    def __init__(self, parent, usuario_id):
        super().__init__(parent)

        self.usuario_id = usuario_id

        # TITULO
        ttk.Label(
            self,
            text="Mis Tweets",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        # PUBLICAR TWEET
        self.mensaje = ttk.Entry(
            self,
            width=60
        )
        self.mensaje.pack(pady=5)

        ttk.Button(
            self,
            text="Publicar",
            command=self.publicar
        ).pack(pady=5)

        # AQUÍ VA EL CONTENEDOR
        self.contenedor_tweets = ttk.Frame(self)

        self.contenedor_tweets.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # cargar tweets al abrir
        self.cargar_tweets()


    def publicar(self):
        mensaje = self.mensaje.get()

        if not mensaje.strip():
            messagebox.showwarning(
                "Tweet",
                "Escribe un mensaje"
            )
            return

        publicar_tweet(
            self.usuario_id,
            mensaje
        )

        self.mensaje.delete(
            0,
            tk.END
        )

        self.cargar_tweets()


    def cargar_tweets(self):
        tweets = listar_tweets_propios(
            self.usuario_id
        )

        # borrar lo que estaba mostrado antes
        for widget in self.contenedor_tweets.winfo_children():
            widget.destroy()

        if not tweets:
            ttk.Label(
                self.contenedor_tweets,
                text="No tienes tweets publicados"
            ).pack(pady=20)

            return

        for tweet in tweets:

            fila = ttk.Frame(
                self.contenedor_tweets
            )

            fila.pack(
                fill="x",
                padx=10,
                pady=8
            )

            ttk.Label(
                fila,
                text=(
                    f'{tweet["mensaje"]}\n'
                    f'{tweet["fecha"]}'
                ),
                justify="left"
            ).pack(
                side="left",
                padx=10
            )

            ttk.Button(
                fila,
                text="Eliminar",
                command=lambda id=tweet["id"]: self.eliminar(id)
            ).pack(
                side="right",
                padx=10
            )


    def eliminar(self, tweet_id):
        eliminar_tweet(
            self.usuario_id,
            tweet_id
        )

        self.cargar_tweets()