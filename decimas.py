from os import system
system("cls")

import random

# Variables globales
equipos = {}
eventos_partido = []
estadisticas = {
    'goles_local': 0,
    'goles_visitante': 0,
    'tiros_arco': 0,
    'faltas': 0,
    'posesion': [0, 0]  # [local, visitante]
}

def mostrar_menu():
    print("\n Menú del Partido")
    print("1. Registrar equipos")
    print("2. Simular partido")
    print("3. Mostrar estadísticas")
    print("4. Ver eventos del partido")
    print("5. Salir...")

def registrar_equipos():
    try:
        equipos['local'] = input("Nombre equipo local: ")
        equipos['visitante'] = input("Nombre equipo visitante: ")
        print(f"Equipos registrados: {equipos['local']} vs {equipos['visitante']}")
    except Exception as e:
        print(f"Error al registrar equipos: {e}")

def simular_goles(equipo):
    if random.randint(1, 100) > 70:  # 30% de probabilidad de gol
        estadisticas[f'goles_{equipo}'] += 1
        eventos_partido.append(f"Gol del {equipo.upper()}!")
        return True
    return False

def simular_acontecimiento():
    equipo_atacante = random.choice(['local', 'visitante'])
    estadisticas['tiros_arco'] += 1
    estadisticas['posesion'][0 if equipo_atacante == 'local' else 1] += 1
    
    if simular_goles(equipo_atacante):
        return
    
    if random.randint(1, 10) > 7:  # 30% de probabilidad de falta
        estadisticas['faltas'] += 1
        eventos_partido.append("Falta cometida")

def calcular_porcentaje_posesion():
    total = sum(estadisticas['posesion'])
    try:
        local = (estadisticas['posesion'][0] / total) * 100
        visitante = (estadisticas['posesion'][1] / total) * 100
        return local, visitante
    except ZeroDivisionError:
        print("Error: No se ha jugado ningún minuto aún")
        return 0, 0

def mostrar_estadisticas():
    if not equipos:
        print("Primero registre los equipos")
        return
    
    try:
        print(f"\n--- Estadísticas ({equipos['local']} vs {equipos['visitante']}) ---")
        print(f"Goles: {estadisticas['goles_local']}-{estadisticas['goles_visitante']}")
        print(f"Tiros al arco: {estadisticas['tiros_arco']}")
        print(f"Faltas cometidas: {estadisticas['faltas']}")
        
        posesion_local, posesion_visitante = calcular_porcentaje_posesion()
        print(f"Posesión: {posesion_local:.1f}% - {posesion_visitante:.1f}%")
    except KeyError as e:
        print(f"Error mostrando estadísticas: {e}")

# Ejecución directa del programa sin función main ni if __name__ == "__main__"
while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registrar_equipos()
        elif opcion == 2:
            if not equipos:
                print("Primero registre los equipos")
                continue
            
            for minuto in range(1, 91):  # Range para 90 minutos
                if random.random() < 0.35:  # 35% de probabilidad de evento por minuto
                    simular_acontecimiento()
                if minuto == 45:
                    eventos_partido.append("--- Medio tiempo ---")
            
            print("\n--- Resultado Final ---")
            mostrar_estadisticas()
        elif opcion == 3:
            mostrar_estadisticas()
        elif opcion == 4:
            print("\nEventos del partido:")
            for evento in eventos_partido:
                print(f"- {evento}")
        elif opcion == 5:
            print("¡Partido terminado!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
    except ValueError:
        print("Error: Ingrese un número válido")
    except ZeroDivisionError:
        print("Error: División por cero detectada")
    except Exception as e:
        print(f"Error inesperado: {e}")






