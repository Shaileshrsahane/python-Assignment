# 2: Design a Python application that creates two threads named EvenFactor and 
# OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message: 
# “Exit from main”

import threading

def Even(No):
    EvenSum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 == 0:
            EvenSum = EvenSum + i
 
    print("addition of even Factors is : ",EvenSum)
        
def Odd(No):
    OddSum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 != 0:
            OddSum = OddSum + i

    print("Addition of odd factors is : ",OddSum)

def main():
    value = int(input("Enter the number : "))

    EvenFactor = threading.Thread(target= Even, args=(value,) )

    OddFactor = threading.Thread(target= Odd, args=(value,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
