
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

def colors_not_in_use(possibles):
    colors = get_all_colors()
    for possible in possibles:
        for color in possible:
            if color in colors:
                colors.remove(color)
    return colors

def colors_sure_of(possibles):
    colors = list(possibles[0])
    for possible in possibles:
        test = colors.copy()
        for color in colors:
            if color not in possible:
                test.remove(color)
        if len(test) == 0:
            return []
        colors = test
    return colors

assert colors_sure_of(["ABCD", "ABCE", "ABCF", "GHIA"]) == ['A']
assert colors_sure_of(["ABCD", "ABCE", "ABCF"]) == ["A", "B", "C"]

def positions_sure_of(possibles):
    positions = list(possibles[0])
    
    for possible in possibles:
        test = positions.copy()
        for i in range(len(positions)):
            if positions[i] != possible[i]:
                test.remove(positions[i])
        if len(test) == 0:
            return []
        positions = test
    
    return positions

assert positions_sure_of(["ABCD", "ABCE", "ABCF"]) == ['A', 'B', 'C']
assert positions_sure_of(["ABCD", "ECBA", "ABCF"]) == []

def set_text_box_text(tb, text_lst):
    tb.configure(state="normal")
    tb.delete("0.0", "end")
    tb.insert("0.0",f"{', '.join(text_lst)}")
    tb.configure(state="disabled")
    
    print(text_lst)
#endregion
