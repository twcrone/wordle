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


def matches(word, pattern):
    for i in range(len(pattern)):
        letter = pattern[i]
        if letter == "_":
            continue
        if letter.isupper() and not letter.lower() == word[i].lower():
            return False
        elif letter.islower() and not letter in word:
            return False
    return True


def excluded(word, excludes):
    for i in range(len(excludes)):
        if excludes[i] in word:
            return False

    return True


def match(word, exact, include, exclude):
    if word.lower() == exact.lower():
        return True
    for i in range(len(word)):
        if not match_letter(word[i], exact[i]):
            return False

    for i in range(len(include)):
        if not include[i] == "_" and not include[i] in word:
            return False

    for i in range(len(exclude)):
        if exclude[i] in word:
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
