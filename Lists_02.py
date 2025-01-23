# 4.7 List multiple of 3
threes = []

for number in range(3,31):
    if number % 3 == 0:
        threes.append(number)

print(threes)

# 4.8 Cubes
cubes_no_comprehension = []
for number in range(1,11):
    cubes_no_comprehension.append(number**3)
    print( number**3 )

# 4.9 Cube comprehension
cubes = [ num ** 3 for num in range(1,11)]
print(cubes)