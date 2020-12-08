import random as rd

def rand_num(max):
    return rd.randint(0, max)

def rand_str(dict, size):
    return ''.join(rd.choice(dict) for x in range(size))