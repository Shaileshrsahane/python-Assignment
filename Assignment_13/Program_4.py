#write a program which accepts one number and print Binary of that number
# Input : 10
# Output : 1 0 1 0

def PrintBinary(No):
  Binary = []
  while No != 0:
    Binary.append(No % 2)
    No = No // 2

  stop = (len(Binary)) // 2
  length = len(Binary) - 1

  for i in range(stop):
    

    last = Binary[length]

    first = Binary[i]

    Binary[i] = Binary[length]
    Binary[length] = first

    length = length - 1

  print(f"Binary of {No} is : ")

  for digit in Binary:
    print(digit, end= " ")

def main():
  print("Enter the number of which you want binary: ")
  Value = int(input())

  PrintBinary(Value)


if __name__ == "__main__":
  main()
