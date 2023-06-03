import tkinter as tk

# Ventana principal
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Chatopia")
    
    # Barra de navegación o menú
    menu_bar = tk.Menu(ventana)
    ventana.config(menu=menu_bar)
    
    # Elementos de la barra de navegación o menú
    archivo_menu = tk.Menu(menu_bar, tearoff=0)
    archivo_menu.add_command(label="Salir", command=ventana.quit)
    menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
    
    # Lista de salas disponibles
    lista_salas = tk.Listbox(ventana)
    lista_salas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Área de chat
    area_chat = tk.Text(ventana)
    area_chat.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Botón para crear sala
    boton_crear_sala = tk.Button(ventana, text="Crear Sala", command=ventana_creacion_sala)
    boton_crear_sala.pack(side=tk.TOP)
    
    ventana.mainloop()

# Ventana de inicio de sesión
def ventana_inicio_sesion():
    ventana = tk.Tk()
    ventana.title("Inicio de Sesión")
    
    # Elementos de la ventana de inicio de sesión
    
    # Botón de inicio de sesión
    boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=validar_inicio_sesion)
    boton_iniciar_sesion.pack()
    
    ventana.mainloop()

# Ventana de registro de cuenta
def ventana_registro_cuenta():
    ventana = tk.Tk()
    ventana.title("Registro de Cuenta")
    
    # Elementos de la ventana de registro de cuenta
    
    # Botón de registro de cuenta
    boton_registrar = tk.Button(ventana, text="Registrar Cuenta", command=registrar_cuenta)
    boton_registrar.pack()
    
    ventana.mainloop()

# Ventana de creación de sala
def ventana_creacion_sala():
    ventana = tk.Tk()
    ventana.title("Creación de Sala")
    
    # Elementos de la ventana de creación de sala
    
    # Botón de creación de sala
    boton_crear = tk.Button(ventana, text="Crear", command=crear_sala)
    boton_crear.pack()
    
    ventana.mainloop()

# Ventana de configuración
def ventana_configuracion():
    ventana = tk.Tk()
    ventana.title("Configuración")
    
    # Elementos de la ventana de configuración
    
    # Botón de guardar configuración
    boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_configuracion)
    boton_guardar.pack()
    
    ventana.mainloop()

# Ejecutar la ventana principal
ventana_principal()
