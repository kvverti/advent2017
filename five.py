# Python implementation of puzzle 5
# Probably should add string ops to Lavender STL
def main(str):
    seq = list(map(lambda x: int(x), str.split()))
    count = 0
    pos = 0
    while pos >= 0 and pos < len(seq):
        tmp = pos
        pos += seq[pos]
        seq[tmp] += 1
        count += 1
    return count
    
def main2(str):
    seq = list(map(lambda x: int(x), str.split()))
    count = 0
    pos = 0
    while pos >= 0 and pos < len(seq):
        tmp = pos
        pos += seq[pos]
        if seq[tmp] < 3:
            seq[tmp] += 1
        else:
            seq[tmp] -= 1
        count += 1
    return count
