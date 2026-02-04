# 3.Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# should filter out all such number which are even. Map function will calculate its square. 
# reduce will return addition of all that number

# Input List :   [1, 2, 3, 4, 5, 6]
# List after filter is :   [2, 4, 6]
# List after map is :    [4, 16, 36]
# Output after reduce is :  56

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

    FilterList = list(filter((lambda No : No % 2 == 0), List))
    print("List after filter is : ",end= "  ")
    print(FilterList)

    MapList = list(map(lambda No : No ** 2, FilterList))
    print("List after map is : ",end= "   ")
    print(MapList)

    ReduceList = functools.reduce(lambda No1, No2 : No1 + No2, MapList)
    print("Output after reduce is : ",ReduceList)

if __name__ == "__main__":
    main()
