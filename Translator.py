import sqlite3

conn = sqlite3.connect("words.db")
c = conn.cursor()

#c.execute('''CREATE TABLE chavacanowords(
#  chavacanoword text,
#  filipinoword text,
#englishword text
  
#  )''')

def add_word(): 
  chavacano = input("Enter word in Chavacano: ")
  filipino = input("Enter translation in Filipino: ")
  english = input("Enter translation in English: ")
  enter = "INSERT INTO chavacanowords (chavacanoword, filipinoword, englishword) VALUES(?, ?, ?)"
  c.execute(enter, (chavacano, filipino, english))
  conn.commit()
  
def translate():
  text = input("\nEnter language: ")
  ins = text.lower()
  langlist = ["eng", "english", "fil", "filipino", "tag", "tagalog"]
  translatedwords = []
  if ins in langlist:
    if ins == "eng" or ins =="english":
      lang = "english"
      text = input("Enter text: ")
      basket = text.split()
      for i in basket:
        search = "SELECT * FROM chavacanowords WHERE englishword = ?"
        c.execute(search, (i.title(), ))
        result = c.fetchone()
        if result:
          translatedwords.append(result[0])
        else:
          translatedwords.append(i)
      
    elif ins == "fil" or ins == "filipino" or ins == "tag" or ins == "tagalog":
      lang = "filipino"
      text = input("\nEnter text: ")
      basket = text.split()
      for i in basket:
        search = "SELECT * FROM chavacanowords WHERE filipinoword LIKE ? OR filipinoword LIKE ?"
        c.execute(search, ('%'+i+'%', '%'+i.title()+'%'))
        result = c.fetchone()
        print(f"Result: {result} \n")
        if result:
          translatedwords.append(result[0])
        else:
          translatedwords.append(i)
        
    else:
      print("Invalid Input")
  translated_text = ' '.join(translatedwords)
  print(f"Translated text: {translated_text.lower()} \n")
      
def checkword():
  check = "SELECT * FROM chavacanowords"
  c.execute(check)
  print(c.fetchall() )
  print("")

checkword()
while True:
  add_word()
 # option = input("Enter command: ")
#  if option.lower() == "add word":
  #  add_word()
#  elif option.lower() == "check db":
 #   checkword()
 # elif option.lower() == "translate":
 #   translate()
  
  

