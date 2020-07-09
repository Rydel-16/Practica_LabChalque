#  Diseñar un programa que permita mostrar la cantidad de letras que tiene una cadena
# Autor: rose

def  contar_digitos(cadena):
    digitos = 0
    letras = 0
    
    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
        
    return digitos, letras

texto = input('digite un texto: ')

resultado = contar_digitos(texto)
print("cantidad de digitos: %i" % resultado[0])
print("cantidad de letras: %i" % resultado[1])