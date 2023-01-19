def score_from_file(filename):
    try:
        scores = dict()
        tiles = []
        with open(filename, 'r') as f:
            for line in f:
                letter, value = line.split()
                scores[letter] = int(value)
        return scores
    except FileNotFoundError:
        return f"{filename} does not exist"


def tiles_from_file(filename):
    try:
        tiles = []
        with open(filename, 'r') as f:
            for line in f:
                line = "".join(line.split())
                tiles.append(line)
        return tiles
    except FileNotFoundError:
        return f"{filename} does not exist"


def dictionary_from_file(filename):
    dictionary = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.split()
                line = "".join(line)
                dictionary.append(line)
        return dictionary
    except FileNotFoundError:
        return f"{filename} does not exist"


#Task 2

def onlyEnglishLetters(value): # NOQA
    import re
    regex = re.search("^[a-zA-Z]*$", value)
    if regex:
        return True
    else:
        return False
#Or we can also use:
# if value.isalpha()



#Task 3

def getLetterScore(value, score): # NOQA
    if value.upper() in score:
        return score[value.upper()]
    else:
        return 0




if __name__ == '__main__':
    print(score_from_file("score.txt"))
    print(tiles_from_file("tiles.txt"))
    print(dictionary_from_file("dictionary.txt"))
    print(onlyEnglishLetters("HELLO"))
    print(getLetterScore("L",score_from_file("score.txt")))







