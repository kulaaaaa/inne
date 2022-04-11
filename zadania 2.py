#Zadanie 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
cube = [number * number * number for number in numbers]
print("Liczby z listy to:" , numbers)
print("Sześciany liczb z listy to:", cube)

undivided = [number * number for number in numbers if number %2  != 0]
print("Niepodzielne liczby sześcianów liczb z listy to:", undivided)

print("======================")
#Zadanie 2
num = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

print(num [1:4] + num [5:10] + num [-2:])
print(num [0], num [4], num [-4:-2])