#Write a program which contains one functions that accepts one number and return True if it is divisible by 5 else return False
# Input = 15
# Output = True 

def ChkDivisible(No):
  if(No % 5 == 0):
    return True
  else:
    return False

def main():
  print("Enter the number : ")
  Value = int(input())

  BResult = ChkDivisible(Value)
  print(BResult)

if __name__ == "__main__":
  main()    
