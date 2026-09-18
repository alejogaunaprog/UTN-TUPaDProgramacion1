# Ejercicio 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: solo letras y no puede estar vacío.")
    operador = input("Nombre del operador: ").strip()

print(f"Bienvenido/a, {operador}.\n")

opcion = 0
while opcion != 5:
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    op = input("Opción: ").strip()

    if not op.isdigit():
        print("Error: ingrese un número válido.\n")
        continue

    opcion = int(op)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.\n")

    elif opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while not dia.isdigit() or int(dia) not in (1, 2):
            print("Error: elija 1 (Lunes) o 2 (Martes).")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()
        dia = int(dia)

        nombre = input("Nombre del paciente: ").strip()
        while not nombre.isalpha():
            print("Error: solo letras y no puede estar vacío.")
            nombre = input("Nombre del paciente: ").strip()

        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error: ese paciente ya tiene turno el Lunes.\n")
            elif lunes1 == "":
                lunes1 = nombre
                print("Turno reservado: Lunes - Turno 1.\n")
            elif lunes2 == "":
                lunes2 = nombre
                print("Turno reservado: Lunes - Turno 2.\n")
            elif lunes3 == "":
                lunes3 = nombre
                print("Turno reservado: Lunes - Turno 3.\n")
            elif lunes4 == "":
                lunes4 = nombre
                print("Turno reservado: Lunes - Turno 4.\n")
            else:
                print("No hay turnos disponibles el Lunes.\n")
        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: ese paciente ya tiene turno el Martes.\n")
            elif martes1 == "":
                martes1 = nombre
                print("Turno reservado: Martes - Turno 1.\n")
            elif martes2 == "":
                martes2 = nombre
                print("Turno reservado: Martes - Turno 2.\n")
            elif martes3 == "":
                martes3 = nombre
                print("Turno reservado: Martes - Turno 3.\n")
            else:
                print("No hay turnos disponibles el Martes.\n")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while not dia.isdigit() or int(dia) not in (1, 2):
            print("Error: elija 1 (Lunes) o 2 (Martes).")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()
        dia = int(dia)

        nombre = input("Nombre del paciente a cancelar: ").strip()
        while not nombre.isalpha():
            print("Error: solo letras y no puede estar vacío.")
            nombre = input("Nombre del paciente a cancelar: ").strip()

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                print("Turno cancelado.\n")
            elif lunes2 == nombre:
                lunes2 = ""
                print("Turno cancelado.\n")
            elif lunes3 == nombre:
                lunes3 = ""
                print("Turno cancelado.\n")
            elif lunes4 == nombre:
                lunes4 = ""
                print("Turno cancelado.\n")
            else:
                print("Error: no se encontró ese paciente el Lunes.\n")
        else:
            if martes1 == nombre:
                martes1 = ""
                print("Turno cancelado.\n")
            elif martes2 == nombre:
                martes2 = ""
                print("Turno cancelado.\n")
            elif martes3 == nombre:
                martes3 = ""
                print("Turno cancelado.\n")
            else:
                print("Error: no se encontró ese paciente el Martes.\n")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while not dia.isdigit() or int(dia) not in (1, 2):
            print("Error: elija 1 (Lunes) o 2 (Martes).")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()
        dia = int(dia)

        if dia == 1:
            print("Agenda del Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}\n")
        else:
            print("Agenda del Martes:")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}\n")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("Resumen general:")
        print(f"Lunes  -> Ocupados: {ocupados_lunes} / Disponibles: {libres_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} / Disponibles: {libres_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes\n")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes\n")
        else:
            print("Día con más turnos ocupados: Empate\n")

    else:
        print("Cerrando sistema...")