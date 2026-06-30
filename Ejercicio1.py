# Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#A.funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# B.funcion recursiva para listar los superheroes de la lista.

superheroes = [
    "Kang",
    "Hulk",
    "Black Widow",
    "Black Cat",
    "Iron Man",
    "Magneto",
    "Storm",
    "Venom",
    "Scarlet Witch",
    "Abomination",
    "Adam Warlock",
    "Angel",
    "Captain America",
    "Annihilus",
    "Ant Man",
]

#A
def buscar(lista: list)-> bool:
    if not lista:
        return False
    if lista[0] == "Captain America":
        return True
    return buscar(lista[1:])

#B
def listar(lista: list)-> None:
    if not lista:
        return
    print(lista[0])
    listar(lista[1:])

print("Lista de Superheroes:")
listar(superheroes)
    

encontrado = buscar(superheroes)
if encontrado:
        print("Captain America está en la lista.")
else:
        print("Captain America no está en la lista.")