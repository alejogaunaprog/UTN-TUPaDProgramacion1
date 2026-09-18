# Ejericio 5

nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_jugador = 100          # int
vida_enemigo = 100          # int
pociones = 3                 # int
daño_base_pesado = 15         # int
daño_base_enemigo = 12       # int
turno_gladiador = True       # boolean

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    op = input("Opción: ").strip()
    while not op.isdigit() or int(op) not in (1, 2, 3):
        print("Error: Ingrese un número válido.")
        op = input("Opción: ").strip()
    opcion = int(op)

    if opcion == 1:
        if vida_enemigo < 20:
            daño = daño_base_pesado * 1.5   # float, golpe crítico
            print("¡Crítico!")
        else:
            daño = float(daño_base_pesado)

        vida_enemigo -= daño
        print(f"¡Atacaste al enemigo por {daño} de daño!")

    elif opcion == 2:
        print(">> ¡Ráfaga de golpes")
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    else:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Usaste poción y recuperaste 30 de vida.")
        else:
            print("No te quedan pociones")

    if vida_enemigo > 0:
        vida_jugador -= daño_base_enemigo
        print(f"¡El enemigo te atacó por {daño_base_enemigo} de daño!")

    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

print()
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ganó la batalla.")
else:
    print("DERROTA. Has caído.")