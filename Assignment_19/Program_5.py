# 3.Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
# return maximum number from that numbers.

# Input List :   [1, 2, 17, 19, 15, 16, 14, 12]
# List after filter is :   [1, 2, 17, 19]
# List after map is :    [2, 4, 34, 38]
# after reduce Maximum is :  38

def ChkPrime(No):
    iCount = 0
    Bool = True

    for i in range(1,No):
        if(No % i == 0):
            iCount = iCount + 1
            
            if iCount == 2:
                Bool = False

                break
    return Bool

import functools

def main():

    print("Enter total number of elements : ")
    stop = int(input())

    List = []

    print("Enter the elements : ")
    for i in range(stop):
        List.append(int(input()))

    print("Input List : ",end="  ")
    print(List)

    FilterList = list(filter(ChkPrime, List))
    print("List after filter is : ",end= "  ")
    print(FilterList)

    MapList = list(map(lambda x : x * 2, FilterList))
    print("List after map is : ",end= "   ")
    print(MapList)

    Maximum = functools.reduce(lambda x, y: x if x > y else y,MapList)

    print("Maximum is : ",Maximum)

if __name__ == "__main__":
    main()
