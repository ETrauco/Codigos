print("\n ==== Bienvenido al convertor de divisas ==== \n")

def usd_to_clp():
    print("Conversión de USD a CLP")
    cant_usd = float(input("Ingrese la cantidad de USD: "))
    valor_clp = float(input("Ingrese el valor del dolar en CLP: \n"))
    clp = cant_usd * valor_clp
    print(f"{cant_usd} USD equivalen a {clp} CLP \n")
    return clp


def clp_to_usd(): 
    print("Conversión de CLP a USD")
    cant_clp = float(input("Ingrese la cantidad de CLP: "))
    valor_usd = float(input("Ingrese el valor del dolar en CLP: \n"))
    usd = cant_clp / valor_usd
    print(f"{cant_clp} CLP equivalen a {usd:.2f} USD \n")
    return usd

def main():
    while True:
        opcion = int(input("Ingrese la opción que desea realizar: \n 1. USD a CLP \n 2. CLP a USD \n 3. Salir \n"))
        if opcion == 1:
            usd_to_clp()
        elif opcion == 2:
            clp_to_usd()
        elif opcion == 3:
            print("\n ==== Gracias por usar el convertor de divisas ==== \n")   
            break
        else:
            print("Opción no válida")
            continue
    
main()  
    

