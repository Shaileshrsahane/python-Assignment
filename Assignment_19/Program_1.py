# write a program which contains one lambda function which accepts one parameter and return power of two
# Input : 5
# Output : 25

Square = lambda No : No ** 2

def main():
  print("Enter total number of elements : ")
  Value = int(input())

  Ans = Square(Value)

  print(f"Power of {Value} is : ",Ans)

if __name__ == "__main__":
  main()
