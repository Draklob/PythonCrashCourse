javier = { "nombre":"Javier", "apellido":"Barreiro", "edad":34, "ciudad":"Pontevedra"}

print(type(javier.get("edad")))

personas = {
    "javier": {"nombre":"Javier", "apellido":"Barreiro", "edad":34, "ciudad":"Pontevedra"},
    "ana": {"nombre":"Ana", "apellido":"Pombo", "edad":25, "ciudad":"Barcelona"},
    "juan": {"nombre":"Juan", "apellido":"Martinez", "edad":33, "ciudad":"Pontevedra"},
}
print("\n")
print(*(persona for persona in personas))
personas["ana"]["ciudad"] = "Madrid"
print(personas.get("ana"))

favourite_numbers = {
    "lucas" : 5,
    "paco" : 13,
    "javi" : 23,
}

print(favourite_numbers)

lobo = {"tipo":"mamifero", "propietario": "salvaje", "peso": 25}
elefante = {"tipo":"mamifero", "propietario": "salvaje", "peso": 115}
perro = {"tipo":"mamifero", "propietario": "lucas", "peso": 12}
salamandra = {"tipo":"reptil", "propietario": "javi", "peso": 4}

pets = [ lobo, elefante, perro, salamandra]

for pet in pets:
    print(pet)

favourite_places = {
    "ana": ["Paris", "Venecia"],
    "javi": ["Las Palmas", "Cangas", "California"],
    "andrea": ["India", "Japon", "Cangas", "Indonesia"],
    "marcial": ["Cangas"],
}

for persona, lugares in favourite_places.items():
    persona = persona.title()
    if len(lugares) > 1:
        print(f"A {persona} sus sitios favoritos son:")
    else:
        print(f"A {persona} su sitio favoritos es:")
    for lugar in lugares:
        print(lugar)

estudiante = {"nombre": "Paco", "edad":23, "curso":"Python nivel 1", "notas": [8, 7, 5]}

print(f"El estudiante {estudiante.get("nombre")} tiene {estudiante.get("edad")} años.")
estudiante["edad"] = 21
estudiante["ciudad"] = "Madrid"

print(estudiante)

del estudiante["curso"]
print(estudiante)

print("Imprimiendo clave valor")
for clave, valor in estudiante.items():
    print(f"{clave} : {valor}")

clase = {
    "paco" : {"nombre":"Paco", "edad": 23, "notas": [5, 7, 7]},
    "lucas" : {"nombre":"Lucas", "edad": 21, "notas": [3, 4, 5]},
    "sergio" : {"nombre":"Sergio", "edad": 18, "notas": [4, 4, 3]},
}

print( clase["lucas"]["nombre"])
print( clase["lucas"]["edad"])

for estudiante in clase:
    notas = clase[estudiante]["notas"]
    promedio = sum(notas) / len(notas)
    clase[estudiante]["promedio"] = promedio

for datos in clase.values():    
    print(f"{datos}")

dic1 = { "libro1": "Pocahontas", "libro2" : "Randombook", "libro3":"Fiesta en Cangas"}
dic_copy = dic1.copy()
dic2 = {"libro2":"Libro cambiado", "libro4": "La vida es maravillosa"}

dic_fusion = {**dic1, **dic2}
print(dic_fusion, " version pro")

dic2.update(dic_copy)
dic_fusionado = dic2
print(dic_fusionado, " usando update hace cosas raras")

# Busqueda en diccionarios
inventario = {
    "lechugas" : 20,
    "chocolate" : 33,
    "tomates" : 12,
    "cebollas" : 43,
}

producto = input("Que producto estás buscando? ")
print(inventario.get(producto, "NOOOO"))

if producto in inventario:
    print(f"Hay {inventario[producto]} unidades de {producto}")
else:
    print(f"El producto {producto} no está en el inventario.")

for key, cantidad in inventario.items():
    if key == producto:
        print(f"Nos quedan {cantidad} {key} en la tienda")
        break

edades = {
    "Juan" : 10,
    "Ana" : 20,
    "Lucas" : 19,
    "Bartolomeo" : 44,
}

edades = { nombre : edad for nombre, edad in edades.items() if edad >= 18}
print(edades)

palabras = [
    "platanos",
    "manzanas",
    "ciruelas",
    "fresas",
    "sandia",
    "platanos"
]

longitud = {}
for palabra in palabras:
    longitud[palabra] = len(palabra)

print(longitud)

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(frecuencia)