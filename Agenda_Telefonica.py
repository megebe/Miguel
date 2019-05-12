import json

# base de datos
def cargar_contactos():
    with open('./contactos.json') as file:
        data = json.load(file)
        file.close()
        return data

def guardar_contactos(contactos):
    with open('./contactos.json', 'w') as file:
        json.dump(contactos, file)
        file.close()
contactos=[{ "nombre": "Miguel","numero": "644302878" }]
# funciones
  

print("---------------------------------------------------------")         
print("----------Bienvenido a tu agenda telefónica-------------------")

def imprimir_operacion(nombre_operacion): 
    print()
    print("-------------------Agenda Telefonica------------------")
    print(nombre_operacion)
    print("------------------------------------------------------")
    print() 

def agregar_contacto():
    print()
    nombre = input("Nombre del contacto para añadir: ")
    nombre = str(nombre)
    numero = int(input("Numero del contacto para añadir: "))
    contactos.append({ "nombre": nombre,"numero": numero })
    nombre_operacion = ("Contacto Agregado")
    imprimir_operacion(nombre_operacion)
    guardar_contactos(contactos)
        
def remover_contacto():
    contactos = cargar_contactos()
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'],"-->", contact['numero'])
    index_contacto = int(input("-- Selecciona uno: ")) - 1
    contactos.remove(contactos[index_contacto])

    guardar_contactos(contactos)
    print("Contacto eliminado!")
    

def actualizar_contacto():
    contactos = cargar_contactos()
    campos = ["nombre", "numero"]
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'], "-->", contact['numero'])
    index_contacto = int(input("-- Selecciona uno: ")) - 1
    print("Cual quieres cambiar?:")
    for index in range(len(campos)):
        print(str(index + 1) + ".-", campos[index].capitalize())

    propiedad = int(input("-- Selecciona una: ")) - 1
    valor = input("-- Nuevo valor: ")
    contacto = contactos[index_contacto]
    contacto[campos[propiedad]] = valor

    guardar_contactos(contactos)
    print("Contacto editado!")
        
def ver_todos_contacto():
    print()
    print("----- Lista de contactos----------")
    print()
    contactos = cargar_contactos()
       
    nombre_operacion = None
    
    contactos = cargar_contactos()
    print("Lista de contactos:")
    for index in range(len(contactos)):
        contact = contactos[index]
        print (str(index + 1) + ".-", contact['nombre'], "-->", contact['numero'])

    
    imprimir_operacion(nombre_operacion)
            
    print()
    print("-------------------------------")
    print()

while True:
    print("Estas son las operaciones que puedes realizar")
    print("1 - Agregar Contacto")
    print("2 - Remover Contacto")
    print("3 - Editar Contacto")
    print("4 - Ver todos los contactos")
    print("5 - Salir")
    
    try:
        operacion = int(input("Escriba aquí el nº de la operación que quiere realizar--> : "))
    except ValueError:
        print("-----------------------------------------")
        print("Seleccione número del 1 al 5")
        print("-----------------------------------------")
    else: 
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_todos_contacto()
        elif operacion == 5:
            break
        else:
            print("Operacion desconocida")

print()
print("Gracias por usar nuestro sistema telefónico!!")

