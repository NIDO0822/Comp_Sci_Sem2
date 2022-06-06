import datetime

people_list = []
comp_list = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people_list.append(l)

comp_list =[]
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        comp_list.append(l)

import random
numpeople = random.randrange(0, len(people_list))
numcomp = random.randrange(0, len(comp_list))

print(people_list[numpeople] + comp_list[numcomp])
x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
