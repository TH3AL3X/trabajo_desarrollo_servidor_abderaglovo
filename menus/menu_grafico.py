import base_de_datos.database, funciones.funciones, time, os, clases.cliente, clases.restaurante

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(f"{os.getcwd()}\\theme\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ventana = Tk()

def menu_principal_grafico_inicio_sesion(): # login
    ventana.geometry("450x491")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Abdera Glovo")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_registro.png"))
    boton_registro = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("registro"),
        relief="flat"
    )
    boton_registro.place(
        x=94.0,
        y=388.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_sesion.png"))

    boton_inicio_sesion = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciar_sesion(usuario.get(), contraseña.get()),
        relief="flat"
    )
    boton_inicio_sesion.place(
        x=94.0,
        y=338.0,
        width=262.0,
        height=43.0
    )

    usuario_texto = Label(ventana, font="Helvetica 20", text="Usuario")
    usuario_texto.place(x=94.0,
                        y=125.0,
                        width=262.0,
                        height=43.0)

    usuario = Entry(ventana, font="Helvetica 20", background="#ccc6c6")
    usuario.place(x=94.0,
                  y=170.0,
                  width=262.0,
                  height=43.0)

    contraseña_texto = Label(ventana, font="Helvetica 20", text="Contraseña")
    contraseña_texto.place(x=94.0,
                           y=215.0,
                           width=262.0,
                           height=43.0)

    contraseña = Entry(ventana, font="Helvetica 20",
                       background="#ccc6c6", show="*")
    contraseña.place(x=94.0,
                     y=260.0,
                     width=262.0,
                     height=43.0)

    ventana.resizable(False, False)
    ventana.mainloop()

def menu_usuario_grafico(usuario): # usuario
    clases.cliente.lista_compra.clear()
    ventana.geometry("450x491")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Menu Principal")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_pedido.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_restaurantes(usuario),
        relief="flat"
    )
    button_1.place(
        x=94.0,
        y=277.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_credito.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_añadir_saldo(usuario, False),
        relief="flat"
    )
    button_2.place(
        x=94.0,
        y=224.0,
        width=262.0,
        height=43.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("boton_historial.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_historial(usuario),
        relief="flat"
    )
    button_3.place(
        x=94.0,
        y=171.0,
        width=262.0,
        height=43.0
    )
    texto_bienvenido = Label(ventana, font="Helvetica 15", fg="#ffffff",
                             background="#6aa84f", text=f"Bienvenido, {usuario}..")
    texto_bienvenido.place(x=80.0,
                           y=60.0,
                           width=300.0,
                           height=43.0)

    ventana.resizable(False, False)
    ventana.mainloop()

def menu_historial(usuario):
    ventana.title("Historial")
    ventana.geometry("450x491")
    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_regresar.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_usuario_grafico(usuario),
        relief="flat"
    )
    button_1.place(
        x=94.0,
        y=351.0,
        width=262.0,
        height=43.0
    )
    lista = ""

    for mostrar in clases.cliente.historial_clientes[usuario]:
        lista+=str(mostrar).replace("Producto:", "\nProducto:")+"\n"
    
    Texto = Label(
        font="Helvetica 10",
        text=lista
    )
    Texto.place(x=70)
    
    ventana.resizable(False, False)
    ventana.mainloop()

def menu_restaurantes(usuario):
    ventana.title("Restaurantes")
    ventana.geometry("450x300")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_continuar.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_pedidos(combo.get(), usuario),
        relief="flat"
    )
    button_1.place(
        x=94.0,
        y=190.0,
        width=262.0,
        height=43.0
    )
    lista = []

    for restaurantes in clases.restaurante.restaurantes_lista.keys():
        lista.append(restaurantes)

    texto = Label(ventana, text="Selecciona el restaurante", font="20")
    texto.place(x=90, y=90)

    combo = ttk.Combobox(
        state="readonly",
        values=lista,
        font="Helvetica 20"
    )
    combo.place(x=80.0, y=130.0, width=300.0, height=50.0)
    
    ventana.resizable(False, False)
    ventana.mainloop()

