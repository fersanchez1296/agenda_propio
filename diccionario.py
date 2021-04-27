contactos={"Nombre":None,
            "Apellido_P":None,
            "Apellido_M":None}

lista_contactos=[]

def validar_opcion():
    try:
        opcion = int(input("Seleccione la opción deseada->"))
    except ValueError as error:
        print("***Valor ingresado invalido***",error,sep="\n",end="\n")
    else:
        return opcion

def menu_agenda():
    while True:
        print("1)Registrar","2)Listar","3)Buscar","4)Modificar","5)Eliminar","6)Salir",sep="\n",end="\n")
        opcion = validar_opcion()
        if opcion == 1:
            registrar()
            break


def validar_nombre(nombre):
    validacion = 0
    nombre = nombre.split()
    nombre = "".join(nombre)
    if nombre != nombre.isalpha()== False: 
        print("***Formato invalido***")
        return validacion
    else:  
        validacion+=1
        return validacion
        


def registrar():
    condicion = True
    while condicion:
        nombre = input()
        val = validar_nombre(nombre)
        nombre = nombre.split()
        if val == 1:
            if len(nombre) == 1:
                if len(lista_contactos) == 0:
                    lista_contactos.append({"Nombre":nombre[0]})
                    condicion = False
                else:
                    for i in lista_contactos:
                        buscar_nombre = i.get("Nombre")
                        if nombre[0] == buscar_nombre:
                            print("Este nombre ya existe")
                            break
                        else:
                            lista_contactos.append({"Nombre":nombre[0]})
                            condicion = False
                            break
            elif len(nombre) == 2:
                pass
        """
        lista_contactos.append({"Nombre":nombre[0],
                    "Apellido_P":nombre[1],
                    "Apellido_M":nombre[2]})
        """
        
    

def buscar():
    buscar = input()
    for i in lista_contactos:
        x=i.get("Nombre")
        y=i.get("Apellido_P")
        z=i.get("Apellido_M")
        if buscar == x or buscar == y or buscar == z:
            print("Este nombre existe")
            break
        else:
            print("Este nombre no existe")
            break

def main():
    while True:
        menu_agenda()
    for i in lista_contactos:
        for clave,valor in i.items():
            print(clave,valor)
    


if __name__ == "__main__":
    main()
