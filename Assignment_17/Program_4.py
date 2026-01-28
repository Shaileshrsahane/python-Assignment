# Write a program which accepts one number from user and return Addition of its factors
# Input : 12
# Output : 16         (1 + 2 + 3 + 4 + 6)

def FactorAddition(No):
  Ans = 0
  for i in range(1,No):
    if(No % i == 0):
      Ans = Ans + i
  return Ans

def main():
  print("Enter number : ")
  Value = int(input())

  Result = FactorAddition(Value)

  print(f"Addition of factors is : ",Result)

if __name__ == "__main__":
  main()
  
