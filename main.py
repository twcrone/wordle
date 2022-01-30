import sys


def find_all_matches(word):
    ms = []
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    for line in lines:
        if matches(word, line):
            ms.append(line)
    return ms


def matches(word, other):
    return len(word) * 3 if word == other else 0


if __name__ == "__main__":
    arg = "could" if len(sys.argv) < 2 else sys.argv[1]
    print(arg)
    find_all_matches(arg)
