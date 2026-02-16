# 1: Design a Python application that creates two threads named Prime and NonPrime.
#  Both threads should accept a list of integers.
#  The Prime thread should display all prime numbers from the list.
#  The NonPrime thread should display all non-prime numbers from the list.

import threading

lobj = threading.Lock()

def DisplayPrime(List1):
    with lobj:
        print("Prime numbers are : ")
        for No in List1:
            Count = 0

            for i in range(1,No):
                if No % i == 0:
                    Count = Count + 1
                    if Count == 2:
                        break  

            if Count < 2:
                print(No)
    
def DisplayNonPrime(List1):
     with lobj:
        print("Non prime numbers are : ")
        for No in List1:
            Count = 0

            for i in range(1,No):
                if No % i == 0:
                    Count = Count + 1
                    if Count == 2:
                        print(No)
                        break

def main():

    Total = int(input("Enter total number of elements : "))

    Listdigits = []

    for i in range(Total):
        Listdigits.append(int(input()))

    prime = threading.Thread(target= DisplayPrime, args= (Listdigits,))

    NonPrime = threading.Thread(target= DisplayNonPrime, args= (Listdigits,))

    prime.start()
    NonPrime.start()

    prime.join()
    NonPrime.join()

if __name__ == "__main__":
    main()
