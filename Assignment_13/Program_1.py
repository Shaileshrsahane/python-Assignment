#write a program which accepts length and width of rectangle and print area

def RectangleArea(No1, No2):
  return No1 * No2

def main():
  print("Enter the length of rectangle : ")
  length = int(input())

  print("Enter the width of rectangle : ")
  width = int(input())

  Area = RectangleArea(length,width)
  print("Area of rectangle is : ",Area)

if __name__ == "__main__":
  main()
