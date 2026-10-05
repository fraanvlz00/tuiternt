import tkinter as tk
from tkinter import ttk, messagebox

from service.usuario_service import (
    obtener_usuario_por_nombre,
    crear_usuario
)


class Login_interfaz(ttk.Frame):

    def __init__(self, parent, iniciar_sesion):
        super().__init__(parent)

        self.iniciar_sesion = iniciar_sesion

        ttk.Label(
            self,
            text="tuitern't",
            font=("Arial", 28, "bold")
        ).pack(pady=(100, 20))

        ttk.Label(
            self,
            text="Nombre de usuario"
        ).pack(pady=5)

        self.nombre_usuario = ttk.Entry(
            self,
            width=30
        )
        self.nombre_usuario.pack(pady=5)

        ttk.Button(
            self,
            text="Iniciar sesión",
            command=self.login
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Crear usuario",
            command=self.abrir_registro
        ).pack(pady=5)


    def login(self):
        nombre = self.nombre_usuario.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Inicio de sesión",
                "Ingresa tu nombre de usuario"
            )
            return

        usuario = obtener_usuario_por_nombre(nombre)

        if usuario is None:
            messagebox.showerror(
                "Inicio de sesión",
                "El usuario no existe"
            )
            return

        self.iniciar_sesion(
            int(usuario["id"]),
            usuario
        )


    def abrir_registro(self):
        ventana_registro = tk.Toplevel(self)

        ventana_registro.title("Crear usuario")
        ventana_registro.geometry("420x350")
        ventana_registro.resizable(False, False)

        ttk.Label(
            ventana_registro,
            text="Crear usuario",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        formulario = ttk.Frame(ventana_registro)
        formulario.pack(padx=20, pady=10)

        ttk.Label(
            formulario,
            text="Nombre de usuario:"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

        entrada_nombre = ttk.Entry(
            formulario,
            width=28
        )
        entrada_nombre.grid(row=0, column=1, padx=10, pady=8)

        ttk.Label(
            formulario,
            text="Correo electrónico:"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

        entrada_correo = ttk.Entry(
            formulario,
            width=28
        )
        entrada_correo.grid(row=1, column=1, padx=10, pady=8)

        ttk.Label(
            formulario,
            text="Edad:"
        ).grid(row=2, column=0, padx=10, pady=8, sticky="w")

        entrada_edad = ttk.Entry(
            formulario,
            width=28
        )
        entrada_edad.grid(row=2, column=1, padx=10, pady=8)

        ttk.Label(
            formulario,
            text="Ciudad:"
        ).grid(row=3, column=0, padx=10, pady=8, sticky="w")

        entrada_ciudad = ttk.Entry(
            formulario,
            width=28
        )
        entrada_ciudad.grid(row=3, column=1, padx=10, pady=8)

        def registrar():
            nombre = entrada_nombre.get().strip()
            correo = entrada_correo.get().strip()
            edad = entrada_edad.get().strip()
            ciudad = entrada_ciudad.get().strip()

            if not nombre or not correo or not edad or not ciudad:
                messagebox.showwarning(
                    "Registro",
                    "Debes completar todos los campos"
                )
                return

            if not edad.isdigit():
                messagebox.showwarning(
                    "Registro",
                    "La edad debe ser un número"
                )
                return

            usuario_existente = obtener_usuario_por_nombre(nombre)

            if usuario_existente is not None:
                messagebox.showerror(
                    "Registro",
                    "Ese nombre de usuario ya existe"
                )
                return

            usuario = crear_usuario(
                nombre,
                correo,
                int(edad),
                ciudad
            )
            
            ventana_registro.destroy()

            messagebox.showinfo(
                "Registro",
                "Usuario creado correctamente"
            )


            self.iniciar_sesion(
                int(usuario["id"]),
                usuario
            )

        ttk.Button(
            ventana_registro,
            text="Registrarse",
            command=registrar
        ).pack(pady=20)