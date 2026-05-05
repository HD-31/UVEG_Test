def main_menu():
    while True:
        print("\nMiniCafe Menu")
        print("1. Sistema de ventas")
        print("2. Reporte")
        print("3. Salir2")
        
        choice = input('Elegir opción:')
        if choice == '1':
            print(" Bienvenido al sistema de ventas")
            break
        elif choice == '2':
            print(" Bienvenido al sistema de rporte")
            break
        elif choice == '3':
            print(" Bye")
            break
main_menu()