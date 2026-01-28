# Write a program which accepts one number from user return number of digits in that number
# Input : 54564
# Output : 5

def CountDigits(No):
  iCount = 0
  while(No > 0):
    No = No // 10
    iCount = iCount + 1
  return iCount

def main():
  print("Enter number : ")
  Value = int(input())

  Digits = CountDigits(Value)
  print("Number of digits are : ",Digits)

if __name__ == "__main__":
  main()
