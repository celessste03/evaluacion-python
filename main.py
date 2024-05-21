#Astry Rosendo
import os 
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

lista_producto= []


def main():
    clear()
    print("****Sistema de inventario****")
    menu='''1.)Agregar un producto  \n2.)Actualizar cantidad de productos \n3.)Mostrar inventario Completo \n4.)Buscar un producto '''
    opc=[1,2,3,4]
    inventario=[]
    a=None
    while True:
        print(menu)
        a=input("Elige una opcion: ")
        if not a.isdigit():
            clear()
            print("Indique un numero valido")
            a=None
            input("Preciona enter para continuar...")
            clear()
            continue
        a=int(a)
        if a<1 or a>len(opc):
            clear()
            print("Indique un numero valido")
            a=None
            input("Preciona enter para continuar")
            clear()
            continue
            
        match a:
            
            case 1:
                clear()
                nombre=input("Ingrese el nombre del producto: ")
                precio=input("Ingrese el precio del producto: ")
                cantidad=input("Ingrese la cantidad de productos: ")
                producto={
                    "nombre": nombre,
                    "precio":precio,
                    "cantidad":cantidad 
                }
                lista_producto.append(producto)
                input("Presione enter para continuar...")
            case 2:
                clear()
                nombre_producto=input("Ingresa el nombre del producto: ")
                nueva_cantidad=input("Ingresa la nueva cantidad del producto: ")
                for producto in lista_producto:
                    if producto["nombre"]==nombre_producto:
                        producto["cantidad"]=nueva_cantidad
                input("Presione enter para continuar...")


            case 3:
                clear()
                for producto in lista_producto:
                    print("=====================")
                    print(f'Nombre: {producto["nombre"]}\nPrecio: {producto["precio"]} \nCantidad: {producto["cantidad"]}')
                    
                input("Presione enter para continuar...")

            case 4:
                clear()
                variable=input("Ingrese el nombre del producto: ")
                busqueda = list(filter(lambda elemento: elemento["nombre"].startswith(variable), lista_producto))
                clear()
                for producto in busqueda:
                    print("====================")
                    print(f'Nombre: {producto["nombre"]}\nprecio: {producto["precio"]} \nCantidad: {producto["cantidad"]}')
                        
                input("Presione enter para continuar...")
main()