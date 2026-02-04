# 1: Design a Python application that creates two separate threads named Even and Odd.
#  The Even thread should display the first 10 even numbers.
#  The Odd thread should display the first 10 odd numbers.
#  Both threads should execute independently using the threading module.
#  Ensure proper thread creation and execution.

import threading

def Even():
    Count = 0
    No = 1
    while (Count < 10):
        if No % 2 == 0:
            Count = Count + 1
            print(No)
        No = No + 1

def Odd():
    Count = 0
    No = 0

    while(Count < 10):
        if No % 2 != 0:
            Count = Count + 1
            print(No)
        No = No + 1

def main():
    # Even()
    # Odd()

    Thread1 = threading.Thread(target= Even)

    Thread2 = threading.Thread(target= Odd)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()
