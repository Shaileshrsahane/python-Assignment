#write a lambda function which accepts a list of number and return a list number who are divisible by 3 and 5

CheckDivisible = lambda No1 : No1 % 3 == 0 and No1 % 5 == 0

def main():
    List = []
    print("Enter the total number of elements: ")
    TotalNo = int(input())

    print("Enter the elements : ")
    for i in range(TotalNo):
      List.append(int(input()))

    UpdatedList = filter(CheckDivisible, List)

    print("the List with numbers divisible by 3 and 4 : ")
    for No in UpdatedList:
       print(No , end= " ")

if __name__ == "__main__":
    main()
