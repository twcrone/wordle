import sys


def find_all_matches(word):
    ms = []
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    for line in lines:
        if score(word, line):
            ms.append(line)
    return ms


def score(word, pattern):
    if len(word) != len(pattern):
        return -1
    result = 0
    for i in range(len(word)):
        w = word[i]
        p = pattern[i]
        if p.isupper() and w == p.lower():
            result += 3
        elif p in word:
            result += 1

    return result


if __name__ == "__main__":
    arg = "could" if len(sys.argv) < 2 else sys.argv[1]
    print(arg)
    find_all_matches(arg)
