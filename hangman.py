import random
#game logic
word=list()
lives=6
word_iter=0
letter=""
letters_guessed=list()
decision_num=random.randrange(20)
if(decision_num==0):
   language="C"
if(decision_num==1):
   language="Java"
if(decision_num==2):
   language="C++"
if(decision_num==3):
   language="Ruby"
if(decision_num==4):
   language="Clojure"
if(decision_num==5):
   language="LISP"
if(decision_num==6):
   language="COBOL"
if(decision_num==7):
   language="BASIC"
if(decision_num==8):
   language="Haskell"
if(decision_num==9):
   language="Perl"
if(decision_num==10):
   language="PHP"
if(decision_num==11):
   language="Kotlin"
if(decision_num==12):
   language="Scheme"
if(decision_num==13):
   language="Ada"
if(decision_num==14):
   language="Forth"
if(decision_num==15):
   language="Fortran"
if(decision_num==16):
   language="Rust"
if(decision_num==17):
   language="Javascript"
if(decision_num==18):
   language="R"
if(decision_num==19):
   language="Lua"
if(decision_num==20):
   language="Smalltalk"
#graphics logic
def graphics():
   if (lives==6):
      print(" ---^")
      print("|")
      print("|")
      print("|")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==5):
      print(" ---^")
      print("|   0")
      print("|")
      print("|")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==4):
      print(" ---^")
      print("|   0")
      print("|   |")
      print("|")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==3):
      print(" ---^")
      print("|   0")
      print("|   |")
      print("|   ^")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==2):
      print(" ---^")
      print("|   0")
      print("|   |\\")
      print("|   ^")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==1):
      print(" ---^")
      print("|   0")
      print("|  /|\\")
      print("|  / \\")
      print("_______")
      print("\\       \\")
      print("\\ \\_______\\")
      print("  \\|_______|")
   if (lives==0):
      print(" ________")
      print("\\  RIP   \\")
      print("\\ \\________\\")
      print("  \\|_______|")
      print("    @@@@@@@@@@")
      print("    //////////")
      print("    GAME OVER")
#open sequence error checker
try:
   text = input("Hangman. Press Enter") 
   if text.lower()=="exit":
      exit()
except KeyboardInterrupt as a:
   print(a)
except EOFError as e:
   print(e)
except:
   pass


for spaces in language:
   word.append("_"+" ")
#the game loop
while(lives>0):
   #score, lives, and letters guessed
   print("\nLetters Guessed:"+" "+"".join(letters_guessed)+"\n")
   print("Tries Left"+" "+str(lives))
   #resets iterator to circle to index in word
   word_iter=0
   #the underscore index
   print("\n"+"".join(word))
   #the letter loop to check for letter and errors
   try:
      letter = input("Please enter a letter"+" ")
   except KeyboardInterrupt as a:
       print(a)
   except EOFError as e:
       print(e)
   except:
       pass
    #makes sure character is not a number of other invalid input
      
   if letter.isnumeric==True:
      try:
         letter = input("Please enter a letter, not a number"+" ")
         continue    
      except KeyboardInterrupt as a:
         print(a)
      except EOFError as e:
         print(e)
      except:
         pass
   #make sure it is only one character and that there is no unwanted data
   if len(letter)>1:
      if letter.lower()=="exit":
         exit()
      try:
         letter = input("Please enter a single character please"+" ")
         continue    
      except KeyboardInterrupt as a:
         print(a)
      except EOFError as e:
         print(e)
      except:
         pass
   #checks if the letter is in the language that was chosen, evaluates for einning conditions, and changes _ when needed 
   if (letter.lower() in language.lower()):
      word_iter=0
      graphics()
      for characters in language:
         word_iter=word_iter+1
         if (letter.lower()==characters.lower()):
            if word[word_iter-1]!="_":
               word[word_iter-1]=letter
      if "".join(word).strip().lower()==language.strip().lower():
         print("YOU WIN! HOW DARE YOU HANG AN INNOCENT MAN!")
         exit()
 # wrong guess else statement           
   else:
      letters_guessed.append(letter+" ")
      
      lives=lives-1
      print("\n")
      graphics()
