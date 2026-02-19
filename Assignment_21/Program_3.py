# 3: Design a Python application where multiple threads update a shared variable.
#  Use a Lock to avoid race conditions.
#  Each thread should increment the shared counter multiple times.
#  Display the final value of the counter after all threads complete execution.

import threading

lobj = threading.Lock()

Counter = 0

def Update(Frequency):
    global Counter
    for i in range(Frequency):
        with lobj:
            Counter = Counter + 1

def main():
    global Counter

    Total = int(input("Enter the frequency "))

    Thread1 = threading.Thread(target= Update, args= (Total,))

    Thread2 = threading.Thread(target= Update, args= (Total,))
    Thread3 = threading.Thread(target= Update, args= (Total,))

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("Value of counter is : ",Counter)

if __name__ == "__main__":
    main()
