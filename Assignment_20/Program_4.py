# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
#  All threads should accept a string as input.
#  The Small thread should count and display the number of lowercase characters.
#  The Capital thread should count and display the number of uppercase characters.
#  The Digits thread should count and display the number of numeric digits.
#  Each thread must also display:
#  Thread ID
#  Thread Name

import threading

def findSmall(List1):
    CountSmall = 0

    for i in List1:
        if ord(i) >= 97 and ord(i) <= 122:
            CountSmall = CountSmall + 1

    print("Number of lowerclass characters are : ",CountSmall)
    print("Thread name  of lowerclass characters : ",threading.current_thread().name)
    print("Thread ID  of lowerclass charactrs: ",threading.get_ident())
 
def findCapital(List1):
    CountCapital = 0

    for i in List1:
        if ord(i) >= 65 and ord(i) <= 90:
            CountCapital = CountCapital + 1

    print("Number of Upperclass characters are : ",CountCapital)
    print("Thread name  of Upperclass element: ",threading.current_thread().name)
    print("Thread ID  of upperclass element: ",threading.get_ident())


def findDigits(List1):
    CountDigits = 0
    for i in List1:
        if ord(i) >= 48 and ord(i) <= 57:
            CountDigits = CountDigits + 1
        
    print("Number of digits are : ",CountDigits)
    print("Thread name of digits : ",threading.current_thread().name)
    print("Thread ID is of digits: ",threading.get_ident())

def main():

    InputString = (input("Enter the string : "))

    List = list(InputString)

    small = threading.Thread(target= findSmall, args=(List,) )

    captital = threading.Thread(target= findCapital, args=(List,))

    digits = threading.Thread(target= findDigits, args=(List,))

    small.start()
    captital.start()
    digits.start()

    small.join()
    captital.join()
    digits.join()


if __name__ == "__main__":
    main()
