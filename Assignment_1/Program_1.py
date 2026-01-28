# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
# parameters as number and perform the operation. Write on python program which call all the 
# functions from Arithmetic module by accepting the parameters from user.
import Arithmatic  # it is user defined module

def main():
  print("Enter first number : ")
  Value1 = int(input())

  print("Enter second number : ")
  Value2 = int(input())

  Addition = Arithmatic.Add(Value1,Value2)
  print("Addition is : ",Addition)
    
  Substraction = Arithmatic.Sub(Value1,Value2)
  print("Substraction is : ",Substraction)

  Multiplication = Arithmatic.Mult(Value1,Value2)
  print("Multiplication is : ",Multiplication)

  Division = Arithmatic.Div(Value1,Value2)
  print("Division is : ",Division)

if __name__ == "__main__":
  main()
