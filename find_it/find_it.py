def find_it(seq):
    
    xor = 0
    for i in seq:
        xor = xor ^ i
    return xor
