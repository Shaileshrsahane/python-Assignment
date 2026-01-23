#write a program which accepts one number and print the odd number till that number

def PrintOdd(No):
  for i in range(1,No+1,2):
    print(i, end= " ")

def main():
  print("Enter the number : ")
  Value = int(input())

  PrintOdd(Value)


if __name__ == "__main__":
  main()
