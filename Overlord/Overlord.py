import glob
filenames = glob.glob('Overlord/*.txt')
filenames = [filename.split('\\')[-1].replace('.txt', '') for filename in filenames]

def overlord():

   logo = open("Overlord/Overlord Logo", "r" ,encoding="utf8")
   Ovelord_logo = logo.read()
   print(Ovelord_logo)
 
   while True:
       choice = str(input("\nType Your Favorite Overlord Character. Exit = Q / List Avalieble Characters = L: ")) 
       while not choice:
          choice = str(input("Wrong input Try again?: ")) #kinda lazy
       file_path = f"Overlord/{choice}"
       if choice.lower() == "q":
          break
       elif choice.lower() == "l":
          print(filenames)
          continue
       try:
        with open(file_path+".txt", "r", encoding="utf8") as file:
            content = file.read()
            print(content)
       except FileNotFoundError:
            print("Not Found, Wrong Input")
       continue
overlord()