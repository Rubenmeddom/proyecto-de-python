import tkinter as tk
class VentanaNombre(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback es una función que esta ventana llamará
        # una vez presionado el botón para comunicarle el nombre
        # ingresado a la ventana padre.
        self.callback = callback
        self.config(width=300, height=90)
        self.title("Ingresa tu nombre")
        self.caja_nombre = tk.Entry(self, width=20)
        self.caja_nombre.pack(padx=20, pady=20)
        self.boton_listo = tk.Button(
            self,
            text="¡Listo!",
            command=self.boton_listo_presionado
        )
        self.boton_listo.pack(padx=20, pady=20)
        self.grab_set()
   
    def boton_listo_presionado(self):
        # Obtener el dato ingresado y llamar a la función
        # especificada al crear esta ventana.
        self.callback(self.caja_nombre.get())
        # Cerrar la ventana.
        self.destroy()


class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Ventana principal")
        self.boton_solicitar_nombre = tk.Button(
            self,
            text="Solicitar nombre",
            command=self.solicitar_nombre
        )
        self.boton_solicitar_nombre.pack(padx=20, pady=20)
        self.etiqueta_nombre = tk.Label(
            self,
            text="Aún no has ingresado ningún nombre."
        )
        self.etiqueta_nombre.pack(padx=20, pady=20)
    def solicitar_nombre(self):
        # Crear la ventana secundaria y pasar como argumento
        # la función en la cual queremos recibir el dato
        # ingresado.
        VentanaNombre(callback=self.nombre_ingresado)
   
    def nombre_ingresado(self, nombre):
        # Esta función es invocada cuando el usuario presiona el
        # botón "¡Listo!" de la ventana secundaria. El dato
        # ingresado estará en el argumento "nombre".
        self.etiqueta_nombre.config(
            text="Ingresaste el nombre: " + nombre
        )
ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()