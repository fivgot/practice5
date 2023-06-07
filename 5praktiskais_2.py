import random as rnd

def generatearray(x, y):
    arr = []
    for i in range (10):
        row = []
        for j in range (10):
            rnd_n = rnd.randint(x, y)
            multiplied_val = rnd_n * (i+1)
            row.append(multiplied_val)
        arr.append(row)
    return arr
x = 0
y = 1000

array = generatearray(x, y)

for row in array:
    print(row)