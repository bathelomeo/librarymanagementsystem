print("Hello and Welcome to Nathaniel's Library System ")
from curses.ascii import isalpha
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

while True:
    Name=(input("What is your name"))
    if isalpha() and (len(Name) > 2 and len(Name) <=10):
        print('Right name')
        break;
    else:
        print ("Please enter right Name")
        continue

print(Name)

Gender= input('Are you Male or Female')

if Gender == 'Male':
    print('Hello Mr ' + Name)

if Gender == 'Female':
    print('Hello Mrs '+ Name)
elif Gender ==' ':
    ('invalid input')
# print("""This are the books we have:
#       The hungry Cartapilla
#       The diary of a wimpy kid all books
#       Harry potter all 7 books
#       Horrid henry
#       Dog man
#       Captain underpants 
#       The lion king all 3 books 
#       The Last Olympian(Percy Jackson and the Olympians)
#       Diary of a 6 grade ninja 
#       Big nate
#       The last kids on Earth
#       Dork Diaries
#       Vampire Academy
#       The Magicians.
#       The Golden Compass
#       Fantastic beasts and where to find them
#       """)

# aos =input('''Are you an admin or student 
# if you are a student your name is your password ''')

# spassword=(Name)
# apassword =('admin')

# for i in range(3):
#     pwd= input('Please enter you password')
#     j=3
#     if (pwd==apassword):
#         print('Welcome Administrator')
        
#         print("""this is all your permited do do:
#         recommend a book (to be in this library)
#         borow a book
#         return a book
#         distribute books (that we have)
#         see bookes your (and other students) have both borrowed and returned,for that type (All lists)
#         see how many students are using the library, for that type(See all students)""")
        
#         abook = input('What are you here to do')
        
#         if abook == ' Recomend a book':
#             recommend = input('What book do you want to recommend')
#             print('We will try get that soon ')
        
#         if abook == ' Return a book':
#             print("Please give me your book i'l take it from there")
        
#         if abook == 'I am borowing':
#             right = input ('What book do you want to borow from the list?')
#             print('Here is the book you asked for, the'+ right)
        
#         if abook == 'List of every borowed and returned books':
#             book = input("""But first, how many book have you borowed
#             and their names""")
#             print('Adrien has borrowed 1 books The lion king(Hakuna matata) ')
#             print("""Monica has borrowed 4 books Big Nate
#             The magicians
#             The lion king simbas pride
#             Fantastic beasts and where to findThem (Newt Scamander)""")
#             print("""Tyrone has borowed 2 books
#             Diary of a wimpy kid(old school)
#             Harry potter(chamber of secrets) """)
#             print('Veronica has borowed 3 books Dork Diaries,Vampire Academy,The golden compass')

#             print("And here's the list " + book)
        
#         if abook == 'See all students':
#             print('Currently, Adrien, Veronica, Tyrone, Monica,')
#     if (pwd==spassword):
#         print('Welcome Student')
#         print("""this is all you can do
#          Recommend a book (to be in this library)
#         borow a book, for that type(I am borowing)
#         return a book
#         see bookes you (yourself)have both borrowed and returned,for that type (My list)""")
        
#         sbook= input('What have you come to do')
        
#         if sbook == ' Recommend a book ':
#             bookinlibrary = input('What book do you want to recommend')
#             print('We will try get that soon ')
        
#         if sbook == 'Returning':
#             print("Please give me your book i'l take it from there")
        
#         if sbook == 'I am borowing':
#             right = input ('What book do you want to borow from the list?')
#             print('Here is the book you asked for the'+right)
        
#         if sbook == 'My List':
#             book = input("""how many book have you borowed
#             and their names""")
#             print("Here's the list :" + book)
#         break
#     else:
#         print('incorrect password chances left',j-i)
#         continue
# print('\nSee you next time')