#write a lambda function which accepts a list of string and return the list of string who have length greater than 5

from functools import reduce

FilteredList = lambda String: len(String) > 5

def main():
    List = []
    print("Enter the total number of elements: ")
    TotalNo = int(input())

    print("Enter the elements : ")
    for i in range(TotalNo):
      List.append(input())

    UpdatedList = filter(FilteredList, List)

    print("the List who have string with greater than 5 alphabets : ")
    for String in UpdatedList:
       print(String , end= " ")

if __name__ == "__main__":
    main()
