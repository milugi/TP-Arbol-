from Archivos import abrir, leer, cerrar, guardar, modificar
from TDA_Arbol_Binario import busqueda, inorden_lightsaber, busqueda_proximidad, nodoArbolGreek, busqueda_nario, insertar_nario, nodoArbolMarvel
from TDA_Arbol_Binario import por_nivel, preorden, postorden, insertar_nodo as ins_nod, nodoArbolHuffman, insertar_nodo_morse, inorden_altura, inorden_peso
from TDA_Arbol_Binario_AVL import altura, cortar_por_nivel, contar_a, eliminar_nodo, inorden, hijo_der, hijo_izq, insertar_nodo, padre
from TDA_Cola import Cola, cola_vacia, arribo, atencion
from random import randint, choice



# 1 cargar 1000 número enteros –generados de manera aleatoria–

arbol = None

for i in range(1000):
    arbol = insertar_nodo(arbol, randint(0,100))

#A Realizar los barridos preorden, inorden, postorden y por nivel.

print('Barrido inorden: ')
print()
inorden(arbol)
a = input()
print('Barrido preorden')
print()
preorden(arbol)
a = input()
print('Barrido postorden')
print()
postorden(arbol)
a = input()
print('Barrido por nivel')
print()
por_nivel(arbol)
a = input()

#B Determinar si un número está cargado en el árbol o no.
buscado = int(input('Ingrese el número buscado: '))
pos = busqueda(arbol, buscado)
if(pos is not None):
    print('El número indicado está en el árbol')
else:
    print('El número indicado no está en el árbol')

#C Eliminar tres valores del árbol.
arbol, dato = eliminar_nodo(arbol, 5)
print('El número', dato, 'ha sido eliminado')
arbol, dato = eliminar_nodo(arbol, 13)
print('El número', dato, 'ha sido eliminado')
arbol, dato = eliminar_nodo(arbol, 57)
print('El número', dato, 'ha sido eliminado')

#D Determinar la altura del subárbol izquierdo y del subárbol derecho.
print('La altura del subárbol derecho es: ',altura(arbol.der))
print('La altura del subárbol izquierdo es: ',altura(arbol.izq))

#E Determinar la cantidad de ocurrencias de un elemento en el árbol.
def contar_repetidos(raiz, buscado, cant):
    if(raiz is not None):
        if(raiz.info == buscado):
            cant += 1
            cant = contar_repetidos(raiz.der, buscado, cant)
        else:
            cant = contar_repetidos(raiz.izq, buscado, cant)
    return cant
cant = 0
buscado = 73
pos = busqueda(arbol, buscado)
if(pos is not None):
    print('El número ',buscado, 'está', contar_repetidos(pos, buscado, cant), 'veces en el árbol')
else:
    print('El número no se encuentra en el árbol')

#F Contar cuántos números pares e impares hay en el árbol.
cantp, canti = 0, 0

def contar(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = contar(raiz.izq, cp, ci)
        cp, ci = contar(raiz.der, cp, ci)
    return cp, ci
cantp, canti = contar(arbol, cantp, canti)
print('La cantidad de números pares es de: ', cantp)
print('La cantidad de números impares es de: ', canti)

#Ejercicio 4
arbol = None
for i in range(10):
    arbol = insertar_nodo(arbol, randint(0,10))
    print('Recorrido numero: ',i)
    por_nivel(arbol)
print()
hijo_der(arbol)
hijo_izq(arbol)


#E5

arbol = None
arbol_villanos = None
lista = [['Iron-Man', True], ['Capitán América', True], ['Thanos', False], 
['Misterio', False], ['Hulk', True], ['Galactus', False], ['Doctor Estrange', True]]

#A En cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano.
for i in lista:
    nodo = nodoArbolMarvel(i[0], i[1])
    arbol = insertar_nodo(arbol, [nodo.nombre, nodo.heroe])
    if i[1] is False:
        arbol_villanos = insertar_nodo(arbol_villanos, nodo.nombre)

#B Listar los villanos ordenados alfabéticamente.
print('-Villanos: ')
inorden(arbol_villanos)
print()

#C Mostrar todos los superhéroes que empiezan con C.
def comienzo(raiz):
    if (raiz is not None):
        if ((raiz.info[0][0] == 'C') and (raiz.info[1] is True)):
            print(raiz.info[0])
        comienzo(raiz.der)
        comienzo(raiz.izq)
print('-Superheroes que comienzan con C: ')
comienzo(arbol)
print()

#D Determinar cuántos superhéroes hay el árbol.
c = 0
def contar_heroes(raiz, c):
    if (raiz is not None):
        if (raiz.info[1] is True):
           c += 1
        c = contar_heroes(raiz.der, c)
        c = contar_heroes(raiz.izq, c)
    return c
print('-Hay',contar_heroes(arbol, c), 'superhéroes en el árbol')
print()

#E Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre.
def busqueda_proximidad_dr(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0][0:len(buscado)] == buscado):
            print('Encontrado:', raiz.info[0])
            return raiz
        else:
            if(raiz.info[0] > buscado):         
                return busqueda_proximidad_dr(raiz.izq, buscado)
            else:
                return busqueda_proximidad_dr(raiz.der, buscado)
