# This is module for Program_5.py

def ChkPrime(No):
    Count = 0
    for i in range(1,No):
        if No % i == 0:
            Count = Count + 1
    if Count > 1:
        return False
    else :
        return True
    
