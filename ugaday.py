import random

with open('sowpods.txt', 'r') as file:
    file= file.readlines()
    x= len(file)
    NUMB = random.randint(1, x)
    slovo = list(file[NUMB])
slovo = slovo[0:-1]
print(slovo)
shifr = ['_'] * len(slovo)
print(shifr)

def zamena():
    predlo = input('Предложите букву ')
    while predlo in slovo:
        ind = slovo.index(predlo)
        shifr[ind] = predlo
        slovo.pop(ind)
        slovo.insert(ind, '*')

def chelovek(rang):
    if rang == 1:
        print(' O')
    elif rang == 2:
        print(' O')
        print('/', end='')
    elif rang == 3:
        print(' O')
        print('/', end='')
        print('|', end='')
    elif rang == 4:
        print(' O')
        print('/', end='')
        print('|', end='')
        print('\\')
    elif rang == 5:
        print(' O')
        print('/', end='')
        print('|', end='')
        print('\\')
        print('/', end =' ')
    elif rang == 6:
        print(' O')
        print('/', end='')
        print('|', end='')
        print('\\')
        print('/', end =' ')
        print('\\')

schetchik = 0
while '_' in shifr and schetchik != 6:
    neugadal = shifr.count("_")
    zamena()
    neugadal2 = shifr.count("_")
    print(shifr)
    if neugadal == neugadal2:
        schetchik+=1
        chelovek(schetchik)
    print()
if schetchik == 6:
    print('Вы проиграли')
if '_' not in shifr:
    print('Поздравляю')