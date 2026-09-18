# Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

bloqueado = False
forzar_seguidas = 0  # cuenta cuántas veces seguidas elige forzar

nombre = input("Nombre del agente: ").strip()
while not nombre.isalpha():
    print("Error: solo letras y no puede estar vacío.")
    nombre = input("Nombre del agente: ").strip()

print(f"\nBienvenido, agente {nombre}. La bóveda tiene 3 cerraduras.\n")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:

    print("----- ESTADO -----")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    op = input("Opción: ").strip()
    while not op.isdigit() or int(op) not in (1, 2, 3):
        print("Error: opción inválida.")
        op = input("Opción: ").strip()
    opcion = int(op)

    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            print("La cerradura se trabó por forzarla varias veces.")
            alarma = True
            forzar_seguidas = 0
        elif energia < 40:
            print("Riesgo de alarma (energía baja).")
            riesgo = input("Elija una acción (1-3): ").strip()
            while not riesgo.isdigit() or int(riesgo) not in (1, 2, 3):
                print("Error: ingrese un número entre 1 y 3.")
                riesgo = input("Elija una acción (1-3): ").strip()
            riesgo = int(riesgo)

            if riesgo == 3:
                print("Activaste la alarma")
                alarma = True
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada con éxito.")
        else:
            cerraduras_abiertas += 1
            print("Cerradura forzada con éxito.")

    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")
        letras = "ABCD"
        for i in range(4):
            codigo_parcial += letras[i]
            print(f"Paso {i + 1}/4 - Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código completo. Se abrió una cerradura automáticamente.")

    else:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansas, pero la alarma sigue activa y consume energía extra.")
        else:
            print("Descansas y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("\nLa alarma se disparó y se bloqueó el acceso")

    print()

if cerraduras_abiertas == 3:
    print(f"VICTORIA: {nombre} abriste las 3 cerraduras y escapaste con el botín.")
elif bloqueado:
    print(f"DERROTA (bloqueo): la alarma bloqueó el sistema antes de terminar.")
elif energia <= 0:
    print(f"DERROTA: {nombre} te quedaste sin energía.")
elif tiempo <= 0:
    print(f"DERROTA: {nombre} te quedaste sin tiempo.")