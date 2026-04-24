from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofacama import SofaCama
from services.tienda import TiendaMuebles
from services.catalogo import Catalogo

def mostrar_menu():
    tienda = TiendaMuebles()
    catalogo = Catalogo()

    while True:
        print("\n--- Menú Tienda de Muebles ---")
        print("1. Agregar Silla")
        print("2. Agregar Mesa")
        print("3. Agregar Sofá Cama")
        print("4. Mostrar Inventario")
        print("5. Calcular Total")
        print("6. Ver Catálogo")
        print("7. Buscar en Catálogo")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            silla = Silla("Silla comedor", "Madera", "Blanco", 100, respaldo=True)
            tienda.agregar_mueble(silla)
            print(f"✅ {silla.obtener_descripcion()} agregado al inventario")
            tienda.mostrar_inventario()

        elif opcion == "2":
            mesa = Mesa("Mesa comedor", "Metal", "Negro", 200, forma="rectangular", tamaño="grande", plazas=6)
            tienda.agregar_mueble(mesa)
            print(f"✅ {mesa.obtener_descripcion()} agregado al inventario")
            tienda.mostrar_inventario()

        elif opcion == "3":
            sofacama = SofaCama("Sofá cama", "Tela", "Gris", 500, plazas=3, tamaño="grande")
            tienda.agregar_mueble(sofacama)
            print(f"✅ {sofacama.obtener_descripcion()} agregado al inventario")
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.mostrar_inventario()

        elif opcion == "5":
            total = tienda.calcular_total()
            print(f"💰 Total del inventario: {total}")

        elif opcion == "6":
            print("\n--- Catálogo ---")
            for desc in catalogo.listar_muebles():
                print(desc)

        elif opcion == "7":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = catalogo.buscar_por_nombre(nombre)
            if resultados:
                print("\nResultados:")
                for r in resultados:
                    print(r.obtener_descripcion())
            else:
                print("No se encontraron muebles con ese nombre.")

        elif opcion == "0":
            print("👋 Saliendo de la tienda...")
            break

        else:
            print("❌ Opción inválida, intenta de nuevo.")
