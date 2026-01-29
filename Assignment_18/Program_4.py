# Write a program which accepts N numbers from user and store it into the list. Accept one number from user and return frequency of that number
# Input : Number of elements : 6
# Input : 70  15  35  15  14  15
# Input : Element to search : 15
# Output : 3

def PrintFrequency(NumList,Number):
  Count = 0
  
  for num in NumList:
    if num == Number:
      Count += 1
  return Count

def main():
  print("Enter total number of elements : ")
  Total = int(input())

  List = []

  print("Enter the elements")
  for i in range(Total):
    List.append(int(input()))

  print("Enter the element who's frequency have to check : ")
  target = int(input())

  Frequency = PrintFrequency(List,target)
  print(f"frequency of {target} is : ",Frequency)

if __name__ == "__main__":
  main()
