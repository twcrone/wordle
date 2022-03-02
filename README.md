# Wordle Helper
Python script to help solve Wordle and help me get comfortable with Python

`python main.py <pattern> [includes] [excludes]`

`python main.py` Will pick a random starting word

`python main.py M_s__` Will find a list of best options given that `M` and `s` is correct location (ignoring case)

`python main.py M_s__ abc` As above but only including words that also have `a`, `b` and `c` in them

`python main.py M_s__ abc xyz` As above but only including words that also do NOT include `x`, `y` and `z` in them
