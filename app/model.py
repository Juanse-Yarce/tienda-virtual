class Producto:

    def __init__(self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio

    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"

class Cliente:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.carrito: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)

    def mostrar_carrito(self) -> str:
        carrito_str: str = ""
        for producto in self.carrito:
            carrito_str += producto.mostrar_info() +"\n"
        return carrito_str

    def calcular_total(self) -> float:
        total: float = 0
        for producto in self.carrito:
            total += producto.precio
        return total

class Tienda:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.productos: list[Producto] =[]

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_carrito(self) -> str:
        producto_str: str = ""
        for producto in self.productos:
            producto_str += producto.mostrar_info() +"\n"
        return producto_str