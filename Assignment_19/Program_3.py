# 3.Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# should filter out all such numbers which greater than or equal to 70 and less than or equal to 
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List :   [85, 75, 73, 25, 45]
# List after filter is : [85, 75, 73]
# List after map is :    [95, 85, 83]
# Output after reduce is :  670225

import functools

Multiplication = lambda No1, No2: No1 * No2

lambda No : No >= 70 and No <= 90 

lambda No : No + 10

lambda No1, No2 : No1 * No2



def main():
    print("Enter total number of elements : ")
    stop = int(input())

    List = []

    print("Enter the elements : ")
    for i in range(stop):
        List.append(int(input()))

    print("Input List : ",end="  ")
    print(List)

    FilterList = list(filter((lambda No : No >= 70 and No <= 90 ), List))
    print("List after filter is : ",end= "  ")
    print(FilterList)

    MapList = list(map(lambda No : No + 10, FilterList))
    print("List after map is : ",end= "   ")
    print(MapList)


    ReduceList = functools.reduce(lambda No1, No2 : No1 * No2, MapList)
    print("Output after reduce is : ",ReduceList)

if __name__ == "__main__":
    main()
