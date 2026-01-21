#write a program which accepts one number and print factorial of that number
def Factorial(No):
  Fact = 1
  for i in range(1,No + 1):
    Fact = Fact * i
  return Fact

def main():
  print("Enter the number")
  Value = int(input())

  Result = Factorial(Value)

  print("Factorial is : ",Result)

if __name__ == "__main__":
  main()
