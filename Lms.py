print("Hello and Welcome to Nathaniel's Library System ")
import datetime
now = datetime.datetime.now()
print('Current time is:')
print(now.strftime('%Y-%M-%D %H:%M %p'))
if (now.strftime("%p")) == "AM":
     print("So Good morning!")
elif (now.strftime("%p")) == "PM":
    print("So Good Afternoon!" )
else:
    print('Good Evening!')



Name = input('What is your name')

Gender= input('Are you Male or Female')

if Gender == 'Male':
    print('Hello Mr ' + Name)

if Gender == 'Female':
    print('Hello Mrs '+ Name)
elif Gender ==' ':
    ('invalid input')
print("""This are the books we have:
      The hungry Cartapilla
      The diary of a wimpy kid all books
      Harry potter all 7 books
      Horrid henry
      Dog man
      Captain underpants 
      The lion king all 3 books 
      The Last Olympian(Percy Jackson and the Olympians)
      Diary of a 6 grade ninja 
      Big nate
      The last kids on Earth
      Dork Diaries
      Vampire Academy
      The Magicians.
      The Golden Compass
      The tales of beedles the bard
      """)

aos =input('''Are you an admin or student 
if you are a student your name is your password ''')

spassword=(Name)
apassword =('admin')

for i in range(3):
    pwd= input('Please enter you password')
    j=3
    if (pwd==apassword):
        print('Welcome Administrator')
        print("""this is all your permited do do:
        recommend a book to be in this library
        borow a book
        return a book
        distribute books that we have 
        see bookes your (and other students) have both borrowed and returned
        see how many students are using the library""")
        abook = input('So why are you here ')
        if abook == 'recomend':
            recommend = input('What book do you want to recommend')
            print('We will try get that soon ')
        if abook == 'returning':
            print("Please give me your book i'l take it from there")
        if abook == 'borow':
            right = input ('What book do you want to borow from the list?')
            print('Here is the book you asked for the'+right)
        if abook == 'List of your borowed and returned books':
            book = input("""how many book have you borowed
            and their names""")
            print("here's the list " + book)
        if abook == 'to See how many students':
            print('Currently,Adrien,Veronica,Tyrone,Monica,')
    if (pwd==spassword):
        print('Welcome Student')
        print("""this is all you can do
        recommend a book to be in this library
        borow a book
        return a book
        see bookes you (yourself)have both borrowedand returned""")
        sbook= input('So why are you here')
        if sbook == 'recomend':
            recommend = input('What book do you want to recommend')
            print('We will try get that soon ')
        if sbook == 'returning':
            print("Please give me your book i'l take it from there")
        if sbook == 'borow':
            right = input ('What book do you want to borow from the list?')
            print('Here is the book you asked for the'+right)
        if sbook == 'List of borowed and returned books':
            book = input("""how many book have you borowed
            and their names""")
            print("here's the list " + book)
        break
    else:
        print('incorrect password chances left',j-i)
        continue
print('\nSee you next time')