#write a program which accepts one number and check whether it is palindrome or not
#Input = 121
#Output = it is palindrome

def ChkPalindrome(No):
  OriginalNo = No #because you are dividing no so it will become zero to store actual value we need new variable as OriginalNo
  Number = 0

  while No > 0:
    Digit = No % 10
    Number = (Number * 10) + Digit
    No = No // 10
  if Number == OriginalNo:
    return True
  else:
    return False

def main():
  print("Enter the number : ")
  Value = int(input())

  BResult = ChkPalindrome(Value)
  if (BResult == True):
    print(Value,"is a palindrome number")
  else:
    print(Value,"is not a palindrome number")

if __name__ == "__main__":
  main()