pos = busqueda_proximidad_dr(arbol, 'Doctor')
pos.info[0] = 'Doctor Strange'
print('-Corregido')
print()

#F Listar los superhéroes ordenados de manera descendente.
arbol_heroes = None
listita = []
def cargar_heroes(raiz, listita):
    if (raiz is not None):
        if (raiz.info[1] is True):
            listita += [raiz.info[0]]
        cargar_heroes(raiz.izq, listita)
        cargar_heroes(raiz.der, listita)
cargar_heroes(arbol, listita)
print('-Superhéroes ordenados de manera descendente: ')
print()
for i in listita:
    arbol_heroes = insertar_nodo(arbol_heroes, i)
postorden(arbol_heroes)
print()

#G Generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos.
bosque = []
bosque.append(arbol_heroes)
bosque.append(arbol_villanos)

#.1
print('-La altura del primer árbol es: ',altura(bosque[0]))
print('-La altura del segundo árbol es: ',altura(bosque[1]))
print()

#.2
print('-Barrido primer árbol del bosque: ')
inorden(bosque[0])
print()
print('-Barrido segundo árbol del bosque: ')
inorden(bosque[1])



'''
#6

arbol_nombre = None
arbol_ranking = None
arbol_especie = None

# file = abrir('jedis')
file = open('jedis.dat')
linea = file.readline()
pos = 0
while linea:
    linea = linea.replace('\n', '')
    arbol_nombre = insertar_nodo(arbol_nombre, linea.split(';')[0], pos)
    arbol_ranking = insertar_nodo(arbol_ranking, linea.split(';')[1], pos)
    arbol_especie = insertar_nodo(arbol_especie , linea.split(';')[2], pos)
    pos += 1
    linea = file.readline()    
file.close()

# while (pos < len(file)):
#     jedi = leer(file, pos)
#     arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
#     arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
#     arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
#     pos += 1
# cerrar(file)
print('Termino de cargar los arboles')

#b
# file = abrir('jedis')
# inorden_lightsaber(arbol_nombre, file)
# cerrar(file)
file = open('jedis.dat')
inorden(arbol_nombre)
a=input()

#c
por_nivel(arbol_especie)
a=input()

#proximidad
busqueda_proximidad(arbol_nombre, 'l')

#d
pos = busqueda(arbol_nombre, 'luke skywalker')
index = 0
if(pos is not None):
    print(pos.nrr)
    file = open('jedis.dat')
    linea = file.readline()
    while linea and index < pos.nrr:
        linea = linea.replace('\n', '')
        linea = file.readline()
        index += 1
    print(linea)
'''

# 8

nmin = None
nmax = None
arbol = None
def nodo_min(raiz):
    if (raiz is not None):
        return raiz
    else:
        print('No posee nodos')
def nodo_max(raiz):
    if (raiz is None):
        print('No posee nodos')
    else:
        if (raiz.altura == 0):
            return raiz
        else:
            if (raiz.der is not None):
                if (raiz.der.altura == 0):
                    return raiz.der
                else:
                    return nodo_max(raiz.der)
            if (raiz.izq is not None):
                if (raiz.izq.altura == 0):
                    return raiz.izq
                else:
                    return nodo_max(raiz.izq)
for i in range(10):
    arbol = insertar_nodo(arbol, randint(0,10))
print()
nmin = nodo_min(arbol)
nmax = nodo_max(arbol)
por_nivel(arbol)
print()
if (nmin is not None):
    print('Datos del nodo minimo:', nmin.info)
else:
    print('Ta vacio')
if (nmax is not None):
    print('Datos del nodo maximo:', nmax.info)
