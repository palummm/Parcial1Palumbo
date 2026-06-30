from super_heroes_data import superheroes
from collections import deque

print("Lista por nombre ascendente:")
superheroes.sort(key=lambda x: x['name'])
for hero in superheroes:
    print(hero["name"])

print("posicion de the thing y rocket raccoon enla lista:")
for index, hero in enumerate(superheroes):
    if hero["name"] == "The Thing":
        print(f"The Thing está en la posición {index}.")
    elif hero["name"] == "Rocket Raccoon":
        print(f"Rocket Raccoon está en la posición {index}.")

print("Lista de villanos:")
villanos = [hero for hero in superheroes if hero["is_villain"]]
for villain in villanos:
    print(villain["name"])

print("cola de villanos 1980")
cola_villanos = deque(villanos)
villanos_viejos = []
while cola_villanos:
    villano_actual = cola_villanos.popleft()
    if villano_actual["first_appearance"] < 1980:
        villanos_viejos.append(villano_actual["name"])

for villain in villanos_viejos:
    print(villain)

print ("superheroes que comienzan con bl, g, my, w")
iniciales = ("Bl", "G", "My", "W")
for hero in superheroes:
    if any(hero["name"].startswith(initial) for initial in iniciales):
        print(hero["name"])

print("listado ordenado por nombre real ascendente")
superheroes.sort(key=lambda x: x['real_name'] if x["real_name"] is not None else "")
for hero in superheroes:
    print(f"nombre real: {hero['real_name']}, nombre de superheroe: {hero['name']}")

print("listado por fecha de aparicion")
superheroes.sort(key=lambda x: x['first_appearance'])
for hero in superheroes:
    print(f"fecha de aparicion: {hero['first_appearance']}, nombre de superheroe: {hero['name']}")

print("modificar nombre")

for hero in superheroes:
    if hero["name"] == "Ant Man":
        hero["real_name"] = "Scott Lang"
        print(f"Nombre real de {hero['name']} modificado a {hero['real_name']}")
        break

print("biografias con 'time traveling' o 'suit' ===")
for hero in superheroes:
    biografia = hero["short_bio"]
    if "time-traveling" in biografia or "suit" in biografia:
        print(f"{hero['name']}: {biografia}")

print("eliminar a electro y baron zemo")
eliminar = ["Electro", "Baron Zemo"]
eliminados = []

for nombre in eliminar:
    for i in range(len(superheroes)):
        if superheroes[i]["name"] == nombre:
            eliminados.append(superheroes.pop(i))
            break
if eliminados:
        print("personajes eliminados:")
        for eliminado in eliminados:
            print(eliminado)
else:
    print("No se encontraron personajes para eliminar.")