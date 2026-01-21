#write a program which accepts one  number and check whether does it divisible by 3 and 5

def BoolCheck(No):
  if (No % 3 == 0) and (No % 5 == 0):
    return True

def main():
  print("Enter the number")
  Value = int(input())

  Result = BoolCheck(Value)

  if Result == True:
    print("The Number is divisible by 3 and 5")
  else:
    print("The Number is not divisible by 3 and 5")
    

if __name__ == "__main__":
  main()
