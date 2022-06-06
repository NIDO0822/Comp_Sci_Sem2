inpage = input("what is your age?(use proper grammar)")
for i in range(0,len(inpage)):
    if (inpage[len(inpage)-3,len(inpage)-2] == " "):
        age = len(inpage)-2,len(inpage)-1
    elif (inpage[len(inpage)-4,len(inpage)-3] == " "):
        age = len(inpage)-3,len(inpage)-1
    elif (inpage[len(inpage)-5,len(inpage)-4] == " "):
        age = len(inpage)-4,len(inpage)-1
age = int(age)
inpfav = int(input("what is your favorite number?(ex: 10"))

math = age * inpfav
print(math)
#this wont work but I dont know whats wrong because when i compile it says: TypeError: string indices must be integers and idk how to fix it so I cant fix the other stuff thats wrong