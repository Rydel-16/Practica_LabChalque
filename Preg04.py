#Autor:Chalque
numero_ingresado = (input("Ingrese un número a ser invertido: "))
invertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        invertir = (invertir * 10) + residuo
        valor //= 10
    print('El numero invertido es: ', invertir)
except ValueError:
    print("Ese número no es valido. Inténtalo de nevo !")  
    