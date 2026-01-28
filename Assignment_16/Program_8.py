#Write a program which accepts one number from user and print number of "*" on screen
#Input : 5
#Output : * * * * *

def Display(No):
  for i in range(No):
    print("*",end= "  ")
    
def main():
  print("Enter the number : ")
  Value = int(input())

  Display(Value)

if __name__ == "__main__":
  main()    
