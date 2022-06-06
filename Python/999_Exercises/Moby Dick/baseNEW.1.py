sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        counter = 0
        whales = "whales"
        for i in range(0,len(sentence)):
            if (whales[i:i+5].lower() == "whales"):
                counter = counter + 1
   
    










#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
f.close()
print(counter)