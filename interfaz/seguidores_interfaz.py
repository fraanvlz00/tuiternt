import tkinter as tk
from tkinter import ttk

from service.usuario_service import (
    listar_usuarios,
    siguiendo_usuario,
    eliminar_siguiendo_usuario,
    esta_siguiendo
)


class Seguidores_interfaz(ttk.Frame):

    def __init__(self, parent, usuario_id):
        super().__init__(parent)

        self.usuario_id = usuario_id

        ttk.Label(
            self,
            text="Usuarios",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        ttk.Label(
            self,
            text="Sigue a otros usuarios de tuitern't"
        ).pack(pady=(0, 10))

        self.contenedor = ttk.Frame(self)

        self.contenedor.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        ttk.Button(
            self,
            text="Actualizar usuarios",
            command=self.cargar_usuarios
        ).pack(pady=10)

        self.cargar_usuarios()

    def cargar_usuarios(self):

        # Eliminar elementos anteriores
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        usuarios = listar_usuarios()

        for usuario in usuarios:

            usuario_id = int(usuario["id"])

            # No mostrar al propio usuario
            if usuario_id == self.usuario_id:
                continue

            fila = ttk.Frame(self.contenedor)

            fila.pack(
                fill="x",
                pady=8
            )

            nombre = usuario.get(
                "nombre_usuario",
                f"Usuario {usuario_id}"
            )

            ciudad = usuario.get(
                "ciudad",
                ""
            )

            ttk.Label(
                fila,
                text=f"@{nombre}",
                font=("Arial", 12, "bold"),
                width=20
            ).pack(
                side="left",
                padx=10
            )

            ttk.Label(
                fila,
                text=ciudad,
                width=15
            ).pack(
                side="left",
                padx=10
            )

            siguiendo = esta_siguiendo(
                self.usuario_id,
                usuario_id
            )

            if siguiendo:

                boton = ttk.Button(
                    fila,
                    text="Dejar de seguir",
                    command=lambda id=usuario_id:
                    self.dejar_de_seguir(id)
                )

            else:

                boton = ttk.Button(
                    fila,
                    text="Seguir",
                    command=lambda id=usuario_id:
                    self.seguir(id)
                )

            boton.pack(
                side="right",
                padx=10
            )

    def seguir(self, usuario_seguido_id):

        siguiendo_usuario(
            self.usuario_id,
            usuario_seguido_id
        )

        self.cargar_usuarios()

    def dejar_de_seguir(self, usuario_seguido_id):

        eliminar_siguiendo_usuario(
            self.usuario_id,
            usuario_seguido_id
        )

        self.cargar_usuarios()