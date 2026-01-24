#write a program which accepts one Number and print its factors
#Input = 12
#Output = 1 2 3 4 6 12
def PrintFactors(No):
  for i in range(1,No + 1):
    if No % i == 0:
      print(i,end= " ")


def main():
  print("Enter the Character : ")
  Value = int(input())

  PrintFactors(Value)


if __name__ == "__main__":
  main()
