import funciones.funciones
restaurantes_clase = []
restaurantes_lista = {}
historial_restaurantes = {}

class Restaurante:
    def __init__(self, nombre, password, comidas, bebidas, postres, cocineros, reputacion = 0):
        self.nombre = nombre
        self.password = password
        self.comidas = comidas
        self.bebidas = bebidas
        self.postres = postres
        self.cocineros = cocineros
        self.reputacion = reputacion

    def __str__(self):
        return 'nombre:{} reputacion:{}'.format(self.nombre,self.reputacion)

    def aceptar_pedido(self, pedido):
        self.pedido = pedido
        self.cuenta = 0

        for item in self.pedido:
            self.cuenta += item['precio']

        return self.cuenta        

    def cobrar_pedido(self):
        pass

    def asignar_cocinero(self):
        pass

    def preparar_pedido(self):
       pass  

    # Obtener historial de compras
    def historial(nombre):
        contador=0
        for historial in historial_restaurantes.get(nombre):
            print (f"{contador} - {historial}")
            contador=contador+1
    
    # Obtener menu del restaurante
    def menu(categoria, nombre):
        contador=0
        funciones.funciones.borrar_pantalla()
        for menu in restaurantes_lista[nombre][categoria]:
            print(f"{contador} - {menu['nombre']} - Precio: {menu['precio']} €")
            contador=contador+1






