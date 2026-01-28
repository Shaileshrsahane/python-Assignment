# Write a program which accepts one number from user and display below pattern
# Input : 5
# Output :  1    2    3    4    5    
          # 1    2    3    4    5
          # 1    2    3    4    5
          # 1    2    3    4    5
          # 1    2    3    4    5

def Pattern(No):
  for i in range(No):
    for i in range(1,No+1):
      print(i,end= "    ")
    print()

def main():
  print("Enter number : ")
  Value = int(input())

  Pattern(Value)

if __name__ == "__main__":
  main()
