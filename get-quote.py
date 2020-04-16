import random

def primary():
 string = "Keep it logically awesome\d"
 print(string)

 f = open("quotes.txt")
 quotes = f.readlines()
 f.close()


 rnd = random.randint(0, 13)
 print(quotes[rnd])

if __name__== "__main__":
  primary()
