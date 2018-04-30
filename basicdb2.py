import pymysql
from gtts import gTTS
import os
import speech_recognition as sr


db=pymysql.connect("den1.mysql2.gear.host","alasya2","alasya2.0","alasya2")
def talk(u):
 tts = gTTS(text=u, lang='en-us')
 tts.save("hel.mp3")
 os.system("mpg321 hel.mp3")

def recognize():
 try:
  r = sr.Recognizer()
  with sr.Microphone() as source:
   audio = r.listen(source)
  output = r.recognize_google(audio)
  return output
 except:
  output=recognize()
  return output

def recognize1():
 try:
  r = sr.Recognizer()
  with sr.Microphone() as source:
   audio = r.listen(source)
  output = r.recognize_google(audio)
  return output
 except:
  output=''
  return output

g=1
f=1
h=1
while(g==1):
 talk("Login or Register")
 output=recognize()
 print("You said: " + output)
 g=0
 if(output!='register'):
  if(output!='login'):
   talk("I didn't get it exactly , come again")
   g=1

g=1
if(output=='register'):
 while(g==1):
  talk("Username please")
  name=recognize()
  print("You said: " + name)
  p = db.cursor()
  p.execute("SELECT name1 FROM contacts")
  check = p.fetchall()
  for user in check:
   if(user==name):
    talk("Username already exists , try a new one")
    h=0
    break
  if(h==1):
   g=0
 talk("Password please")
 password=recognize()
 print("You said: " + password)
 insert = db.cursor()
 insert.execute("INSERT INTO contacts (name1,name2) VALUES('" + name + "','" + password + "');")
 db.commit()
 insert.close()

elif(output=='login'):
 while(f==1):
  talk("Username")
  user = recognize()
  print("You said: " + user)

  g=1
  h=1
  talk("Password")
  password = recognize()
  print("You said: " + password)
  p = db.cursor()
  p.execute("SELECT name1,name2 FROM contacts")
  check = p.fetchall()
  for username,pas in check:
   if(user==username):
    g=0
    if(password==pas):
     h=0
     f=0
     break
  if(g==1):
   talk("Username does not exist")
  elif(g==0 and h==1):
   talk("Password does not match")

g=1
while (g == 1):
 talk("With whom you want to chat")
 friend = recognize()
 print("You said: " + friend)
 p = db.cursor()
 p.execute("SELECT name1 FROM contacts")
 check = p.fetchall()
 for name in check:
  name= ''.join(name)
  if (name == friend):
   g = 0
   break
 if (g == 1):
  talk("That user does not have an account , try another name please")

a=0;k=0
no1=0
no2=0
p=db.cursor()
p.execute("SELECT name1,name2,text1,text2 FROM contacts")
c=p.fetchall()
for f,k,i,j in c:
 if(j=='' and k==user and f==friend) :
  print(i)
  no1+=1
 if(j=='' and k==friend and f==user):
  print(' '*40,end='')
  print(i)
  no2+=1
p.close()
k=0
while(a!=1):
 p=db.cursor()
 p.execute("SELECT * FROM contacts")
 c = p.fetchall()
 num1=0
 num2=0
 for f, w, i, j in c:
  if (j == '' and w == user and f == friend):
   if(no1<num1):
    no1+=1
    print(i)
   num1 += 1
  if (j == '' and w == friend and f == user):
   if(no2<num2):
    no2+=1
    print(' ' * 40, end='')
    print(i)
   num2 += 1
 p.close()
 if(k!=0 and message!=''):
  c = db.cursor()
  c.execute("INSERT INTO contacts (name1,name2,text1,text2) VALUES('" + user + "','" + friend + "','" + message + "',' ');")
  c.execute("SELECT text1,text2 FROM contacts")
  z=c.fetchall()
  for i,j in z:
   x=i
  print(' '*40,end='')
  print(x)
  c.close()
 db.commit()
 talk("Message here")
 message = recognize1()

 k+=1
 if(message=="hey buddy stop"):
  talk("Bye")
  break
db.close()










