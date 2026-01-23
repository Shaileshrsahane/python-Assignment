#write a program which accepts one number and print sum of digit.
#Input = 254
#Output = 2+5+4 = 11

def SumDigits(No):
  Sum = 0

  while No > 0:
    digit = No % 10
    Sum = Sum + digit
    
    No = No // 10  #due to double slash it will give answer only in int .and if we use single slash then it will give answer in float

  return Sum

def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = SumDigits(Value)

  print("Sum of Digits is : ",Ans)

if __name__ == "__main__":
  main()
