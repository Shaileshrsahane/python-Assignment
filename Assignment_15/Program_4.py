import functools
#write a lambda function using reduce() which accepts list of numbers and return a sum of all numbers

def main():
  print("Enter total number of elements : ")
  Total = int(input())
  List = []

  print("Enter elements : ")
  for i in range(Total):
    List.append(int(input()))

  TotalSum = functools.reduce(lambda No1, No2 : No1 + No2, List)

  print("Total Sum is : ",TotalSum)

if __name__ == "__main__":
  main()
