#write a program which contains one function named as Add(). that accepts two number from user and return addition of twp number
# Input = 10 5
# Output = 15
def Add(No1, No2):
  return No1 + No2

def main():
  print("Enter first number : ")
  Number1 = int(input())

  print("Enter second number : ")
  Number2 = int(input())

  Addition = Add(Number1, Number2)
  print("Addition is : ",Addition)

if __name__ == "__main__":
  main()    
