#write a program which accept one number and print sum of first N natural number
def SumNatural(No):
  Sum = 0
  for i in range(No+1):
    Sum = Sum + i

  return Sum

def main():
  print("Enter the number")
  Value = int(input())

  Result = SumNatural(Value)

  print("Sum of natural number is : ",Result)

if __name__ == "__main__":
  main()
