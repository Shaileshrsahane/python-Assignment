#write a lambda function with reduce() which accepts a list and return the minimum element

from functools import reduce

Minimum = lambda No1, No2: No1 if (No1 < No2) else No2

def main():
    List = []
    print("Enter the total number of elements: ")
    TotalNo = int(input())

    print("Enter the elements : ")
    for i in range(TotalNo):
      List.append(int(input()))

    Min = reduce(Minimum, List)

    print("Minimum number is : ",Min)

if __name__ == "__main__":
    main()
