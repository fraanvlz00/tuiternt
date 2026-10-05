import tkinter as tk
from tkinter import ttk, messagebox
from service.usuario_service import crear_usuario


class Usuario_interfaz(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(
            self,
            text="Crear usuario",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        formulario = ttk.Frame(self)
        formulario.pack(pady=10)

        ttk.Label(formulario, text="Nombre de usuario").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )

        self.nombre = ttk.Entry(formulario, width=30)
        self.nombre.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(formulario, text="Correo electrónico").grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )

        self.correo = ttk.Entry(formulario, width=30)
        self.correo.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(formulario, text="Edad").grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )

        self.edad = ttk.Entry(formulario, width=30)
        self.edad.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(formulario, text="Ciudad").grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )

        self.ciudad = ttk.Entry(formulario, width=30)
        self.ciudad.grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(
            self,
            text="Crear usuario",
            command=self.crear_usuario
        ).pack(pady=15)

    def crear_usuario(self):
        nombre = self.nombre.get()
        correo = self.correo.get()
        edad = self.edad.get()
        ciudad = self.ciudad.get()

        if not nombre or not correo or not edad or not ciudad:
            messagebox.showwarning(
                "Datos incompletos",
                "Debes completar todos los campos"
            )
            return

        crear_usuario(
            nombre,
            correo,
            edad,
            ciudad
        )

        messagebox.showinfo(
            "Usuario",
            "Usuario creado correctamente"
        )

        self.nombre.delete(0, tk.END)
        self.correo.delete(0, tk.END)
        self.edad.delete(0, tk.END)
        self.ciudad.delete(0, tk.END)
