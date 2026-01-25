#write a program which accepts one number and print check whether is it perfect number or not
# Input : 6
# Output : perfect

def ChkPerfect(No):
  Sum = 0
  for i in range(1,No):
    if(No % i == 0):
      Sum = Sum + i
  print(Sum)

  if Sum == No:
    return True


def main():
  print("Enter the number: ")
  Value = int(input())

  Result = ChkPerfect(Value)

  if(Result == True):
    print(f"{Value} is perfect number")
  else:
    print(f"{Value} is not a perfect number")


if __name__ == "__main__":
  main()
