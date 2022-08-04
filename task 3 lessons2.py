x = input("Введите 3 числа через пробел:")
fizz, buzz, number = list(map(int, x.split()))

for i in range(1, number + 1):
    if ((i % fizz == 0) and (i % buzz == 0)):
        print ('FB')
    elif (i % fizz == 0):
        print ('F')
    elif (i % buzz == 0):
        print ('B')
    else:
        print (i)