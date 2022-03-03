# Wordle Helper
Python script to help solve Wordle and help me get comfortable with Python

`python main.py <pattern> [pattern] [pattern] -[excludes]`

`python main.py` Will pick a random starting word

`python main.py M____` Will find a list of best options given that `M` is in correct location

`python main.py M_s__` As above but only including words that also have `s` in the word but not in actual index

`python main.py M_s__ -xyz` As above but only including words that also do NOT include `x`, `y` and `z`
