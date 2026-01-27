#write a lambda function which accepts one and retrun true if it is odd otherwise return false
# Input : 35
# Output : True

IsOdd = lambda No: (No % 2 != 0)

def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = IsOdd(Value)
  print(Ans)

if __name__ == "__main__":
  main()
