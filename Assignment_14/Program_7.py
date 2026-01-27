#write a lambda function which accepts one and retrun true if it is divisible by 5
# Input : 35
# Output : True

CheckDivisible = lambda No: (No % 5 == 0)

def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = CheckDivisible(Value)
  print(Ans)

if __name__ == "__main__":
  main()
