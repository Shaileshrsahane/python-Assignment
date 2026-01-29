# Write a program which accepts N numbers from user and store it into the list and return Maximum number from list
# Input : 10  50  30  40  20
# Output :  50

def ChkMaximum(NumList):
  Maximum= 0
  
  for num in NumList:
    if(Maximum < num):
      Maximum = num
  return Maximum

def main():
  print("Enter total number of elements : ")
  Total = int(input())

  List = []

  print("Enter the elements")
  for i in range(Total):
    List.append(int(input()))

  max = ChkMaximum(List)
  print("Maximum number from list is : ",max)

if __name__ == "__main__":
  main()
