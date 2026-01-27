#write a lambda function using map() which accepts list of numbers and return a list of square of each number

def main():
  print("Enter the number of elements : ")
  Total = int(input())
  
  List = []

  print("Enter the elements : ")
  for i in range(Total):
    List.append(int(input()))

  SquareList = map(lambda No : No**2, List)

  print("Square of elements is : ")

  for Square in SquareList:
    print(Square, end= " ")


if __name__ == "__main__":
  main()
