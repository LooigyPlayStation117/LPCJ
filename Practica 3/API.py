from pyhunter import PyHunter

ApiKey = input("ingrese su apikey: ")
hunter = PyHunter (ApiKey)
#Dominio = input("ingrese el dominio en url: ")

#Puede cambiar la url por Dominio
Busqueda = hunter.domain_search ('https://www.uanl.mx/') 
print(Busqueda)
