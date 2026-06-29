# Proyecto Integrador
# Nombre: Víctor Mora

opcion = 0
ganancias_totales = 0
contador_citas = 0

stock_cera = 12
stock_shampoo = 6
stock_tintes = 4
stock_toallas = 15


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
        print("1. Corte de Cabello Clásico ($10.00)")
        print("2. Servicio Completo (Barba + Corte) ($18.00)")
        print("3. Tinte / Cambio de Color ($25.00)")
        print("4. Manicura Basica ($12.00)")
        
        tipo_servicio = int(input("Ingrese el número del servicio: "))
        
        
        if tipo_servicio == 1:
            print("Servicio seleccionado: Corte Clásico")
            ganancias_totales = ganancias_totales + 10
            contador_citas = contador_citas + 1
            print("Cita registrada para:", nombre_cliente)
            
        elif tipo_servicio == 2:
            print("Servicio seleccionado: Servicio Completo")
            # Validamos si hay cera en stock
            if stock_cera > 0:
                stock_cera = stock_cera - 1
                ganancias_totales = ganancias_totales + 18
                contador_citas = contador_citas + 1
                print("Cita registrada para:", nombre_cliente)
            else:
                print("No se pudo registrar, no queda cera en el inventario.")
                
        elif tipo_servicio == 3:
            print("Servicio seleccionado: Tinte")
            # Validamos si hay tintes en stock
            if stock_tintes > 0:
                stock_tintes = stock_tintes - 1
                ganancias_totales = ganancias_totales + 25
                contador_citas = contador_citas + 1
                print("Cita registrada para:", nombre_cliente)
            else:
                print("No se pudo registrar, no quedan tintes en el inventario.")
                
        elif tipo_servicio == 4:
            print("Servicio seleccionado: Manicura")
            ganancias_totales = ganancias_totales + 12
            contador_citas = contador_citas + 1
            print("Cita registrada para:", nombre_cliente)
            
        else:
            print("Opción de servicio no válida.")

    
    elif opcion == 2:
        print("\n--- CONTROL DE INSUMOS ---")
        
        print("Cera Capilar:", stock_cera, "unidades")
        if stock_cera <= 3:
            print("⚠️ Alerta: Queda poca cera. Hay que comprar.")
            
        print("Shampoo Especial:", stock_shampoo, "litros")
        if stock_shampoo <= 2:
            print("⚠️ Alerta: Quedan pocos litros de shampoo.")
            
        print("Tintes de Cabello:", stock_tintes, "unidades")
        if stock_tintes <= 3:
            print("⚠️ Alerta: Quedan pocos tintes.")
            
        print("Toallas Desechables:", stock_toallas, "paquetes")
        if stock_toallas <= 5:
            print("⚠️ Alerta: Quedan pocas toallas.")

    
    elif opcion == 3:
        print("\n--- REPORTE DE CAJA ---")
        print("Total recaudado el día de hoy: $", ganancias_totales)

    
    elif opcion == 4:
        print("\n--- CLIENTES ATENDIDOS ---")
        print("Número de clientes registrados hoy:", contador_citas)

    elif opcion == 5:
        print("\nSaliendo del sistema...")
        print("¡Gracias por usar el programa!")

    else:
        print("Opción incorrecta. Intente de nuevo.")

print("\n--- PROGRAMA FINALIZADO ---")
