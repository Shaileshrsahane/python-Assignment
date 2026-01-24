#write a program which accepts two number and print addition , substraction, division, multiplication

def Addition(No1,No2):
  print("Addition is : ",No1 + No2)

def Substraction(No1,No2):
  print("Substraction is : ",No1 - No2)

def Multiplication(No1,No2):
  print("Multiplication is : ",No1 * No2)

def Division(No1,No2):
  if(No2 == 0):
    print("Incorrect Value for division")
    return
  print("Division is : ",No1 / No2)

def main():
  print("Enter first NUmber : ")
  Value1 = int(input())

  print("Enter second NUmber : ")
  Value2 = int(input())

  Addition(Value1, Value2)
  Substraction(Value1, Value2)
  Multiplication(Value1, Value2)
  Division(Value1, Value2)


if __name__ == "__main__":
  main()
