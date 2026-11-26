"""
Nombre del archivo: Agenda_eventos.py
Descrpcion: Agenda de eventos con diccionarios
Autor:Eduardo Emiliano Aguirre Toledo
Fecha: 26/11/2026
"""



# agenda = { "fecha": [ [hora, lugar, descripcion], [hora, lugar, descripcion] ] }
import json

# Al iniciar, se carga el archivo si existe
try:
    archivo = open("agenda.json", "r")
    agenda = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    agenda = {}

opcion = 0
while opcion != 1:
    print()
    print("1. Salir")
    print("2. Agregar evento")
    print("3. Consultar eventos de una fecha")
    print("4. Mostrar agenda completa")
    print("5. Eliminar evento")
    print("6. Liberar fecha")
    print("7. Vaciar agenda")
    opcion = int(input("Elige una opción: "))

    if opcion == 2:
        fecha = input("Fecha (dd/mm/aaaa): ")
        hora = input("Hora: ")
        lugar = input("Lugar: ")
        descripcion = input("Descripción: ")
        evento = [hora, lugar, descripcion]
        if fecha in agenda:
            agenda[fecha].append(evento)
        else:
            agenda[fecha] = [evento]
        print("Evento agregado")

    elif opcion == 3:
        fecha = input("Fecha (dd/mm/aaaa): ")
        if fecha in agenda:
            for evento in agenda[fecha]:
                print("Hora:", evento[0], "| Lugar:", evento[1], "| Descripción:", evento[2])
        else:
            print("No hay eventos en esa fecha")

    elif opcion == 4:
        if len(agenda) == 0:
            print("La agenda está vacía")
        else:
            for fecha in agenda:
                print("Fecha:", fecha)
                for evento in agenda[fecha]:
                    print("   Hora:", evento[0], "| Lugar:", evento[1], "| Descripción:", evento[2])

    elif opcion == 5:
        fecha = input("Fecha (dd/mm/aaaa): ")
        if fecha in agenda:
            for i in range(len(agenda[fecha])):
                evento = agenda[fecha][i]
                print(i + 1, "- Hora:", evento[0], "| Lugar:", evento[1], "| Descripción:", evento[2])
            num = int(input("Número del evento a eliminar: "))
            if num >= 1 and num <= len(agenda[fecha]):
                agenda[fecha].pop(num - 1)
                print("Evento eliminado")
                if len(agenda[fecha]) == 0:
                    del agenda[fecha]
            else:
                print("Número no válido")
        else:
            print("No hay eventos en esa fecha")

    elif opcion == 6:
        fecha = input("Fecha (dd/mm/aaaa): ")
        if fecha in agenda:
            del agenda[fecha]
            print("Fecha liberada")
        else:
            print("Esa fecha no tiene eventos")

    elif opcion == 7:
        agenda.clear()
        print("Agenda vaciada")

    elif opcion != 1:
        print("Opción no válida")

# Al terminar, se guarda en el archivo
archivo = open("agenda.json", "w")
json.dump(agenda, archivo, indent=4)
archivo.close()
print("Agenda guardada. ¡Hasta luego!")
