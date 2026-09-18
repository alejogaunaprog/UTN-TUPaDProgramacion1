# Ejercicio 2

USUARIO_OK = "alejo"
clave_ok = "boca123"

acceso = False
intento = 1


while intento <= 3 and not acceso:
    usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == USUARIO_OK and clave == clave_ok:
        acceso = True
        print("Acceso concedido.\n")
    else:
        print("Error: credencial inválida.")
        intento += 1

if not acceso:
    print("cuenta bloqueada")
else:
    opcion = 0
    
    while opcion != 4:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        op = input("Opción: ").strip()

        if not op.isdigit():
            print("Error: ingresá un número válido.\n")
            continue

        opcion = int(op)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.\n")
        elif opcion == 1:
            print("Inscripto\n")
        elif opcion == 2:
            nueva = input("Nueva clave: ").strip()
            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.\n")
            else:
                confirma = input("Confirmar clave: ").strip()
                if nueva != confirma:
                    print("Error: las claves no coinciden.\n")
                else:
                    clave_ok = nueva
                    print("Clave actualizada ok.\n")
        elif opcion == 3:
            print("Todo se cura con amor. Seguí así!\n")
        else:
            print("Saliendo del sistema...")