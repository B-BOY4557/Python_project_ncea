#asks for the required modules to use them in the script (all modules are either included of downloaded from https://pypi.org)
import vlc 
import time
import webbrowser
from curses import wrapper
import keyboard
import os

#clears terminal window
def clearterm():
    os.system('cls' if os.name == 'nt' else 'clear')

#asking if user has required modules to run the program
print("This program may not work without the following modules: vlc, time, webbrowser, keyboard, curses.\nPlease install them via pip3:")
print("Pip install python-vlc\npip install curses\npip install webbrowser\npip install keyboard\n")
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
"""
openingvid.set_fullscreen(True) #sets the video to fullscreen
openingvid.play()
time.sleep(40) #required to make video play through without breaking script
"""
openingvid.stop()

#clear terminal and show title screen
clearterm()

#Title screen
curseslogo = """                           
       @@@@@             @@@@@    @@@@@                                                                                    
       @---@             #---@    *---@                                                                                    
       @---@             #---@    *---@                                                                                    
@*======---@ @=========@ #---@ @==----===@@+===========@ @=========@@===@ @===@ @=========@ %========*@
@*---------@ @=--------@ #---@ @=-------=@@+----=-----=@ @=--===--=@@=-=@ @---@ @=-------=@ %--------*@
@*---------@ @=--------@ #---@ @--------=@@+---####+--=@ @=--% @=-=@@=-=@ @---@ @=-------=@ %--------*@
@*---------@ @=--*@@@@@@ #---@    *---@   @+----##*---=@ @=--% @@@@@@=--------@ @=--*@@=-=@ %---@@@@@@@
@*---------@ @=--*@@@@@@ #---@    *---@   @+----------=@ @=--%      @=--------@ @=--+@@=-=@ %---@@@@@@@
@*---------@ @=--------@ #---@    *---@   @+---=@@%---=@ @=--%      @=--------@ @=--+@@=-=@ %--------*@
@@@@@@@@@@@@ @@@@@@@@@@@ @@@@@    @@@@@   @@@@@@@@@@@@@@ @@@@@      @@@@@@@@@@@ @@@@@@@@@@@ @@@@@@@@@@@
                                               QUIZ
				   PRESS F1 AT ANY TIME FOR A GUIDE
"""
print(curseslogo)
time.sleep(5)
clearterm()

#intrestingly this and the openingvid shit itself if now ran in powershell python interpriter... THE MORE YOU KNOW!!!
instance = vlc.Instance()
media_list = instance.media_list_new()
media_list.add_media(r"src/mus/TV_GAME.ogg")
bgmus = instance.media_list_player_new()
bgmus.set_media_list(media_list)
bgmus.set_playback_mode(vlc.PlaybackMode.loop)
bgmus.play()

def tickanim(): #will display is awncer is correct
    correctsnd = vlc.MediaPlayer(r"src/mus/snd-won.mp3")
    correctsnd.play()
    for i in range(3):
       
        clearterm()
        print("""

                                                                                                        
    ████████████████████████████████████████████████████████████████████████████████████████████████  
    ████████████████████████████████████████████████████████████████████████████████████████████████  
    ████████████████████████████████████████████████████████████████████████████████████████████████  
    ████████████████████████████████████████████████████████████████████████████████████████████████  
        ██████████████████████████████████████████████████████████████████████  ███████████████████    
        ████████████████████████████████████████████████████████████████████       ████████████████    
        ██████████████████████████████████████████████████████████████████           ██████████████    
        █████████████████████████████████████████████████████████████████            ██████████████    
        ███████████████████████████████████████████████████████████████                ████████████    
        █████████████████████████████████████████████████████████████                ██████████████    
        █████████████████████████████████████████████████████████                ████████████████    
        ███████████████████████████████████████████████████████               ████████████████       
        ██████████████████████████████████████████████████████              ██████████████████       
        ████████████████████████████████████████████████████                ██████████████████       
        ██████████████████████████████████████████████████                ████████████████████       
        ████████████████████████████████████████████████               ███████████████████████       
            ███████████████████████████████████████████                █████████████████████████       
            █████████████████████████████████████████                ███████████████████████████       
            █████████████████████████████████████████                ███████████████████████████       
            ████████████  █████████████████████████                ███████████████████████████         
            █████████       █████████████████████               ██████████████████████████████         
            █████           ████████████████                ████████████████████████████████         
            ███████           ████████████                ██████████████████████████████████         
            ████████           ███████████               ███████████████████████████████████         
            ██████████           ███████               █████████████████████████████████████         
            ████████████           ██                ███████████████████████████████████████         
            ██████████████                         ███████████████████████████████████████           
                █████████████                     █████████████████████████████████████████           
                ███████████████                 ███████████████████████████████████████████           
                ████████████████               ████████████████████████████████████████████           
                ██████████████████           ██████████████████████████████████████████████           
                ████████████████████       ████████████████████████████████████████████████           
                ███████████████████████████████████████████████████████████████████████████           
                    ███████████████████████████████████████████████████████████████████████             
                    ██████████████████████████████████████████████████████████████████████              
                    ██████████████████████████████████████████████████████████████████████              
                                                                                                        

    """)
        time.sleep(.5)
        clearterm()
        print(" ")  
        time.sleep(.5)
#make one of the tick for when your wrong.

#I think everything works now. HERES TO BEG I  CAN START THE QUIZ NOW!!!