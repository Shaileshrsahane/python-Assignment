#write a lambda function  using reduce () which accepts a list of number and return product of number

from functools import reduce

AllProduct = lambda No1, No2 : No1 * No2

def main():
    List = []
    print("Enter the total number of elements: ")
    TotalNo = int(input())

    print("Enter the elements : ")
    for i in range(TotalNo):
      List.append(int(input()))

    Product = reduce(AllProduct, List)

    print("Product of all elements is : ",Product)

if __name__ == "__main__":
    main()