else:
    print('Ta vacio')

#9
tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
dic = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}
def como_comparo(elemento):
    return elemento[1]
def como_comparo_nodo(elemento):
    return elemento.valor


tabla.sort(key=como_comparo)
bosque = []
for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)
for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor + elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)
por_nivel(bosque[0])
def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco
def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod
cadena = "AA31TF0AAMMMMMM0000"
from sys import getsizeof
cadena_cod = codificar(cadena, dic)
print(getsizeof(cadena_cod), getsizeof(b'00000110011011110100000'))
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)



#Ejercicio 10
def nodos_totales_posibles (numero):
    return 2**(numero-1)
def cantidad_nodos(raiz, numero, cont_nodos, cont):
    control = False
    if (raiz is not None):
        if (control is False):
            cont += 1
            control = True
        if (cont == (numero-1)):
            cola = Cola()
            arribo(cola, raiz)
            while(not cola_vacia(cola) and cont == (numero-1)):
                nodo = atencion(cola)
                if(nodo.izq is not None):
                    cont_nodos += 1
                    arribo(cola, nodo.izq)
                    print('Info del nodo izq: ',nodo.izq.info)
                if(nodo.der is not None):
                    cont_nodos += 1
                    arribo(cola, nodo.der)
                    print('Info del nodo der: ',nodo.der.info)
                cont += 1
        else:
            if(raiz.izq is not None):
                cont_nodos = cantidad_nodos(raiz.izq, numero, cont_nodos, cont)
            if(raiz.der is not None):
                cont_nodos = cantidad_nodos(raiz.der, numero, cont_nodos, cont)
    return cont_nodos
arbol = None
cont_nodos = 0
cont = 0
for i in range(31):
    arbol = insertar_nodo(arbol, randint(0,100))    
num = int(input('Ingrese el nivel del árbol del cual determinar la máxima cantidad de nodos posibles: '))
posibles = nodos_totales_posibles(num)
print('Total de nodos permitidos en el nivel seleccionado:', posibles)
print()
x = (cantidad_nodos(arbol, num, cont_nodos, cont))
if (x != 0):
    print('Hay', x, 'nodos en el nivel', num)
elif (num == 1):
    print('Hay 1 nodo en el nivel', num)
else:
    print('No hay nodos en este nivel')
print()

#A Determinar si el nivel del árbol está completo.

#B ¿Cuántos nodos faltan para completar dicho nivel?.
if (x == posibles):
    print('El nivel está completo')
else:
    print('Le faltan', posibles-x, 'nodos para estar completo')



#Ej11

Arbol = None
Cont = 0
for i in range(10):
    Arbol = insertar_nodo(Arbol, randint(0, 100))
por_nivel(Arbol)
print()

#A Contar el número de nodos del árbol.

def contar_nodos (raiz, cont):
    if (raiz is not None):
        cont += 1
        cont = contar_nodos(raiz.izq, cont)
        cont = contar_nodos(raiz.der, cont)
    return cont
x = contar_nodos(Arbol, Cont)
if (x is not None):
    print('El arbol contiene', x, 'nodos')

#b Determinar el número de hojas del árbol.


#C mostrar la información de los nodos hojas.

Cont = 0
def contar_hojas (raiz, cont):
    if (raiz is not None):
        if (raiz.izq is None and raiz.der is None):
            cont += 1
            print('Información que contiene la hoja', raiz.info)
        else:
            cont = contar_hojas(raiz.izq, cont)
            cont = contar_hojas(raiz.der, cont)
    return cont
n = contar_hojas(Arbol, Cont)
if (n is not None):
    print('El arbol contiene', n, 'hojas')
#D determinar el padre de un nodo.
buscado = int(input('Ingrese el número a buscar: '))
padre(Arbol, buscado)

#E determinar la altura de un árbol.
print('La altura del arbol es:', altura(Arbol))

#Ej 12
arbol = None
for i in range(1,1024):
    arbol = insertar_nodo(arbol, i)

cantidad = [0]
contar_a(arbol, cantidad)
print(altura(arbol), cantidad[0])
bosque = []
cortar_por_nivel(arbol, bosque)
print(len(bosque))
for arbol in bosque:
    print('raiz del arbol', arbol.info)
    cantidad = [0]
    contar_a(arbol, cantidad)
    print('cantidad de nodos del arbol', cantidad[0])
    

