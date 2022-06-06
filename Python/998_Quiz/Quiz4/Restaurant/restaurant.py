import random
thislist = ["KFC","panera", "blaze"]
KFClist = ["chicken", "tenders","fries", "fountain drink"]
paneralist = ["Mac and cheese", "pizza", "pastry", "fountain drink"]
blazelist = ["cheese", "pepperoni", "half pizza cheese", "half pizza pepperoni"]
print(thislist)
sug = int(random.randrange(4))
choice = input("which restaurant")
if choice == "KFC":
    print(KFClist)
    KFCchoice = input("what would you like to order?")
   
    if sug == 0:
        print("we suggest" + KFClist[0])
    elif sug == 1:
        print("we suggest" + KFClist[1])
    elif sug == 2:
        print("we suggest" + KFClist[2])
    elif sug == 3:
        print("we suggest" + KFClist[3])
    print("you have chosen "+ KFCchoice +" from KFC")
elif choice == "panera":
    print(paneralist)
    panerachoice = input("What would you like to order?")
    
    if sug == 0:
        print("we suggest" + KFClist[0])
    elif sug == 1:
        print("we suggest" + KFClist[1])
    elif sug == 2:
        print("we suggest" + KFClist[2])
    elif sug == 3:
        print("we suggest" + KFClist[3])
    print("you have chosen"+ panerachoice +" from panera")
elif choice == "blaze":
    print(blazelist)
    blazechoice = input("what would you like to order?")
    
    if sug == 0:
        print("we suggest" + KFClist[0])
    elif sug == 1:
        print("we suggest" + KFClist[1])
    elif sug == 2:
        print("we suggest" + KFClist[2])
    elif sug == 3:
        print("we suggest" + KFClist[3])
    print("you have chosen "+ blazechoice+" from blaze")   
else:
    print("invalid choice rerun code please")