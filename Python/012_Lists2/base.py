import random
thislist = ["0","1","2","3","4","5","6","7","8","9",]
b = int(input("how many numbers printed out(1-10)"))

for i in range(0,b):
    x = (random.randrange(10))
    print(thislist[x])
