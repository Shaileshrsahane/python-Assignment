# Write a program which accepts one number from user and return factorial
# Input : 5
# Output : 120

def Factorial(No):
  Ans = 1
  for i in range(1,No+1):
    Ans = Ans * i
  return Ans

def main():
  print("Enter number : ")
  Value = int(input())

  Fact = Factorial(Value)

  print(f"Factorial of {Value} is : ",Fact)

if __name__ == "__main__":
  main()
