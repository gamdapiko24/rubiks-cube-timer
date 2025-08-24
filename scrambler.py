# scrambler.py

import random

def scramble3x3(length):
    def valid(bfr,crnt):
        if [bfr,crnt] in ntogether:
            return False
        else:
            return True
    def try_new():
        moves.pop(-1)
        moves.append(random.choice(mtypes))
        
    ntogether = [['R','L'],
                 ['F','B'],
                 ['D','U'],
                 ['L','R'],
                 ['B','F'],
                 ['U','D',]]
    
    mtypes = ['R','L','F','B','D','U']
    madd = ['',"'",'2']
    moves = []

    def scramble2x2():
        return scramble3x3(10)

    for _ in range(length):
        moves.append(random.choice(mtypes))
        if len(moves) > 1:
            while not valid(moves[-2],moves[-1]):
                try_new()
            while moves[-2] == moves[-1]:
                try_new()
    
    for i in range(length):
        moves[i] += random.choice(madd)
    return ' '.join(moves)