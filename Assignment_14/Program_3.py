#write a lambda function which accepts two number and return the maximum 
# Input : 10 34
# Output : 34

Greater = lambda No1 ,No2: (No1 > No2)

  

def main():
  print("Enter the first number : ")
  Value1 = int(input())

  print("Enter the first number : ")
  Value2 = int(input())

  Ans = Greater(Value1, Value2)
  if(Ans == True):
    print("Greater number is : ",Value1)
  else:
    print("Greater number is : ",Value2)
if __name__ == "__main__":
  main()
