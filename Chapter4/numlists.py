'''for num in range(1,21):
    print(num)'''

'''for num in range(1,1000001):
    print(num)'''

million = range(1,1000001)
print(min(million))
print(max(million))
print(sum(million))

odd_numbers = []
for num in range(1,21):
    if  num % 2 == 0:
        odd_numbers.append( num )

print(odd_numbers)

# Slicing lists
# Doing 4.10 Slices
my_favourite_foods = [ "pizza", "spagetti", "albondigas", "hamburguesa", "churrasco", "guacamole", "merluza"]

first_three_foods = my_favourite_foods[:3]
print(first_three_foods)

middle_index = int(len(my_favourite_foods) /2 )
middle_foods = my_favourite_foods[middle_index:middle_index+3]
print(middle_foods)

last_three_foods = my_favourite_foods[-3:]
print(last_three_foods)

# Doing 4.11 My pizzas, your pizzas
my_pizzas = ["margarita", "barbacoa", "peperoni"]
# this way copies the list into another new list
friend_pizzas = my_pizzas[:]

my_pizzas.append("Hawaina")
friend_pizzas.append("Cuatro Estaciones")

print(my_pizzas)
print(friend_pizzas)