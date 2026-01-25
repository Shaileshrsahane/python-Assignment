#write a program which accepts radius of circle and print area
import math

def AreaCircle(No):
  Area = math.pi * (No ** 2)
  return Area

def main():
  print("Enter the radius of circle : ")
  radius = int(input())

  Area = AreaCircle(radius)
  print("Area of circle is : ",Area)

if __name__ == "__main__":
  main()