#Ejercicio 15
arbol = None
tabla = [['Obi Wan Kenobi', 1.74, 82], ['Chewbacca', 2.04, 113], ['Darth Vader', 1.85, 93], ['Yoda', 1.10, 47], ['Leia Organa', 1.73, 74], ['Han Solo', 1.77, 83]]
class Personaje():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

#A Se almacena el nombre y la posición en la que se encuentra en el archivo(nrr).
print(tabla)
file = abrir('Star_Wars')
for i in tabla:
    sw = Personaje(i[0], i[1], i[2])
    guardar(file, sw)
pos = 0
while(pos < len(tabla)):
    personaje = leer(file, pos)
    arbol = insertar_nodo(arbol, personaje.nombre, pos)
    print(pos)
    print(len(file))
    pos += 1
cerrar(file)
# print('Arbol antes de cualquier modificacion: ')
# por_nivel(arbol)
print()

#B Se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja.
a = input('¿Quiere cargar un nuevo personaje? Si/No: ')
if(a == 'Si' or a == 'si'):
    file = abrir('Star_Wars')
    name = input('Ingrese nombre del personaje: ')
    height = int(input('Ingrese altura del personaje: '))
    weight = int(input('Ingrese peso del personaje: '))
    sw = Personaje(name, height, weight)
    guardar(file, sw)
    arbol = insertar_nodo(arbol, sw.nombre, len(file))
    cerrar(file)
    tabla.append([name, height, weight])
# print('Arbol y tabla luego de cargar un nuevo personaje: ')
# por_nivel(arbol)
# print()
# print(tabla)
print()
a = input('¿Quiere modificar algún campo de un personaje? Si/No: ')
if(a == 'Si' or a == 'si'):
    file = abrir('Star_Wars')
    buscado = input('Ingrese nombre del personaje a buscar: ')
    arbol, x = eliminar_nodo(arbol, buscado)
    print('Nodo eliminado:', x)
    print()
    for i in range (0, len(tabla)):
        psj = leer(file, i)
        if(psj.nombre == buscado):
            pos = i
            break
    a = input('Elija campo a modificar nombre/altura/peso: ')
    if a == 'nombre':
        name = input('Ingrese el nuevo nombre: ')
        sw = Personaje(name, psj.altura, psj.peso)
        modificar(file, pos, sw)
        psj = leer(file, pos)
        arbol = insertar_nodo(arbol, psj.nombre, pos)
    elif a == 'altura':
        height = int(input('Ingrese la nueva altura: '))
        sw = Personaje(psj.nombre, height, psj.peso)
        modificar(file, pos, sw)
        psj = leer(file, pos)
        arbol = insertar_nodo(arbol, psj.nombre, pos)
    else:
        weight = int(input('Ingrese el nuevo peso: '))
        sw = Personaje(psj.nombre, psj.altura, weight)
        modificar(file, pos, sw)
        psj = leer(file, pos)
        arbol = insertar_nodo(arbol, psj.nombre, pos)
cerrar(file)
print()


#C Mostrar toda la info de Yoda y Boba Feet.
file = abrir('Star_Wars')
for i in range (0, len(tabla)):
    psj = leer(file, i)
    if(psj.nombre == 'Yoda'):
        print(psj.nombre, psj.altura, psj.peso)
    elif(psj.nombre == 'Boba Feet'):
        print(psj.nombre, psj.altura, psj.peso)
cerrar(file)
print()

#D Listar personajes con altura mayor a 1m.
file = abrir('Star_Wars')
inorden_altura(arbol, file)
cerrar(file)
print()
#E Listar personajes con peso menor a 75kg.
file = abrir('Star_Wars')
inorden_peso(arbol, file)
cerrar(file)
print()

#ej17

arbol_nombres = None
arbol_tipo = None
arbol_numero = None

class Pokemon(object):
    
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

    def __str__(self):
       return self.nombre + ' ' + str(self.numero) + ' ' + self.tipo + ' ' + self.debilidad

tipo = ['agua', 'fuego', 'tierra', 'electrico']
debil = ['agua', 'fuego', 'tierra', 'electrico', 'Jolteon', 'Lycanroc', 'Tyrantum']
nombre = ['Bulbasaur', 'Charmander', 'Pikachu', 'Ivysaur', 'Charmeleon', 'Charizard', 'Squirtle', 'wartortle', 'Venusaur']


