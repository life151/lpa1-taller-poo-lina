from rich.table import Table
from rich.console import Console

console = Console()

class TiendaMuebles:
    def __init__(self):
        self.inventario = []

    def agregar_mueble(self, mueble):
        self.inventario.append(mueble)

    def calcular_total(self):
        return sum(m.calcular_precio() for m in self.inventario)

    def mostrar_inventario(self):
        if not self.inventario:
            console.print("[red]El inventario está vacío[/red]")
            return

        tabla = Table(title="Inventario de Muebles")
        tabla.add_column("Nombre", style="cyan")
        tabla.add_column("Material", style="magenta")
        tabla.add_column("Color", style="green")
        tabla.add_column("Precio", style="yellow")

        for m in self.inventario:
            tabla.add_row(m.nombre, m.material, m.color, str(m.calcular_precio()))

        console.print(tabla)
