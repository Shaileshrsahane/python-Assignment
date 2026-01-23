#write a program which accepts one number and print number of digits in that number

def CountDigits(No):
  Count = 0
  while No > 0:
    Count = Count + 1
    No = (No // 10)

  return Count
    
def main():
  print("Enter the number : ")
  Value = int(input())

  Ans = CountDigits(Value)

  print("Number of digits is : ",Ans)

if __name__ == "__main__":
  main()
