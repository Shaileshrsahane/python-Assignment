# Write a program which accepts one number from user and check whether it is prime or not
# Input : 5
# Output : it is prime number       

def ChkPrime(No):
  Count = 0
  for i in range(1,No):
    if(No % i == 0):
      Count = Count + 1
  return(Count > 1)

def main():
  print("Enter number : ")
  Value = int(input())

  BResult = ChkPrime(Value)

  if BResult == True:
    print("it is Not prime number")
  else:
    print("It is prime number")

if __name__ == "__main__":
  main()
