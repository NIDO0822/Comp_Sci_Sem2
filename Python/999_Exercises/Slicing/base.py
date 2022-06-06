#x = str(input("full name please:"))

#or z in range(0,len(x)):
 #   w = z + 1
  #  y = x[z:w]
   # if y == " ":
    #    for z in range(w,len(x)):
     #       w = z +1
      #      lastname = x[z:w]
       #     print(lastname+"1")
#    else:
 #       print (y)
    
    
    
name = input("What is your full name?")
space = 1
for i in range(0,len(name)):
    if(name[i:i+1] == " "):
        space = i
    print(name[i:i+1])
print(",")
for x in range(space,len(name)):
    print(name[x:x+1])
print("+")
for m in range(0,space):
    print(name[m:m+1])