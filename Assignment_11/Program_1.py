#write a program which accepts one number and check whether is it prime or not

def ChkPrime(No):
  Result = False
  for i in range(2,(int(No/2))):
    if(No % i == 0):
      Result = True
      break
  return Result

def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = ChkPrime(Value)

  if Ans == True:
    print(Value, "is not prime number")
  else:
    print(Value, "is prime number")


if __name__ == "__main__":
  main()
