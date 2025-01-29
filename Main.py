import json

experimentos = []

def agregar_experimento():
    nombre = input("Nombre del experimento: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    tipo = input("Tipo de experimento (Química, Biología, Física): ")
    
    try:
        resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
    except ValueError:
        print("Error: Los resultados deben ser números separados por comas.")
        return
    
    experimento = {
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados
    }
    experimentos.append(experimento)
    print("Experimento agregado con éxito.")

def mostrar_experimentos():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    
    for i, exp in enumerate(experimentos, 1):
        print(f"{i}. {exp['nombre']} ({exp['fecha']}) - {exp['tipo']}")
        print(f"   Resultados: {exp['resultados']}")

def calcular_estadisticas():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    
    mostrar_experimentos()
    index = int(input("Seleccione el número del experimento a analizar: ")) - 1
    
    if 0 <= index < len(experimentos):
        datos = experimentos[index]["resultados"]
        print(f"Promedio: {sum(datos) / len(datos):.2f}")
        print(f"Máximo: {max(datos)}")
        print(f"Mínimo: {min(datos)}")
    else:
        print("Selección inválida.")

def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar experimento")
        print("2. Mostrar experimentos")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            mostrar_experimentos()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
