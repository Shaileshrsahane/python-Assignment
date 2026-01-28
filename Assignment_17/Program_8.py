# Write a program which accepts one number from user and display below pattern
# Input : 5
# Output :  1    
          # 1    2
          # 1    2    3
          # 1    2    3    4
          # 1    2    3    4    5

def Pattern(No):
  Loop = 1
  for i in range(No):
    
    for i in range(1,Loop + 1):
      print(i,end= "    ")
    Loop = Loop + 1
    print()

def main():
  print("Enter number : ")
  Value = int(input())

  Pattern(Value)

if __name__ == "__main__":
  main()
