mis_amigos = [ "Juan", "Andrea", "Jess", "Uxia", "Mauro", "Zeltia",]
print(mis_amigos)

for amigo in mis_amigos:
    print(f"Hola {amigo}, como te encuentras hoy?")

pop_amigo = mis_amigos.pop()
print(f"{pop_amigo} fue eliminado de la lista.")
for amigo in mis_amigos:
    print(f"Hola {amigo}, como te encuentras hoy?")

print(type(pop_amigo))

invitados = []
invitados.append("Lucas")
invitados.append("Marcos")
invitados.append("Nuria")

for invitado in invitados:
    print(f"{invitado} estás invitado a la cena de esta noche.")

print(f"{invitados.pop()} me acaba de llamar y no puede asistir a la cena.")
print("Lucas acaba de llamar a ultima hora para decir que no viene a cenar.")
invitados.remove("Lucas")
print("Pero me acaba de llamar Pablo diciendo que viene él y su novia Tania a cenar.")
invitados.append("Pablo")
invitados.append("Tania")
for invitado in invitados:
    print(f"{invitado} estás invitado a la cena de esta noche.")

print("Acabo de encontrar una mesa mucho mas grande!")

invitados.insert(0, "Ana")
invitados.insert( int(len(invitados)/2), "Javi")
invitados.insert(-1, "Jaime")

for invitado in invitados:
    print(f"{invitado} estás invitado a la cena de esta noche.")

print("Al final la mesa no llega asi que solo tengo sitio para 2 personas")

while len(invitados) > 2:
    print(f"Lo siento {invitados.pop()}, al final no tengo sitio para cenar esta noche.")

for invitado in invitados:
    print(f"{invitado} aún estás invitado a la cena de esta noche.")

invitados.clear()
print(invitados)