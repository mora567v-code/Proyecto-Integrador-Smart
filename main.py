# -*- coding: utf-8 -*-
# Proyecto Integrador - Fundamentos de Programación
# Nombre: Víctor Mora


opcion = 0
ganancias_totales = 0
contador_citas = 0


servicios = ["Corte de Cabello Clásico", "Servicio Completo (Barba + Corte)", "Tinte / Cambio de Color", "Manicura Básica"]
precios   = [10, 18, 25, 12]

inventario = {
    "Cera Capilar":        {"stock": 12, "unidad": "unidades", "minimo": 3},
    "Shampoo Especial":    {"stock": 6,  "unidad": "litros",   "minimo": 2},
    "Tintes de Cabello":   {"stock": 4,  "unidad": "unidades", "minimo": 3},
    "Toallas Desechables": {"stock": 15, "unidad": "paquetes", "minimo": 5},
}

insumos_por_servicio = {
    2: "Cera Capilar",
    3: "Tintes de Cabello",
}


while opcion != 5:
    print("\n========================================")
    print("      SMARTCUT MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Registrar Nueva Cita")
    print("2. Ver Inventario de Insumos")
    print("3. Ver Reporte de Caja Diario")
    print("4. Ver Total de Clientes Atendidos")
    print("5. Salir del Sistema")
    print("========================================")

    opcion = int(input("Por favor, seleccione una opción (1-5): "))

   
    if opcion == 1:
        print("\n--- REGISTRAR NUEVA CITA ---")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        print("\nSeleccione el tipo de servicio:")
        for i in range(len(servicios)):
            print(str(i+1) + ". " + servicios[i] + " ($" + str(precios[i]) + ".00)")

        tipo_servicio = int(input("Ingrese el número del servicio: "))

        if tipo_servicio >= 1 and tipo_servicio <= 4:
            servicio_nombre = servicios[tipo_servicio - 1]
            precio = precios[tipo_servicio - 1]

            # Verificar si el servicio necesita un insumo
            if tipo_servicio in insumos_por_servicio:
                insumo = insumos_por_servicio[tipo_servicio]
                if inventario[insumo]["stock"] > 0:
                    inventario[insumo]["stock"] = inventario[insumo]["stock"] - 1
                    ganancias_totales = ganancias_totales + precio
                    contador_citas = contador_citas + 1
                    print("Servicio seleccionado: " + servicio_nombre)
                    print("Cita registrada para: " + nombre_cliente)
                else:
                    print("No se pudo registrar, no queda " + insumo + " en el inventario.")
            else:
                ganancias_totales = ganancias_totales + precio
                contador_citas = contador_citas + 1
                print("Servicio seleccionado: " + servicio_nombre)
                print("Cita registrada para: " + nombre_cliente)
        else:
            print("Opción de servicio no válida.")

    elif opcion == 2:
        print("\n--- CONTROL DE INSUMOS ---")
        for nombre, datos in inventario.items():
            print(nombre + ": " + str(datos["stock"]) + " " + datos["unidad"])
            if datos["stock"] <= datos["minimo"]:
                print("  ⚠️  Alerta: Stock bajo. Hay que comprar.")

    elif opcion == 3:
        print("\n--- REPORTE DE CAJA ---")
        print("Total recaudado hoy: $", ganancias_totales)

    elif opcion == 4:
        print("\n--- CLIENTES ATENDIDOS ---")
        print("Número de clientes registrados hoy:", contador_citas)

    elif opcion == 5:
        print("\nSaliendo del sistema...")
        print("¡Gracias por usar SmartCut!")

    else:
        print("Opción incorrecta. Intente de nuevo.")

print("\n--- PROGRAMA FINALIZADO ---")
