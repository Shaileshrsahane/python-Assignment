#write a lambda function which accepts one number and return square of that number
# Input : 3
# Output : 9

Square = lambda No: No**2

def main():
  print("Enter the marks : ")
  Value = int(input())

  Ans = Square(Value)
  print(f"Square of {Value} is : ",Ans)

if __name__ == "__main__":
  main()
