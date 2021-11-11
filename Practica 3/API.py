#!/bin/python3
from pyhunter import PyHunter

ApiKey = input("Ingrese la llave de la API: ")
hunter = PyHunter (ApiKey)
Dominio = input("Ingrese un Dominio en url: ")
Busqueda = hunter.domain_search (Dominio)

#Busqueda = hunter.domain_search ('https://www.uanl.mx/') 
print(Busqueda)
