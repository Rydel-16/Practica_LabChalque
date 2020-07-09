#Autor: Vilca 

def comprobar():
    correo=input(f"Ingrese correo electronico: ")

    tamaño=len(correo)
    tamaño1=len(correo[0:(len(correo)-13)])
    direccion=(correo[(len(correo)-14):(len(correo))])

    if tamaño<14:
        print("No es correo de la untels")
    elif direccion=="@untels.edu.pe":
       print("Sí es correo de la untels") 
    else:
       print("No es correo de la untels") 
        
comprobar()

