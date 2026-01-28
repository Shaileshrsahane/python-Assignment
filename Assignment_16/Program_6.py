#Write a program which Accepts nummber from user and check whether the number is positive, negative or zero
# Input = 4
# Output = positive 

# Input = -8
# Output = Negative 

# Input = 0
# Output = zero 

def ChkNumber(No):
  if(No > 0):
    print("Number is positive")
  elif(No < 0):
    print("Number is negative")
  elif(No == 0):
    print("Number is zero")

def main():
  print("Enter the number : ")
  Value = int(input())

  ChkNumber(Value)

if __name__ == "__main__":
  main()    
