def findNonDuplicate(arr):
    xor = 0
    for i in arr:
        xor ^= i
    
    return xor