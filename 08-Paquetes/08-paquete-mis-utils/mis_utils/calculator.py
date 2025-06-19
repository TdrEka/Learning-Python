
def calculator(n1, n2, math_thing):
    if math_thing not in ('+', '-', '*', '/'):
        return "das hard"
    elif math_thing == '+':
        return n1 + n2
    elif math_thing == '-':
        return n1 - n2
    elif math_thing == '*':
        return n1 * n2
    else:
        if n2 == 0:
            return "why do you hate me?"
        else:
            return n1 / n2