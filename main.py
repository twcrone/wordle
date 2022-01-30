import sys


def findAllMatches(word):
    Matches = []
    wordFile = open("words.txt", "r")
    Lines = wordFile.readlines()
    for line in Lines:
        if matches(word, line):
            Matches.append(line)
    return Matches


def matches(word, other):
    return len(word) * 3 if word == other else 0


if __name__ == "__main__":
    arg = "could" if len(sys.argv) < 2 else sys.argv[1]
    print(arg)
    findAllMatches(arg)