#A
for i in range (0, len(nombre)):
    pokemon = Pokemon(nombre[i], randint(1, 100), choice(tipo), choice(debil))
    arbol_nombres = insertar_nodo(arbol_nombres, [pokemon, pokemon.nombre])
    arbol_tipo = insertar_nodo(arbol_tipo, [pokemon, pokemon.tipo])
    arbol_numero = insertar_nodo(arbol_numero, [pokemon, pokemon.numero])


#B
def inorden_numero(raiz):
    if(raiz is not None):
        inorden_numero(raiz.izq)
        print(raiz.info[1], raiz.info[0])
        inorden_numero(raiz.der)
print('Listado en orden por número:')
inorden_numero(arbol_numero)
print()

def busqueda_proximidad_poke(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[1])
        busqueda_proximidad_poke(raiz.izq, buscado)
        busqueda_proximidad_poke(raiz.der, buscado)

x = input('Ingrese el nombre parcial de pokemon a buscar:')
print('Todos los pokemons con ese nombre parcial:')
busqueda_proximidad_poke(arbol_nombres, x)
print()

#C
def busqueda_proximidad_poke2(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[1][0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke2(raiz.izq, buscado)
        busqueda_proximidad_poke2(raiz.der, buscado)

x = input('Ingrese el tipo de pokemon a buscar:')
print('Todos los pokemons de un tipo:')
busqueda_proximidad_poke2(arbol_tipo, x.lower())
print()

#D
def inorden_numero2(raiz):
    if(raiz is not None):
        inorden_numero2(raiz.izq)
        print(raiz.info[0])
        inorden_numero2(raiz.der)

print('Listado en orden creciente numérico de pokemons:')
inorden_numero2(arbol_numero)
print()

def inorden_nombre(raiz):
    if(raiz is not None):
        inorden_nombre(raiz.izq)
        print(raiz.info[0])
        inorden_nombre(raiz.der)

print('Listado en orden creciente alfabético de pokemons:')
inorden_nombre(arbol_nombres)
print()

def por_nivel_nombre(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info[0])
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)
    
print('Listado en orden por nivel de pokemons:')
por_nivel_nombre(arbol_nombres)
print()

#E
def busqueda_proximidad_poke3(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0].debilidad[0:len(buscado)] == buscado):
            print(raiz.info[0].nombre)
        busqueda_proximidad_poke3(raiz.izq, buscado)
        busqueda_proximidad_poke3(raiz.der, buscado)

print('Debiles contra Jolteon: ')
busqueda_proximidad_poke3(arbol_nombres, 'Jolteon')
print()

print('Debiles contra Lycanroc: ')
busqueda_proximidad_poke3(arbol_nombres, 'Lycanroc')
print()

print('Debiles contra Tyrantrum: ')
busqueda_proximidad_poke3(arbol_nombres, 'Tyrantrum')
print()

#F
cont = 0

def inorden_tipo(raiz, cont):
    if(raiz is not None):
        if raiz.info[0].tipo == 'fuego':
            cont += 1
        inorden_tipo(raiz.izq, cont)
        print(raiz.info[0].nombre, raiz.info[0].tipo)
        inorden_tipo(raiz.der, cont)
    return cont

print('Pokemons y su tipo:')
cont = inorden_tipo(arbol_nombres, cont)
print()

print('Cantidad del tipo fuego:',cont)








#Ej19
class Libro():
    def __init__(self, isbn, titulo, autores, editorial, cant):
        self.isbn = isbn
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.cant = cant
arbol_titulo = None
arbol_ISBN = None
arbol_autor = None
autor = ['J. K. Rowling','Edgar Allan Poe','Beca Flitzpatrick','John Green','Tanenbaum','Connoly','Riordan','Morgan', 'Kass','Sommerville', 'Morgan-Kass']
tit = ['Los 100','Algoritmos','Minería de Datos','Bases de Datos','Ingeniería de Software','Harry Potter','Hush Hush','Ciudades de Papel','El Gato Negro']
#A
file = abrir('libros')
#B
for i in range (0, 100):
    l1 = Libro(randint(1000, 9789504967453), choice(tit), choice(autor), 'UADER', randint(50,2000))
    guardar(file, l1)

#C
pos = 0
while(pos < len(file)):
    libro = leer(file, pos)
    arbol_ISBN = insertar_nodo(arbol_ISBN, libro.isbn, pos)
    arbol_titulo = insertar_nodo(arbol_titulo, libro.titulo, pos)
    arbol_autor = insertar_nodo(arbol_autor , libro.autores, pos)
    pos += 1
