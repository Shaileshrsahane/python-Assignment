# 2: Design a Python application that creates two threads.
#  Thread 1 should calculate and display the maximum element from an list.
#  Thread 2 should calculate and display the minimum element from the same list.
#  The list should be accepted from the user

import threading

lobj = threading.Lock()

def Maximum(List1):
    Max = List1[0]

    for No in List1:
        if Max < No:
            Max = No
    
    print("Maximum element is : ",Max)
            
def Minimum(List1):
    Min = List1[0]

    for No in List1:
        if Min > No:
            Min = No

    print("Minimum element is : ",Min)

def main():

    Total = int(input("Enter total number of elements : "))

    Listdigits = []

    for i in range(Total):
        Listdigits.append(int(input()))

    Thread1 = threading.Thread(target= Maximum, args= (Listdigits,))

    Thread2 = threading.Thread(target= Minimum, args= (Listdigits,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()
