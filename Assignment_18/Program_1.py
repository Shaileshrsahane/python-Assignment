# Write a program which accepts N numbers from user and store it into the list and return Addition of all elements from the list
# Input : 10  20  30  40  50
# Output :  150

def AddList(NumList):
  Sum = 0
  
  for num in NumList:
    Sum = Sum + num
  return Sum

def main():
  print("Enter total number of elements : ")
  Total = int(input())

  List = []

  print("Enter the elements")
  for i in range(Total):
    List.append(int(input()))

  Addition = AddList(List)
  print("Addition of total elements from list is : ",Addition)

if __name__ == "__main__":
  main()
