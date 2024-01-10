# constante y variables
NOMBRE = 'Aleksandr'
edad = 20
texto = """ESTOY
MUY
GORDITO"""
# booleanos = True o False

# print por pantalla
print(NOMBRE)
print(edad)
print(texto)

# pedir por pantalla
# apellido = input('Dime tu apellido: ') ctrl + k + c = comentarios
# print(apellido)                        ctrl + k + u = quita comentarios

# exponente 2 ** 2 (2 elevado a 2)

# tupla (varios tipos de dato no modificables)
tupla = ('aleksandr', 20, 1.85)
print(tupla[1])  # o tupla[1:4]

# lista (igual que las duplas, pero este si se puede modificar)
lista = ['aleksandr', 2, 1.85]
lista[1] = 20
lista.append('kladov')  # agregar un nuevo dato al final de la lista
print(lista[1])

# diccionario, busca una clave y devuelve su valor
diccionario = {
    'España': 'Madrid',
    'Francia': 'Paris'
}
print(diccionario['España'])

# if
numero = 1
if numero == 1:
    print()
elif numero == 2:
    print()
else:
    print()
    
# for
array2 = {1,2,3}
for i in range(2):
    print(array2)
    
# for each
array = {1,2,3}
for elemento in array:
    print(elemento)

# while
while numero == 2:
    print()
    
# funciones
def mi_funcion():
    print('hola mundo')

mi_funcion()


def mi_funcion2(nombre, edad=20):
    print(nombre, ' - ', edad)

mi_funcion2('alex')
