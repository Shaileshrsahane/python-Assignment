#write program which accepts one number and print square

def Square(No):
  Ans = No ** 2
  return Ans
  

def main():
  print("Enter number : ")
  Value = int(input())

  Result =  Square(Value)

  print("Square is : ",Result)

if __name__ == "__main__":
  main()
