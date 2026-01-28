#write a program which contains one function named as ChkNum(). that accepts one parameter as number. if number is even then it should 
#display "The number is even". otherwise display "the odd number"
def ChkNum(No):
  if(No % 2 == 0):
    print("The number is Even")
  else:
    print("The number is Odd")

def main():
  print("Enter number : ")
  Number = int(input())

  ChkNum(Number)
if __name__ == "__main__":
  main()    
