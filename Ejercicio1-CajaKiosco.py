# Ejercicio 1

nombre = input("Cliente: ").strip()
while not nombre.isalpha():
    print("Error: sin espacio y solo letras.")
    nombre = input("Cliente: ").strip()


cantidad = input("Cantidad de productos: ").strip()
while not cantidad.isdigit() or int(cantidad) == 0:
    print("Error: ingresa un número entero mayor a 0.")
    cantidad = input("Cantidad de productos: ").strip()
cantidad = int(cantidad)

total_sin = 0
total_con = 0.0


for i in range(1, cantidad + 1):
    print(f"Producto {i}")

    precio = input(" - Precio: ").strip()
    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(" - Precio: ").strip()
    precio = int(precio)

    desc = input(" - Descuento (S/N): ").strip().lower()
    while desc != "s" and desc != "n":
        print("Error: responda Si o No.")
        desc = input(" - Descuento (S/N): ").strip().lower()

    total_sin += precio
    if desc == "s":
        total_con += precio * 0.9
    else:
        total_con += precio


ahorro = total_sin - total_con
promedio = total_con / cantidad

print(f"\nTotal sin descuentos: ${total_sin}")
print(f"Total con descuentos: ${total_con:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")