# Cajero Automatico Básico
saldo = 1000
print("\t.:MENU:.")
print("1. Consultar saldo")
print("2. Retirar dinero")
print("3. Depositar dinero")
print("4. Salir")

print()

def menu():
    opcion = int(input("Digite una opción del menú: "))
    global saldo
    if opcion == 1:
        print(f"Su saldo es: {saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar: "))
        if retirar>saldo:
            print("¡No tiene esa cantidad de dinero!")
            return menu()
        else:
            saldo -= retirar
        print(f"¡Retiro exitoso! \nSu saldo actual es: {saldo}")
        return opcion
    elif opcion == 3:
        extra = float(input("Cuanto dinero desea depositar: "))
        saldo += extra
        print(f"¡Deposito exitoso! \nSu saldo actual es: {saldo}")
        return opcion
    elif opcion == 4:
        print("Gracias por su usar su ATM de confianza")
        return opcion
    else:
        print("Error, digite una opcion valida")
        return menu()
menu()            

print("Gracias por su usar su ATM de confianza")



