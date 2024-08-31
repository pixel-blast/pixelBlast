import pyttsx3
# https://github.com/nateshmbhat/pyttsx3         -    Voice Model
import pygame
# https://github.com/pygame/pygame               -    Pygame
import os
# Included in python
import datetime
# Included in python
import pywhatkit
# https://github.com/Ankit404butfound/PyWhatKit  -    PyWhatKit 
import wikipedia
# https://github.com/goldsmith/Wikipedia         -    Wikipedia
import pyjokes
# https://github.com/pyjokes/pyjokes             -    Pyjokes   
import webbrowser as wb
# Included in python

def clear():
    # Uses clear command in OS using os.system
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()

pygame.mixer.init()
print('Welcome to Pixel Blast - A virtual assistant made using python')
# Pixel Blast by Goutham Kumar

'''
Run this code in terminal
pip install pyttsx3 pygame

That's it folks! Now enjoy Pixel Blast
'''

engine = pyttsx3.init()
# Starting voice model
voices = engine.getProperty('voices')
# Getting different voices
engine.setProperty('voice', voices[1].id)
# Assigning voice model

def talk(text):
    # Pixel Blast speaking
    engine.say(text)
    engine.runAndWait()

def song(path):
    # Playing songs
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def print_commands():
    # Printing Available commands
    print('Song - Play Limited Songs')
    print('Time - Tells The time')
    print('Exit - To Exit Pixel Blast')
    print('Stop - To stop currently playing music')
    print('Table - To print mathematical tables')
    print('Calculator - To use a calculator with formulas built in')
    print('Snapchat - Opens official snapchat webpage')
    print('Instagram - Opens official instagram webpage')
    print('ChatGPT - Opens official chatgpt webpage')
    print('Youtube - Opens official Youtube Webpage')
    print('Joke - Tells you a joke')
    print('Search - Gets you information from wikipedia')
    print('Play - Play things on youtube directly from Pixel Blast')
    print('Google - Search things from google')

def time():
    # Tells current time
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current Time: ' + time)
    talk('Current Time:' + time)

def time_greeting():
    # Greets the user based on time
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print('Good Morning')
        talk('Good Morning')
    elif 12 <= hour < 16:
        print('Good Afternoon')
        talk('Good Afternoon')
    elif 16 <= hour < 21:
        print('Good Evening')
        talk('Good Evening')
    else:
        print('Have A Good Night')
        talk('Have A Good Night')

time()
time_greeting()

redirector = int(input('Press 0 to read manual or 1 to enter Pixel Blast: '))
# Redirecting User to assistant or manual
if redirector == 0:
    print('Printing Available Commands')
    talk('Printing Available Commands')
    print_commands()
else:
    print('Proceeding to Pixel Blast')
    talk('Proceeding to Pixel Blast')

user_name = str(input('Enter Username:  '))
password = str(input('Enter password:  '))

