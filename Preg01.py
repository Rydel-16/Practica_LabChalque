# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:26:56 2020

@author: Rhisto Zea
"""

def primos(numero):
    c=0
    if int(numero) < 1:
        validar = "Numero no valido."
        return validar
    elif numero == 2:
        validar = "No es primo."
        return validar
    else:
        for i in range(2, int(numero)):
            if int(numero)%i == 0:
                c=+1

    if c>=1:
        validar = "No es primo."
        return validar
    else:
        validar = "Es primo"
        return validar

numero = input("Ingrese un numero: ")
print(primos(numero))