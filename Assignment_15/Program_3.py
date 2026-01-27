#write a lambda function using filter() which accepts list of numbers and return a list of odd number

def main():
  print("Enter total number of elements : ")
  Total = int(input())
  List = []

  print("Enter elements : ")
  for i in range(Total):
    List.append(int(input()))

  OddList = filter(lambda No : No % 2 != 0, List)

  print("Odd elements are : ")
  for odds in OddList:
    print(odds,end= " ")

if __name__ == "__main__":
  main()
