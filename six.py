# I've learned the disadvantages of immutability
def getMemoryBanks(str):
    return list(map(lambda x: int(x), str.split()))
    
def largestIndex(memory):
    maxIdx = 0
    for idx in range(len(memory)):
        if memory[idx] > memory[maxIdx]:
            maxIdx = idx
    return maxIdx
    
def redistributeBlocks(memory, maxIdx):
    num = memory[maxIdx]
    memory[maxIdx] = 0
    idx = (maxIdx + 1) % len(memory)
    while num > 0:
        memory[idx] += 1
        idx = (idx + 1) % len(memory)
        num -= 1
    return None

def iterate(memory):
    seen = []
    num = 0
    while memory not in seen:
        print str(memory)
        seen.append(list(memory))
        redistributeBlocks(memory, largestIndex(memory))
        num += 1
    print str(memory)
    return num
    
def main(str):
    memory = getMemoryBanks(str)
    res1 = iterate(memory) # Until we detect a loop
    # res2 = iterate(memory) # Get the size of the loop
    return res1
