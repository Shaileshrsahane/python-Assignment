#write a program which accepts one number and print that many number starting from 1
# Input : 5
# Output : 1 2 3 4 5

def PrintSequence(No):
  for i in range(1,No+1):
    print(i,end= " ")

def main():
  print("Enter the NUmber : ")
  Value = int(input())

  PrintSequence(Value)

if __name__ == "__main__":
  main()
