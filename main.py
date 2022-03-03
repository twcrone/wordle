import random
import sys


def find_best_options(patterns):
    best_options = []
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    if len(patterns) == 0:
        count = len(lines)
        r = random.randrange(count)
        return lines[r]

    for line in lines:
        line = line.strip()
        if is_match_for(line, patterns):
            best_options.append(line)
    return best_options


def is_match_for(word, patterns):
    for pattern in patterns:
        if pattern.startswith("-"):
            if not excluded(word, pattern[1:]):
                return False
        elif not matches(word, pattern):
            return False
    return True


def matches(word, pattern):
    for i in range(len(pattern)):
        letter = pattern[i]
        if letter == "_":
            continue
        if letter.isupper() and not letter.lower() == word[i].lower():
            return False
        elif letter.islower() and not included_but_not_at_index(word, letter, i):
            return False
    return True


def included_but_not_at_index(word, letter, index):
    return letter in word and word[index] != letter

def excluded(word, excludes):
    for i in range(len(excludes)):
        if excludes[i] in word:
            return False

    return True


if __name__ == "__main__":
    print(find_best_options(sys.argv[1:]))
