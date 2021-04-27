contactos={"Nombre":None,
            "Apellido_P":None,
            "Apellido_M":None}

lista_contactos=[]

def registrar():
    nombre = input()
    ape_p = input()
    ape_m = input()
    for clave in contactos.keys():
        contactos["Nombre"]= nombre
        contactos["Apellido_P"] = ape_p
        contactos["Apellido_M"] = ape_m
    

def main():
    cont = 0
    while cont < 2:
        registrar()
        cont+=1
    for clave, valor in contactos.items():
        print(clave,valor,sep=":",end="\n")


if __name__ == "__main__":
    main()
