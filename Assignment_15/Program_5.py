import functools
#write a lambda function using reduce() which accepts list of numbers and return maximum number

Maximum = lambda No1, No2: No1 if (No1 > No2) else No2

def main():
  print("Enter total number of elements : ")
  Total = int(input())
  List = []

  print("Enter elements : ")
  for i in range(Total):
    List.append(int(input()))

  Max = functools.reduce(Maximum , List)

  print("Maximum is : ",Max)

if __name__ == "__main__":
  main()
