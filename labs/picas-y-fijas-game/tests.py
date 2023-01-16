# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:31:20 2020

@author: usuario
"""

import random
import picas_y_fijas as lib

r = random.randint(1000,9999)
numero = int(input("Digite el numero contra el computador: "))
pyf = lib.picas_y_fijas(r, numero)

if numero != r:
   print(lib.picas_y_fijas(r, numero))
   print("Intentos: ", 4)
   numero = int(input("Digite otro numero: "))
if numero != r:
   print(lib.picas_y_fijas(r, numero))
   print("Intentos: ", 3)
   numero = int(input("Digite otro numero: "))
if numero != r:
   print(lib.picas_y_fijas(r, numero))
   print("Intentos: ", 2)
   numero = int(input("Digite otro numero: ")) 
if numero != r:
   print(lib.picas_y_fijas(r, numero))
   print("Intentos: ", 1)
   numero = int(input("Digite otro numero: "))   
if numero != r:
   print(lib.picas_y_fijas(r, numero))
   print("PERDIO")     
elif numero == r:
   print("GANÓ")     
   