cerrar(file)

#D
#.1 Busqueda por exactitud en arbol ISBN
buscado = int(input('Ingrese ISBN del libro a buscar: '))
x = busqueda(arbol_ISBN, buscado)
if(x is not None):
    file = abrir('libros')
    libro = leer(file, x.nrr)
    cerrar(file)
    print('El libro buscado es de ISBN ', libro.isbn,', titulo', libro.titulo, ',y autores', libro.autores)
else:
    print('El libro no ha sido encontrado')

#.2 Si son más de un autor y busco por uno, debería encontrarlo de encontrarlo igual
buscado = input('Ingrese autor del libro a buscar: ')
x = busqueda(arbol_autor, buscado)
if(x is not None):
    file = abrir('libros')
    libro = leer(file, x.nrr)
    cerrar(file)
    palabra = libro.autores.split('-')
    if (palabra[0] or palabra[1] == buscado):
        print('El libro correspondiente a este autor es: ', libro.titulo)
else:
    print('Libro no encontrado')

#.3
buscado = input('Ingrese titulo del libro a buscar: ')
busqueda_proximidad(arbol_titulo, buscado)
#A Mostrar libros de Tanenbaum, Connolly, Rowling, Riordan, Morgan-Kass;
aut = ['Tanenbaum', 'Connolly', 'J. K. Rowling', 'Riordan', 'Morgan-Kass']
for i in aut:
    x = busqueda(arbol_autor, i)
    if(x is not None):
        file = abrir('libros')
        libro = leer(file, x.nrr)
        cerrar(file)
        print('Libro de', i , libro.titulo)
    else:
        print('El autor no fue encontrado')


#B Mostrar los libros de “minería de datos”, “algoritmos” y “bases de datos”
libs = ['Mineria de Datos','Algoritmos','Bases de Datos']
for i in libs:
    x = busqueda(arbol_titulo, i)
    if(x is not None):
        file = abrir('libros')
        libro = leer(file, x.nrr)
        cerrar(file)
        print('Libro de titulo ', i , 'con ISBN', libro.isbn, 'y autores', libro.autores)
    else:
        print('El autor no fue encontrado')


#C Mostrar los libros de más de 873 páginas
pos = 0
file = abrir('libros')
while(pos < len(file)):
    libro = leer(file, pos)
    if (libro.cant > 873):
        print('ISBN del libro', libro.isbn,'cantidad de paginas del libro', libro.cant, 'titulo del libro', libro.titulo)
    pos += 1
cerrar(file)


#D Mostrar los datos del libro ISBN 9789504967453
x = busqueda(arbol_ISBN, 9789504967453)
if(x is not None):
    file = abrir('libros')
    libro = leer(file, x.nrr)
    cerrar(file)
    print('El libro buscado es de ISBN ', libro.isbn,', titulo', libro.titulo, ',y autores', libro.autores)
else:
    print('Libro de ISBN ingresado no fue encontrado')


#E mostrar el autor del libro “los 100”
x = busqueda(arbol_titulo, 'Los 100')
if(x is not None):
    file = abrir('libros')
    libro = leer(file, x.nrr)
    cerrar(file)
    print('El autor del libro Los 100 es: ', libro.autores)
else:
    print('El libro con titulo Los 100 no fue encontrado')

#Ej21
arbol = None
archivo = open('greek_gods')
linea = archivo.readline()
print('archivo')
while linea:        
    linea = linea.replace('\n', '')
    dios = linea.split(';')
    nodo = nodoArbolGreek(dios[0], dios[2])
    #print('insertar', dios[0])
    if(arbol is None):
        arbol = nodo
    else:
        pos = []
        busqueda_nario(arbol, dios[1], pos)
        #print('resultado de busqueda', pos[0].info)
        insertar_nario(pos[0], nodo)
    #preorden(arbol)
    #a = input()
    linea = archivo.readline()
archivo.close()
#por_nivel_nario(arbol)
# pos = []
# busqueda_nario(arbol, 'zeus', pos)
# hijo = pos[0].izq
# while(hijo is not None):
#     print(hijo.info)
#     hijo = hijo.der
bosque = []
hijo = arbol.izq
while(hijo is not None):
    aux = hijo.der
    hijo.der = None
    bosque.append(hijo)
    hijo = aux
print('cantidad de arboles del bosque', len(bosque))
for arbol in bosque:
    print('raiz ------------------>', arbol.info)
    inorden(arbol)
    print()