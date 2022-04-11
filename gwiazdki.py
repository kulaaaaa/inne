#Nr 1
for i in range(5):
    print('* ' *10)
    print(' *' *10)

print ('------------------')

#Nr 2
h = 4
for i in range(h):
    print('*' * (i + 2))
    print('*' * (i + 2))

print ('------------------')

#Nr 3
def gwiazdka(h):
    for i in range(h, 0, -1):
        print(i * "*")
    return
gwiazdka(6)

