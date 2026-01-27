#write a lambda function which accepts one and retrun true if it is even otherwise return false
# Input : 34
# Output : True

IsEven = lambda No: (No % 2 == 0)

def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = IsEven(Value)
  print(Ans)

if __name__ == "__main__":
  main()
