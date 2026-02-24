#asks for the required modules to use them in the script (all modules are either included of downloaded from https://pypi.org)
import vlc 
import time
import webbrowser
import curses
import keyboard

#asking if user has required modules to run the program
print("This program may not work without the following modules: vlc, time, webbrowser, keyboard, curses.\nPlease install them via pip3:")
print("Pip install python-vlc\npip install curses\npip install webbrowser\npip install keyboard\npip install windows-curses")
print('\nSome of these modules may not be neccasary but they will allow the program to run without errors.')
print("\nPress 'y' to continue or 'n' to exit.")

 #asks user if they are confident they can run the program as for having required modules
while True:  
    choice = input().lower()
    if choice == 'y':
        break
    elif choice == 'n':
        exit()
    else:
        print("Invalid choice. Please enter 'y' or 'n': ") #will only run if use enter invalid string

print('\npress F11 to enter fullscreen for the optimal experience, you can skip this.')#sets main term to fullscreen 
time.sleep(3)
    
#creating a basic starting menu.
openingvid = vlc.MediaPlayer(r"src/video/Tenna-intro.mp4")
openingvid.set_fullscreen(True) #sets the video to fullscreen
openingvid.play()
time.sleep(40) #required to make video play through without breaking script
openingvid.stop()

#from here the curses module will be used to make a simple start menu











