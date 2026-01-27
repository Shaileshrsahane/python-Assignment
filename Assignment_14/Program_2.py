#write a lambda function which accepts one number and return cube of that number
# Input : 3
# Output : 27

Square = lambda No: No**3

def main():
  print("Enter the marks : ")
  Value = int(input())

  Ans = Square(Value)
  print(f"cube of {Value} is : ",Ans)

if __name__ == "__main__":
  main()
