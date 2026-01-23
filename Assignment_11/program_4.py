#write a program which accepts one number print reverse of that number.
# Input : 143
# Output : 341

def PrintReverse(No):
  Reversed = 0

  # Result = []
  # while No > 0:
  #   Digit = No % 10
  #   No = No // 10

  #   Result.append((Digit))

  # for number in Result:
  #   print(number, end= "")

  # ------------------------------------------------------

  while No > 0:
    Digit = No % 10
    Reversed = (Reversed * 10) + Digit
    No = No // 10

  return Reversed

def main():
  print("Enter the number : ")
  Value = int(input())

  Result = PrintReverse(Value)
  print("Reversed number is : ",Result)

if __name__ == "__main__":
  main()
