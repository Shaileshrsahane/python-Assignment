# write a program which contains one lambda function which accepts two parameter and return multiplication 
# Input : 10  5
# Output : 50

Multiplication = lambda No1, No2: No1 * No2

def main():
  print("Enter first number : ")
  Value1 = int(input())

  print("Enter second number : ")
  Value2 = int(input())

  Ans = Multiplication(Value1, Value2)

  print("Multiplication is : ",Ans)

if __name__ == "__main__":
  main()
