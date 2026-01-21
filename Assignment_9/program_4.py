#write a program which accepts a number and prints the cube

def Cube(No):
  Ans = No ** 3
  return Ans

def main():
  Value = int(input("Enter the number"))

  Result = Cube(Value)
  print("Cube is : ",Result)

if __name__ == "__main__":
  main()
  
