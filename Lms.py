Name=input('What is your Name ?')
print('Welcome to the library '''+ Name)
day = input('What time of day is it,Sorry i have been in the library all day since 6:00 '''+ Name)
if day == 'Morning ':
    print('Well Good Morning ''' + Name)
if day == 'Afternoon':
    print('Well Good Afternoon ''' + Name)
if day =='Evening':
    print('Well Good Evening '''+ Name)
else:
    print ('Wow its late !!! ''' + Name)
Thebook = input('What book do you want ''' + Name)
Book = input('Is the book do you want Fiction or Non Fiction ''' + Name)
if Book == 'Fiction':
    print('Then go to the right ''' + Name)
else:
    print('Go to the left''' + Name)
Question= input('Have you picked the Book you wanted ''' + Name)
if Question == 'Yes':
    print('Good')
else :
    print('Take your time ''' + Name)
Notice = input('Pick the card in side and write your name '''+ Name)
if Notice == 'Ok':
    print('Lovely ''' + Name)
else:
    print('You cannot get the book until you do it '''+ Name)
notice = input('You need to Stamp the book as well '''+Name)
if notice== 'Ok':
    print('Here is the stamp''' + Name)
else:
    print('You cannot get the book until you do it '''+ Name)
ask = input('when will you return the book ''' + Name)
if ask == 'Tomorrow':
    print('Sorry i wont be here Tomorrow,but another librarian will be here ''' + Name)
if ask =='Next week':
    print('Fine with me ''' + Name)
if ask == 'Next month':
    print('Sorry you have to return the book to the library in under three or three weeks ''' +Name)
    print('Or Else your book will have to be marked overdue '''+ Name)

if ask=='Some where with in this week':
    print('lovley '''+ Name)
else:
    print('You dont get it do you'''+ Name)
print('One or two'+ ask + 'later')

enchante = input('I see your back''' + Name)

if enchante == 'yup':
    print('Nice to see you again'''+ Name)
else:
    print('LOL')

thatBook =input('Do you have the book ''' + Name)

if thatBook=='yes':
    print('Just give me the book and you can choose to get a new one or not ''' + Name)
else:
    print('Then why did you come '''+ Name)
    intr = input('Any way did you lose the book ''' +Name)
if intr=='no ':
    print('Very Good ''' + Name)
else:
    print('Ok')
money = input('Do you have the money '''+ Name)
if money == 'Yes':
    print('Phew i was begining to think that i cant trust that you will pay for a book, Once lost ''' + Name)
else:
    print('Go and find the book now '''+ Name)
    print('And if cant ,bring the money by this week ''' + Name)
    print('Or else never get in again ''' + Name) 