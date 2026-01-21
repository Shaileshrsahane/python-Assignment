#write a program which accepts one number prints Even number till that number
def PrintEven(No):
  for i in range(2,No+1):
    print(i)
    
def main():
  print("Enter the number")
  Value = int(input())

  PrintEven(Value)


if __name__ == "__main__":
  main()
