import random as rnd

def generatearray(x, y):
    arr = []
    for i in range (10):
        row = []
        for j in range (10):
            rnd_n = rnd.randint(x, y)
            row.append(rnd_n * (i+1)) 
        arr.append(row)
    return arr
x = 0
y = 1000

array = generatearray(x, y)

for row in array:
    print(row)