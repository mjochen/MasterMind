
#region generate code, colors
def get_all_colors():
    colors = []
    for i in range(8):
        colors.append(chr(ord('A') + i))
    return colors

def get_random_code(colors: list):
    import random
    code = ""
    for i in range(4):
        color = random.choice(colors)
        while color in code:
            color = random.choice(colors)
        
        code += color
        
    return code
#endregion

#region test color
def test_color(attempt, code):
    nr_correct = 0
    for i in attempt:
        if i in code:
            nr_correct += 1
            
    return nr_correct

assert test_color("ABCD", "ABCD") == 4
assert test_color("ABCD", "ABCE") == 3
assert test_color("ABCD", "DCBA") == 4

def test_position(attempt, code):
    nr_correct = 0
    for i in range(len(attempt)):
        if attempt[i] == code[i]:
            nr_correct += 1
            
    return nr_correct

assert test_position("ABCD", "ABCD") == 4
assert test_position("ABCD", "ABCE") == 3
assert test_position("ABCD", "DCBA") == 0

def test_attempt(attempt, code):
    return f"{test_position(attempt, code)}-{test_color(attempt, code)}"


assert test_attempt("ABCD", "ABCD") == "4-4"
assert test_attempt("ABCD", "ABCE") == "3-3"
assert test_attempt("ABCD", "DCBA") == "0-4"
#endregion

#region count possibilities
def all_possibles(allow_duplicats=False, nr_of_fields=4, colors=get_all_colors()):
    possibles = []

    for first in colors:
        for second in colors:
            for third in colors:
                for fourth in colors:
                    if allow_duplicats or len(set([first, second, third, fourth])) == nr_of_fields:
                        possibles.append(first + second + third + fourth)
                        
    return possibles


def filter_possibles(possibles, attempt, result):
    new_possibles = []
    for possible in possibles:
        if test_attempt(attempt, possible) == result:
            new_possibles.append(possible)
            
    return new_possibles

#endregion
