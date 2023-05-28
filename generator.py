words = ["apple","orange","garp","pineapple","lemon"]
from random import randint
def randomScentanceGenerator(word):
    randomIndex = randint(0,len(words)-1)
    return f"{words[randomIndex]} {word}"


with open("./text.txt") as file:
    paragraph = file.read()
    wordLists = paragraph.split()
    scentanceList = list(map(randomScentanceGenerator,wordLists))

    paraCount = int(input("Paragraph count : "))

    for count in range(paraCount):
        with open("./generator.txt","a") as write_file:
            write_file.write( " ".join(scentanceList) + "\n\n")
