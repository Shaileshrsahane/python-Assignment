#Write a program which acccepts name from user and print the length of name
#Input : Marvellous
#Output : 10 

def CountChar(Name):
  return len(Name)

def main():
  print("Enter the word")
  Word = input()

  Length = CountChar(Word)
  
  print("Length is : ",Length)

if __name__ == "__main__":
  main()    
