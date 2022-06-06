import random
list_words = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        print(l)

num = random.randrange(12972)
answer = list_words[num]
print(answer)
a = 0
w = 0
while(w<6):
    guess = input("Give me a 5 letter word!")
    if guess == answer:
        print("u got it!")
        break
    else:
        for words in list_words:
            if guess == words:
                a = 1
        print("wrong")
f.close()
