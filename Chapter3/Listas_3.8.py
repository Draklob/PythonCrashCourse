visitar_ciudades = ["Venecia", "New York", "California", "Tailandia", "Japón", "Alemania",]

print(visitar_ciudades)
print("Ciudades ordenado: ",sorted(visitar_ciudades))
print("Sigue con el mismo orden: ",visitar_ciudades)
visitar_ciudades.reverse()
print("Orden cambiado al revés: ",visitar_ciudades)
visitar_ciudades.reverse()
print("Orden de vuelta al original: ",visitar_ciudades)
visitar_ciudades.sort()
print("Ordenamos para siempre la lista: ", visitar_ciudades)
visitar_ciudades.sort(reverse=True)
print("Los ordeamos al reves la lista :", visitar_ciudades)

# Exercise 4.2
animales_agua = ["Dolphin", "Shark", "Octopus", "Squid"]

for animal in animales_agua:
    print(f"Bienvenido {animal} al zoo Cangas!!")

print("Todos estos animales viven en el agua.")