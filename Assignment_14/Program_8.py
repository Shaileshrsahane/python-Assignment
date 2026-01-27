#write a lambda function which accepts two number and return addition
# Input : 10 11
# Output : 21

Addition = lambda No1, No2: No1 + No2

def main():
  print("Enter the number : ")
  Value1 = int(input())

  print("Enter the number : ")
  Value2 = int(input())

  Ans = Addition(Value1, Value2)
  print("Addition is : ",Ans)

if __name__ == "__main__":
  main()
