#write a lambda function using filter() which accepts list of numbers and return a list of even number


def main():
  print("Enter the number of elements : ")
  Total = int(input())
  
  List = []

  print("Enter the elements : ")
  for i in range(Total):
    List.append(int(input()))

  EvenList = filter(lambda No : No % 2 == 0, List)

  print("even elements are : ")

  for even in EvenList:
    print(even, end= " ")


if __name__ == "__main__":
  main()
