#write a program which accepts one number and print that many number in reverse order 
# Input : 5
# Output : 5 4 3 2 1

def PrintSequence(No):
  for i in range(No):
    print(No-i, end= " ")

def main():
  print("Enter the NUmber : ")
  Value = int(input())

  PrintSequence(Value)

if __name__ == "__main__":
  main()
