def ChkGreater(No1,No2):
  if (No1 > No2):
    print("Greater number is : ",No1)
  else:
    print("Greater number is : ",No2)



def main():
  print("Enter first number")
  Value1 = int(input())

  print("Enter second number")
  Value2 = int(input())
   
  ChkGreater(Value1, Value2)

if __name__ == "__main__":
  main()
