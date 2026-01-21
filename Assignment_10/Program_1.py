#write a program which accepts number and prints table of that number
def Table(No):
  i = 1
  for i in range(1,11):
    print(No * i, end ="  ")
    

def main():
  print("Enter the number")
  Value = int(input())

  Table(Value)

if __name__ == "__main__":
  main()
