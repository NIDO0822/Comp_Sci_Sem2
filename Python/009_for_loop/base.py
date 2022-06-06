x = int(input("line length"))
y = str(input("hor or ver"))
if y == "ver":
    for z in range (0,x):
        print(z)
elif y == "hor":
    for z in range (0,x):
        print(z, end="")
else:
    print("restart code please")