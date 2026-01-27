#write a program which accepts marks and dispay grade

def printGrade(No):
  if(No > 100):
    print("invalid percentage")
    return

  if(No < 50):
    print("Result is : Fail")
  elif(No >= 50 and No <= 59):
    print("Result is : pass")
  elif(No >= 60 and No <= 74):
    print("Result is : first class")
  elif(No >= 75):
    print("Result is : distinction")

def main():
  print("Enter the marks : ")
  Value = int(input())

  printGrade(Value)

if __name__ == "__main__":
  main()
