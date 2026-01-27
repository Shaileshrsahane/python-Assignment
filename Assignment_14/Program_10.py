#write a lambda function which accepts three number and return Largest number
# Input : 10 5 15
# Output : 15

Maximum = lambda No1, No2, No3: max(No1,No2,No3)

def main():
  print("Enter the first number : ")
  Value1 = int(input())

  print("Enter the second number : ")
  Value2 = int(input())

  print("Enter the  number : ")
  Value3 = int(input())

  Ans = Maximum(Value1, Value2, Value3)
  print("Maximum is : ",Ans)

if __name__ == "__main__":
  main()
