#write a lambda function which accepts two number and return the minimum 
# Input : 10 34
# Output : 10

Minimum = lambda No1 ,No2: (No1 < No2)

def main():
  print("Enter the first number : ")
  Value1 = int(input())

  print("Enter the first number : ")
  Value2 = int(input())

  Ans = Minimum(Value1, Value2)
  if(Ans == True):
    print("Minimum number is : ",Value1)
  else:
    print("Minimum number is : ",Value2)
if __name__ == "__main__":
  main()
