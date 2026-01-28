#Write a program which display first 10 even number on screen
#Input : nothing
#Output : 2   4   6   8   10   12   14   16   18   20  

def DisplayEven():
  Count = 0
  i = 1
  while(Count != 10):
    if(i % 2 == 0):
      print(i, end= "   ")
      Count = Count + 1
    i = i + 1

def main():

  DisplayEven()

if __name__ == "__main__":
  main()    
