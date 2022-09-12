"""
En este prueba tecnica me pidieron 
1) Armar una funcion para filtrar los multiplos de 5 de un array.
input: un array de longitud finita con numeros enteros
output: un array con los multiplos de 5 del array de entrada, no tenia que ordenarlos.

"""

def multipleOf5(n):
    return n % 5 == 0
myList = [10, 25, 17, 9, 30, -5]
myList2 = list(filter(multipleOf5, myList))
print(myList2)

"""
2) Armar un arreglo con numeros impares del 11 al 17 (esto fue una yapa nomas, lo importante era lo otro).

"""

inc = list(range(11, 17,2))
print(inc)