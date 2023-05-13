import random
wordsList = ["apple","banana","cherry","orange","pear"]
randomWord = random.choice(wordsList)
tries = 5
ovel = ["a","e","i","o","u"]
guessWord = ''
blankSpaceIndex = []
print("Start Guessing word?")
ind = 0
guessStr =""
for word in randomWord:
    if word.lower() in ovel:
        print(word, end=" ")
        guessStr+=word
    else:
       blankSpaceIndex.append(ind)
       print("_",end=" ")
       guessStr+="_"
    ind += 1

print("")


for i in range(len(blankSpaceIndex)):
    while tries > 0:
        if i < len(blankSpaceIndex):
            userInput = input("Guess a word:")
            guessWord = userInput.lower()  
            if randomWord[blankSpaceIndex[i]].lower() == guessWord:
                print("Correct")
                # Following code use for create string.
                temp = list(guessStr)
                temp[blankSpaceIndex[i]] = guessWord
                guessStr = "".join(temp)
                print(guessStr)
                i += 1
            else:
                print("failed")
                print(guessStr)
                tries -= 1
       
    if tries == 0:
        print("You Lose")


# Test