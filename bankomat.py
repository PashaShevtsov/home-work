banknotes = [1000, 500, 200, 100, 50 ,20 ,10]

amount = int(input("please provide the amount of grn you want to get: "))
for nominal in banknotes:
    if amount // nominal:
        print(str(nominal) + ' -> ' + str(amount // nominal))
        amount %= nominal
