# Write a program which accepts N numbers from user and store it into the list and return minimum number from list
# Input : 10  50  30  40  20
# Output :  10

def ChkMinimum(NumList):
  Minimum= NumList[0]
  
  for num in NumList:
    if(Minimum > num):
      Minimum = num
  return Minimum

def main():
  print("Enter total number of elements : ")
  Total = int(input())

  List = []

  print("Enter the elements")
  for i in range(Total):
    List.append(int(input()))

  Min = ChkMinimum(List)
  print("Minimum number from list is : ",Min)

if __name__ == "__main__":
  main()
