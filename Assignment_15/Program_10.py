#write a lambda function  using filter() which accepts a list of number and count even number

EvenNum = lambda No1 : No1 % 2 == 0

def main():
    List = []
    count = 0
    print("Enter the total number of elements: ")
    TotalNo = int(input())

    print("Enter the elements : ")
    for i in range(TotalNo):
      List.append(int(input()))

    EvenList = filter(EvenNum, List)

    print("Even numbers are : ")
    for Even in EvenList:
      count = count + 1
      print(Even,end= " ")
    print()

    RealList = list(EvenList)
    length = len(RealList)

    print("Total Even number is : ",count)

if __name__ == "__main__":
    main()
