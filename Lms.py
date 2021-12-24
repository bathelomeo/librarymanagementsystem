print("Hello and Welcome to Nathaniel's library system ")
Name=input('What is your Name ?')
if Name == ' ':
    print('put in something')
else:
    print('shish i just asked one question any good morning')
import datetime
now = datetime.datetime.now()
print('Current time is:')
print(now.strftime('%p'))
if (now.strftime("%p")) == "AM":
     print("Good morning!"+ Name)
elif (now.strftime("%p")) == "PM":
    print("Good Afternoon!"+ Name)
else:
    print('Good Evening!'+ Name)

gender = input('Are you male or female')
if gender == 'Male':
    print('Well hello Mr ' + Name)

if gender == 'Female':
    print('Hello Mrs '+ Name)
elif gender == ' ':
    print('put in something')
else:
    print('please just just put in something')
Thebook = input('What book do you want ' + Name)
if Thebook == ' ':
    print('Thats not a book ')
else:
    print('we dont have that')
Question= input('Have you picked the Book you wanted ''' + Name)
if Question == 'Yes':
    print('Good')
if Question == 'No':
    print('Take your time') 
elif Question == 'No' :
    print('stop that ''' + Name)
else:
   print('That stop that')
Notice = input('Pick the card in side and write your name on it '''+ Name)
if Notice == 'Ok':
    print('Lovely ''' + Name)
if Notice  == 'No':
    print('You cannot get the book until you do it '''+ Name)
elif Notice == ' ':
    print('Can you please just stop') 
else:
    print('please stop')  
notice = input('You need to Stamp the book as well '''+Name)
if notice== 'Ok':
    print('Here is the stamp''' + Name)
if notice == 'No':
    print('Yes you have do that'+ Name)
elif notice == ' ':
    print('if you keep that up it wil be exit the library for you ')
else:
    print('You cannot get the book until you do it '''+ Name)
ask = input('When will you return the book ''' + Name)
if ask == 'Tomorrow':
    print('Sorry i wont be here Tomorrow,but another librarian will be here ''' + Name)
if ask =='Next week':
    print('Fine with me ''' + Name)
if ask == ' ':
    print('why do you do this ):< ')
if ask == 'Next month':
    print('Sorry you have to return the book to the library in under two or three weeks ''' +Name)
    print('Or Else your book will have to be marked overdue '''+ Name)
if ask=='Some where with in this week':
    print('lovley '''+ Name)
elif ask == 'never':
    print('You dont get it do you'''+ Name)
else:
    print('Stop ')
print(+ ask + 'later')

# enchante = input('I see your back''' + Name)

# if enchante == 'yup':
#     print('Nice to see you again'''+ Name)
# if enchante == 'No':
#     print('Lol')
# elif enchante == ' ':
#     print('lol')
# else:
#     print('ok sure ):')
# thatBook =input('Do you have the book ''' + Name)

# if thatBook=='yes':
#     print('Just give me the book and you can choose to get a new one or not ''' + Name)
# else:
#     print('Then why did you come '''+ Name)
#     intr = input('Any way did you lose the book ''' +Name)
# if intr=='no ':
#     print('Very Good ''' + Name)
# else:
#     print('Ok')
# money = input('Do you have the money '''+ Name)
# if money == 'Yes':
#     print('Phew i was begining to think that i cant trust that you will pay for a book, Once lost ''' + Name)
# else:
#     print('Go and find the book now '''+ Name)
#     print('And if cant ,bring the money by this week ''' + Name)
#     print('Or else never get in again ''' + Name)