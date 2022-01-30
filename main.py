import random
import sys


def find_best_options(pattern, exclude):
    best_options = []
    best_score = 0
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    if pattern is None:
        count = len(lines)
        r = random.randrange(count)
        return lines[r]

    for line in lines:
        line = line.strip()
        line_score = score(line, pattern, exclude)
        # print(line + " (" + str(line_score) + ")")
        if line_score == best_score:
            best_options.append(line)
        elif line_score > best_score:
            best_options = [line]
            best_score = line_score
    return best_options


def score(word, pattern, exclude):
    if len(word) != len(pattern):
        return -1
    result = 0
    for i in range(len(word)):
        w = word[i]
        p = pattern[i]
        if any(letter in word for letter in exclude):
            return 0
        elif p.isupper() and w == p.lower():
            result += 3
        elif p in word:
            result += 1

    return result


if __name__ == "__main__":
    pat = None if len(sys.argv) < 2 else sys.argv[1]
    exc = "" if len(sys.argv) < 3 else sys.argv[2]
    print(pat)
    print(exc)
    print(find_best_options(pat, exc))
