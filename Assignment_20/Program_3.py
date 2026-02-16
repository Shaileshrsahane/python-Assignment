# 3: Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def Even(List1):
    EvenSum = 0
    Evenlist = []

    for No in List1:
        if No % 2 == 0:
            EvenSum = EvenSum + No
            Evenlist.append(No)

    print("Addition of even elements from the list is : ",EvenSum)
 
        
def Odd(List1):
    OddSum = 0
    Oddlist = []
    for No in List1:
        if No % 2 != 0:
            OddSum = OddSum + No
            Oddlist.append(No)

    print("Addition of odd element is : ",OddSum)

def main():

    Total = int(input("Enter total number of elements : "))

    List = []

    print("Enter the elements")
    for i in range(Total):
        List.append(int(input()))


    EvenFactor = threading.Thread(target= Even, args=(List,) )

    OddFactor = threading.Thread(target= Odd, args=(List,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

if __name__ == "__main__":
    main()
