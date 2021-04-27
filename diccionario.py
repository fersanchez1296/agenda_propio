contactos={"Nombre":None,
            "Apellido_P":None,
            "Apellido_M":None}

lista_contactos=[]

def registrar():
    nombre = input()
    ape_p = input()
    ape_m = input()
    lista_contactos.append({"Nombre":nombre,
            "Apellido_P":ape_p,
            "Apellido_M":ape_m})
    

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
    cont = 0
    while cont < 2:
        registrar()
        cont+=1
    for i in lista_contactos:
        for clave,valor in i.items():
            print(clave,valor)
    buscar()


if __name__ == "__main__":
    main()