def menu_pedidos(restaurante, usuario):
    ventana.title(f"Pedidos {restaurante}")
    ventana.geometry("450x491")
    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_cancelar.png"))
    boton_cancelar = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_usuario_grafico(usuario),
        relief="flat"
    )
    boton_cancelar.place(
        x=94.0,
        y=321.0,
        width=262.0,
        height=43.0
    )

    button_ver_carrito = PhotoImage(
        file=relative_to_assets("boton_carrito.png"))
    boton_carrito = Button(
        image=button_ver_carrito,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_categoria(usuario, restaurante, "comidas"),
        relief="flat"
    )
    boton_carrito.place(
        x=94.0,
        y=34.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_comidas.png"))
    boton_comidas = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_categoria(usuario, restaurante, "comidas"),
        relief="flat"
    )
    boton_comidas.place(
        x=94.0,
        y=86.0,
        width=262.0,
        height=43.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("boton_bebidas.png"))
    boton_bebidas = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_categoria(usuario, restaurante, "bebidas"),
        relief="flat"
    )
    boton_bebidas.place(
        x=94.0,
        y=139.0,
        width=262.0,
        height=43.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("boton_postres.png"))
    boton_postres = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_categoria(usuario, restaurante, "postres"),
        relief="flat"
    )
    boton_postres.place(
        x=94.0,
        y=192.0,
        width=262.0,
        height=43.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("boton_completar.png"))
    boton_completar = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("completar"),
        relief="flat"
    )
    boton_completar.place(
        x=94.0,
        y=374.0,
        width=262.0,
        height=43.0
    )
    ventana.resizable(False, False)
    ventana.mainloop()

def iniciar_sesion(usuario, password):
    if(base_de_datos.database.Usuarios.comprobacion_usuario_sesion(usuario, password)):
        menu_usuario_grafico(usuario)
    else:
        error_texto = Label(ventana, font="Helvetica 15", fg="#ffffff",
                            background="#2986cc", text="Error, Datos incorrectos")
        error_texto.place(x=80.0,
                          y=60.0,
                          width=300.0,
                          height=43.0)

def menu_añadir_saldo(usuario, recargar): # usuario

    clases.cliente.lista_compra.clear()
    ventana.geometry("450x300")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Añadir Saldo")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_regresar.png"))
    boton_cancelar = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: menu_usuario_grafico(usuario),
        relief="flat"
    )
    boton_cancelar.place(
        x=94.0,
        y=208.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_continuar.png"))

    boton_saldo = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [clases.cliente.Cliente.ingreso(usuario, float(saldo.get())), menu_añadir_saldo(usuario, True)],
        relief="flat"
    )
    boton_saldo.place(
        x=94.0,
        y=158.0,
        width=262.0,
        height=43.0
    )

    
    saldo_texto = Label(ventana, font="Helvetica 15", text=f"Saldo Actual: {clases.cliente.Cliente.saldo(usuario)}")
    saldo_texto.place(x=94.0, y=50.0)

    saldo = Entry(ventana, font="Helvetica 20", background="#ccc6c6")
    saldo.place(x=94.0,
                  y=90.0,
                  width=262.0,
                  height=43.0)
    
    if(recargar):
        texto_saldo_añadido = Label(ventana, font="Helvetica 20", fg="#ffffff",
                                background="#6aa84f", text=f"Se completo el proceso...")
        texto_saldo_añadido.place(x=80.0,
                            y=10.0)

    ventana.resizable(False, False)
    ventana.mainloop()

def menu_categoria(usuario, nombre_restaurante, categoria):
    ventana.title("Categoria selección")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_añadir.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [ clases.cliente.Cliente.pedido_añadir(nombre_restaurante, guardar_id, "postres", int(cantidad.get())), menu_pedidos(nombre_restaurante, usuario)  ],
        relief="flat"
    )
    button_1.place(
        x=94.0,
        y=351.0,
        width=262.0,
        height=43.0
    )

    lista = {}
    dictionary_a_lista = []
    contador = 0

    for menu in clases.restaurante.restaurantes_lista[nombre_restaurante][categoria]:
        lista[contador] = { f"{menu['nombre']} - Precio: {menu['precio']} €" }
        dictionary_a_lista.append(f"{menu['nombre']} - Precio: {menu['precio']} €")
        contador=contador+1

    texto = Label(ventana, font="Helvetica 15", text="Producto")
    texto.place(x=94.0,y=125.0)
    
    combo = ttk.Combobox(
        state="readonly",
        values=dictionary_a_lista,
        font="Helvetica 20"
    )
    combo.place(x=94.0,y=170.0)

    guardar_id = 0
    for name, values in lista.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if values == combo.get():
            guardar_id=int(name)

    texto_cantidad = Label(ventana, font="Helvetica 15", text="Cantidad")
    texto_cantidad.place(x=94.0,
                           y=215.0)

    cantidad = Entry(ventana, font="Helvetica 20",
                       background="#ccc6c6")
    cantidad.place(x=94.0,y=260.0)

    ventana.resizable(False, False)
    ventana.mainloop()