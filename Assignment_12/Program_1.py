#write a program which accepts one character and check whether it is VoWel or not
#Input = a
#Output = Vowel
def ChkVowel(Char1):
  if ord(Char1) == 97 or ord(Char1) == 101 or ord(Char1) == 105 or ord(Char1) == 111 or ord(Char1) == 117:  #ord gives ascii value of character
    return True
  else:
    return False

def main():
  print("Enter the Character : ")
  CharValue = input()

  BResult = ChkVowel(CharValue)
  if (BResult == True):
    print(CharValue,"is a Vowel")
  else:
    print(CharValue,"is not a Vowel ")

if __name__ == "__main__":
  main()