def main():
    while True:
        # The Pixel Blast
        talk('How can I help you?')
        queryRaw = str(input('How can I help you?  '))
        query = queryRaw.lower()

        if 'play' in query:
            # Playing things on youtube using PyWhatKit
            youtube = query.replace('play', '')
            print('Playing ', youtube, 'On Youtube')
            talk('Playing ' + youtube + 'On Youtube')
            pywhatkit.playonyt(youtube)
            print('Check your Browser')

        elif 'google' in query:
                # Searching things on google using PyWhatKit
                text = str(input('What do you want to search today:  '))
                pywhatkit.search(text)

        def calc():
            # Pixel Calculator
            # A calculator using basic arithmetic operators
            # Includes maths formula's
            talk('Hello')
            print("Welcome to Pixel Calculator")
            talk('Welcome to Pixel Calculator')
            print('')
            print('Where do you want to go to')
            print('')
            print('Press 1 to go to Basic Calculator')
            print('Press 2 to go to the Formula section')
            talk("Tell me the number and I will teleport you to that world")
            calRedirect = int(input("Tell me the number and I will teleport you to that world?  "))

            def basic_console():
                print("Basic Calculator Py")
                talk('Welcome to Basic Calculator')
                talk(' ')
                print('Available Operators  +  -  /  *')
                talk('Available Operators are Add, Subtract, Multiply and Divide.')
                o = input("Choose Operator")

                def add():
                    first_num = int(input("Enter First Number  "))
                    b = int(input("Enter Second Number  "))
                    a_var = (b + first_num)
                    print(a_var)
                    talk(a_var)

                if o == "+":
                    add()

                def sub():
                    first = int(input("Enter First Number  "))
                    b = int(input("Enter Second Number  "))
                    print(b - first)
                    talk(b - first)

                if o == "-":
                    sub()

                def mul():
                    first_num = int(input("Enter First Number  "))
                    b = int(input("Enter Second Number  "))
                    print(b * first_num)
                    talk(b * first_num)

                if o == "*":
                    mul()

                def div():
                    first = int(input("Enter First Number  "))
                    b = int(input("Enter Second Number  "))
                    print(b / first)
                    talk(b / first)

                if o == "/":
                    div()

            def formula():
                print('')
                print("Available Formula's")
                print("Circle Sector")
                print("")
                print("1 for Area")
                print("2 for Perimeter")
                print('')
                print("Square Sector")
                print("Press 3 to find area of a square")
                print("Press 4 to find the Perimeter of a square")
                print('')
                print('Rectangle Area')
                print("Press 5 to find the area of a Rectangle")
                print("Press 6 to find the Perimeter of a Square")
                print('Press 7 to find profit')

                acer = str(input("Which formula do you wish to execute ? "))

                def carea():
                    ca = float(input("Tell me the radius of the Circle"))
                    p = 22 / 7
                    ans = p * ca ** 2
                    print(ans)
                    talk(int(ans))

                if acer == "1":
                    carea()

                def cperi():
                    cp = float(input("Tell me the radius of the Circle"))
                    cpans = 22 / 7
                    pans = 2 * cpans * cp
                    print(pans)
                    talk(int(pans))

                if acer == "2":
                    cperi()

                def sqarea():
                    sa = float(input("Tell me side length of the square"))
                    cans = sa * sa
                    print(cans)
                    talk(int(cans))

                if acer == "3":
                    sqarea()

                def sqperi():
                    spe = float(input("Tell me side length of the square"))
                    spans = spe * 4
                    print(spans)
                    talk(int(spans))

                if acer == "4":
                    sqperi()

                def recarea():
                    rab = float(input("Tell my the Breadth of the Rectangle"))
                    ral = float(input("Tell my the Length of the Rectangle"))
                    rans = rab * ral
                    print(rans)
                    talk(int(rans))

                if acer == "5":
                    recarea()

                def recperi():
                    rperb = float(input("Tell my the Breadth of the Rectangle"))
                    rperl = float(input("Tell my the Length of the Rectangle"))
                    rpans = (rperb + rperl) * 2
                    print(rpans)
                    talk(int(rpans))

                if acer == "6":
                    recperi()

                def profit():
                    sp = int(input('Enter Selling Price'))
                    cp = int(input('Enter Cost Price'))
                    fin = sp - cp
                    print(fin)
                    talk(int(fin))

                if acer == '7':
                    profit()

                def loss():
                    sp = int(input('Enter Selling Price'))
                    cp = int(input('Enter Cost Price'))
                    fin = cp - sp
                    print(fin)
                    talk(int(fin))

                if acer == '8':
                    loss()

                def profitper():
                    profit_1 = int(input('Enter Profit'))
                    cp = int(input('Enter Cost Price'))
                    profit_1 = (profit_1 / cp) * 100
                    print(profit_1 + '%')
                    talk(int(profit_1 + '%'))

                if acer == '9':
                    profitper()

                def losper():
                    loss_1 = int(input('Enter Loss'))
                    cp = int(input('Enter Cost Price'))
                    profit_2 = (loss_1 / cp) * 100
                    print(profit_2 + '%')
                    talk(int(profit_2 + "%"))

                if acer == '10':
                    losper()

            if calRedirect == 1:
                basic_console()

            elif calRedirect == 2:
                formula()

        def table():
            # Generates tables using for loop
            print('Table Generator')
            talk('Table Generator')
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            num = int(input('Which Table do you want'))
            for number in numbers:
                result = num * int(number)
                resultString = (str(result))
                print(resultString)

        if 'time' in query:
            # Tdlls current time on request
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current Time is ' + time)
            talk('Current Time is ' + time)

        elif 'search' in query:
            # Gets information from wikipedia
            search = query.replace('search ', '')
            info_line = int(input('How many Lines of Info do you Want:  '))
            info = wikipedia.summary(search, info_line)
            print(info)

        elif 'joke' in query:
            # Tells you a joke using pyjokes
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'youtube' in query:
            # Opens youtube's website using webbrowser
            print('Opening Youtube')
            talk('opening Youtube')
            print('Check your default browser')
            talk('Check your default browser')
            wb.open('https://www.youtube.com/')

        elif 'chatgpt' in query:
            # Opens chatgpt's website using webbrowser
            print('Opening ChatGPT')
            talk('opening ChatGPT')
            print('Check your default browser')
            talk('Check your default browser')
            wb.open('https://chat.openai.com/')

        elif 'instagram' in query:
            # Opens instagram's website using webbrowser
            print('Opening Instagram')
            talk('opening Instagram')
            talk('Check your default browser')
            print('Check your default browser')
            wb.open('https://www.instagram.com/')

        elif 'calculator' in query:
            # Opens the calculator previously created
            calc()

        elif 'snapchat' in query:
            # Opens snapchat's website using webbrowser
            print('Opening SnapChat')
            talk('opening Snap Chat')
            talk('Check your default browser')
            print('Check your default browser')
            wb.open('https://www.snapchat.com/')

        elif 'table' in query:
            # Opens the previously created table generated
            table()

        elif 'tp' in query:
            # Just prints what you type
            tp = str(input('What do you want me to print'))
            print(tp)

        elif 'birthday' in query:
            # Sings you a happy birthday song
            song('song/happy_birthday.mp3')

        elif 'song' in query:
            # Plays limited songs using pygames library
            print('Available Songs are')
            Songs_Avai = ['Happy Birthday', 'Demon Slayer 1', 'Demon Slayer 2', 'Demon Slayer 3', 'Demon Slayer 4', 'Demon Slayer 5', 'Tauba Tauba', 'The Boys', 'Naadaniya']
            for songs in Songs_Avai:
                print(songs)
            songRaw = str((input('Which song do you want to play:  ')))
            songtreated = songRaw.lower()

            if 'tauba' in songRaw:
                song("song/tauba.mp3")

            elif 'happy birthday' in songtreated:
                song('song/happy_birthday.mp3')

            elif 'demon slayer 1' in songtreated:
                song('song/dm_1.mp3')

            elif 'demon slayer 2' in songtreated:
                song('song/dm_2.mp3')

            elif 'demon slayer 3' in songtreated:
                song('song/dm_3.mp3')

            elif 'demon slayer 4' in songtreated:
                song('song/dm_4.mp3')

            elif 'demon slayer 5' in songtreated:
                song('song/dm_5.mp3')

            elif 'the boys' in songtreated:
                song('song/the_boys.mp3')

            elif 'unstoppable' in songtreated:
                song('song/unstoppable.mp3')

            elif 'naadaniyan' in songtreated:
                song('song/naadaniyan.mp3')

            else:
                print('Song not available, contact developer')

        elif 'exit' in query:
            # Closes Pixel Blast
            exit_prompt_raw = str(input('Do you really want to exit:  '))
            exit_prompt = exit_prompt_raw.lower()
            if 'yes' in exit_prompt:
                print('Thank you for using Pixel Blast')
                talk('Thank you for using Pixel Blast')
                exit(0)

            elif 'no' in exit_prompt_raw:
                pass

        elif 'stop' in query:
            # Stops music being played by pygames
            pygame.mixer.music.stop()
            print('Song Stopped')

        else:
            # To retry not recognised commands
            print('Unrecognised command please refer to command list')
            print_commands()

    # Developer available at gouthamkumara2@gmail.com

# Using logical operators and nested if else statement

if user_name == 'admin' and password =='pass101':
    print('Login Successful')
    main()
else:
    print('Login failed, try again')
    user_name_retry = str(input('Enter Username:  '))
    password_retry = str(input('Enter password:  '))
    if user_name_retry == 'admin' and password_retry =='pass101':
        print('Login Successful')
        main()
    else:
        print('Rerun program to try again')

