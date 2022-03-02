import random
import sys


def find_best_options(pattern, include, exclude):
    best_options = []
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    if pattern is None:
        count = len(lines)
        r = random.randrange(count)
        return lines[r]

    for line in lines:
        line = line.strip()
        if match(line, pattern, include, exclude):
            best_options.append(line)
    return best_options


def match_letter(a, b):
    return a.lower() == b.lower() or b == "_"


def match(word, exact, include, exclude):
    if word.lower() == exact.lower():
        return True
    for i in range(len(word)):
        if not match_letter(word[i], exact[i]):
            return False
        elif i < len(include) and not include[i] == "_" and not include[i] in word:
            return False
        elif i < len(exclude) and exclude[i] in word:
            return False

    return True


if __name__ == "__main__":
    pat = None if len(sys.argv) < 2 else sys.argv[1]
    inc = "" if len(sys.argv) < 3 else sys.argv[2]
    exc = "" if len(sys.argv) < 4 else sys.argv[3]
    print(pat)
    print(inc)
    print(exc)
    print(find_best_options(pat, inc, exc))
