import random as r
import string


def generate_index():
    S = string.ascii_uppercase
    ind = (''.join(r.sample(S, 2)) + str(r.randrange(100))
           + "_" + str(r.randrange(100)) + ''.join(r.sample(S, 2)))
    return ind
