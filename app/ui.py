from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from app.model import Tienda, Producto


class TiendaUI:
    def __init__(self, tienda: Tienda):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()

    def mostrar_menu(self):
        self.consola.print("\n[bold green]Tienda virtual[/bold green]")
        self.consola.print("1. Agregar producto a la tienda")
        self.consola.print("2. Mostarar productos de la tienda")
        self.consola.print("3. Agregar producto al carrito")
        self.consola.print("4. Mostrar carrito de compras")
        self.consola.print("5. Calcular total de compras")
        self.consola.print("6. Salir")

        opcion= Prompt.ask("\nSeleccione una opcion", choices=["1", "2", "3", "4", "5", "6"])
        return opcion

    def ejecutar(self):
        while True:
            opcion= self.mostrar_menu()

            match opcion:
                case "1":
                    self.agregar_producto_a_tienda()
                case "2":
                    self.mostrar_productos_tienda()
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    self.consola.print("hasta luego", style="bold red")
                    break

    def agregar_producto_a_tienda(self):
        nombre: str = Prompt.ask("Nombre del producto")
        precio: float = float(Prompt.ask("Precio del producto"))
        producto: Producto = Producto(nombre, precio)
        self.tienda.agregar_producto(producto)
        self.consola.print(f"[green]{nombre} agregado correctamente[/green]")

    def mostrar_productos_tienda(self):
        if len(self.tienda.productos) == 0:
            self.consola.print("[red]No hay productos agregados[/red]")
            return

        tabla: Table = Table(title="lista de productos", box=box.SQUARE_DOUBLE_HEAD)
        tabla.add_column("#",style="purple")
        tabla.add_column("Nombre",style="cyan")
        tabla.add_column("Precio",style="blue")

        for i in range(len(self.tienda.productos)):
            tabla.add_row(str(i+1), self.tienda.productos[i].nombre, str(self.tienda.productos[i].precio))

        self.consola.print(tabla)