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
    for i in range(length):
        if i == 0:
            moves.append(random.choice(mtypes))
        else:
            moves.append(random.choice(mtypes))
            while not valid(moves[i-1],moves[i]):
                try_new()
        moves[i] += random.choice(madd)
    return ' '.join(moves)
