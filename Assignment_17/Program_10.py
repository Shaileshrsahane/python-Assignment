# Write a program which accepts one number from user return addition of digits of that number
# Input : 45677
# Output : 29

def AddDigits(No):
  Sum = 0
  while(No > 0):
    Digit = No % 10
    No = No // 10
    Sum = Sum + Digit
  return Sum

def main():
  print("Enter number : ")
  Value = int(input())

  Addition = AddDigits(Value)
  print("Sum of all digits is : ",Addition)

if __name__ == "__main__":
  main()
