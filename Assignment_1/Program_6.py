# Write a program which accepts one number from user and print below pattern
# Input : 5
# Output :  *    *    *    *    *    
          # *    *    *    *
          # *    *    *
          # *    *
          # *

def Pattern(No):
  Loop = No
  for i in range(No):
    for i in range(Loop):
      print("*",end= "    ")
    print()
    Loop = Loop - 1

def main():
  print("Enter number : ")
  Value = int(input())

  Pattern(Value)

if __name__ == "__main__":
  main()
  
