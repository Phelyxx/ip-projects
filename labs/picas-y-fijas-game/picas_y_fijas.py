# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:06:57 2020

@author: usuario
"""
def picas(numero_secreto:int, intento:int)->int:
    secret1 = (numero_secreto // 1000)
    secret2 = (numero_secreto % 1000) // 100
    secret3 = ((numero_secreto % 1000)%100) // 10
    secret4 = ((numero_secreto % 1000)%100) % 10
    adivina1 = intento // 1000
    adivina2 = (intento % 1000) // 100
    adivina3 = ((intento % 1000)%100) //10
    adivina4 = ((intento % 1000)%100) % 10
    picas = 0
    if secret1 == adivina2 or secret1 == adivina3 or secret1 == adivina4: picas += 1
    if secret2 == adivina1 or secret2 == adivina3 or secret2 == adivina4: picas += 1
    if secret3 == adivina1 or secret3 == adivina2 or secret3 == adivina4: picas += 1
    if secret4 == adivina1 or secret4 == adivina2 or secret4 == adivina3: picas += 1
    return picas

def fijas(numero_secreto:int,intento:int)->int:
    secret1 = (numero_secreto // 1000)
    secret2 = (numero_secreto % 1000) // 100
    secret3 = ((numero_secreto % 1000)%100) // 10
    secret4 = ((numero_secreto % 1000)%100) % 10
    adivina1 = intento // 1000
    adivina2 = (intento % 1000) // 100
    adivina3 = ((intento % 1000)%100) //10
    adivina4 = ((intento % 1000)%100) % 10
    fijas = 0
    if secret1 == adivina1: fijas += 1
    if secret2 == adivina2: fijas += 1
    if secret3 == adivina3: fijas += 1
    if secret4 == adivina4: fijas += 1
    return fijas

def picas_y_fijas(numero_secreto:int,intento:int)->str:
    secret1 = (numero_secreto // 1000)
    secret2 = (numero_secreto % 1000) // 100
    secret3 = ((numero_secreto % 1000)%100) // 10
    secret4 = ((numero_secreto % 1000)%100) % 10
    adivina1 = intento // 1000
    adivina2 = (intento % 1000) // 100
    adivina3 = ((intento % 1000)%100) //10
    adivina4 = ((intento % 1000)%100) % 10
    jugada = {'PICAS':0,'FIJAS':0}
    if secret1 == adivina1: jugada['FIJAS'] += 1
    elif secret1 == adivina2 or secret1 == adivina3 or secret1 == adivina4: jugada['PICAS'] += 1
    if secret2 == adivina2: jugada['FIJAS'] += 1
    elif secret2 == adivina1 or secret2 == adivina3 or secret2 == adivina4: jugada['PICAS'] += 1
    if secret3 == adivina3: jugada['FIJAS'] += 1
    elif secret3 == adivina1 or secret3 == adivina2 or secret3 == adivina4: jugada['PICAS'] += 1
    if secret4== adivina4: jugada['FIJAS'] += 1
    elif secret4 == adivina1 or secret4 == adivina2 or secret4 == adivina3: jugada['PICAS'] += 1
    return jugada