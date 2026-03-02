#asks for the required modules to use them in the script (all modules are either included of downloaded from https://pypi.org)
import vlc 
import time
import os

#clears terminal window
def clearterm():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0 #sets score to 0 at the start of the quiz

#asking if user has required modules to run the program
print("This program uses the python-vlc module included in the .venv folder included")
print("\nplease be sure you have vlc installed on your computer from https://www.videolan.org/vlc/index.html")
time.sleep(3)

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
    global score
    score = score + int("1")
    for i in range(3):
       
        clearterm()
        print(f"""score: {score}

                                                                                                        
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
        print(f"score: {score}")  
        time.sleep(.5)
    clearterm()
#make one of the tick for when your wrong.
def uhohanim(): #will display is awncer is wrong
    for i in range(3):
       
        clearterm()
        print(f"""score: {score}                                                                                            
█████████████████████████████████████████████████████████████████████████████████████████████████████████
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
██▓                                                                                                   ▓██
 ██▓                                                                                                 ▓██
 ██▓▒                                                                                                ▓██
 ██▓▒                                                                                                ▓██
 ██▓▓▒                                                                                              ▓▓██
   ██▒                                                                                              ▓██
   ██▒                                                                                              ▓██
    ██▓                                                                                           ▒▓█
    ██▓                                                                                           ▒██
    ██▓                                                                                           ▒██
     █▓▓                                                                                        ▒▓██
     ██▓                                                                                         ▓██
      ██▓                                                                                         ▓██
     ██▓▒                                                                                       ▒▓██
      ██▓                                                                                       ▓██
      ██▓                                                                                       ▓██
      ██▓                             ▒▓▓▒▓▓▓▓▓ ▓▓▓    ▒▓█▓▒▓▓▓ ▓▓▒                             ▓██
       ██▓▒                           ▒▓▓▒▓█▓▓█▓▓█▓▓▓▓▓█▓▒▓█▓█▓▓▓█▒                            ▓██
       ██▓▒                           ▒▓▓▒▓█▓▓█▓▓█▓▓▓▓▓█▓▒▓█▓█▓▓▓█▒                            ▓██
        ██▓▒                           ▒▓▓▓▓▒▓▓ ▓▓▓    ▒▓▓▓ ▒▓▓ ▓▓▒                          ▒▓▓█
         ██▒                                                                                 ▒▓█
         ██▒                                                                                 ▒▓█
          ██▓▒                                                                                ▓▓█
           ██▓                                                                               ▒███
          ██▓                                                                               ▒███
           ██▓                                                                               ▒███
           ██▓                                                                             ▒██
            ██▓                                                                             ▒██
           ██▓                                                                             ▒██
            ██▓                                                                           ▓██
            ██▓                                                                           ▓██
            ██▓▒                                                                         ▒▓██
              █▓▒                                                                       ▒▓██
              █▓▒                                                                       ▒▓██
              █▓▒                                                                       ▒▓██
              ██▓▒                                                                     ▒▓██
              ███▒                                                                     ▒▓██
              █████████████████████████████████████████████████████████████████████████████ 
 """)#supposed to look like "UH-OH"
        time.sleep(.5)
        clearterm()
        print(f"Score: {score}")  
        time.sleep(.5)
    clearterm()

#recyleable quiz layout for all questions i'll build it soon.
orientation = ["A: ", "B: ", "C: ", "D: "]
question = "placeholder question" 
awncers = [""" """, """ """, """ """, """ """]
def quizlayout():
    print(f"Score: {score}")
    print(question)
    print(f"""
    {orientation[0]}{awncers[0]}
    {orientation[1]}{awncers[1]}
    {orientation[2]}{awncers[2]}
    {orientation[3]}{awncers[3]}
    """) 

#change questipon
question = """             
                             ##                                            
                           #@..@#                             
                         *@+.....@%                           
                        @@........=@+                         
                     *%@:....@@.....@@*:                      
                   @*@:......*%@@....:@=#.                    
                 @@*=.....=+@%**%@--....*+%                   
                 *@.....==@%#****#%@==...=+@#                 
               :@:+...++@%#********#%@*+...@#                 
               :@:..-@%%#************#%%@-.-:@:               
               :@:...@******@@@@@@@%**%@@*..:@-               
               :@:.@@@@%**%@@..@+.:@@@@#.#@.:=:               
               :@=@...#@@@@-.@@@@..........@+@=               
               :#:%.................@@.....%:%:               
                 +@@#.....@@.....@@@.....*@@*                 
     :*#@@@%*:     *@@......@@@@@..=....@@#                   
   :%@@.....@@     @@@@@..............@@@@@@@                 
   .@:...:...:@@ @@.....@@@@@@@@@@@@@@......:@@               
   @@@@@@@.....:@.........%:=-.....%..........:@@             
        -@:..........@@@@@@=.+#=:::*@@@@@.......@@            
          @@.::::..@#+:+=+.....*=+:::::.-@@.......@#          
            @@@@@@@-:=:*.........*:-::::..:@@.:....:@=        
                 -@.:+:...........-+::::::.@@@:.....@-%       
                 :@.:+::-+.:=-=...-+:::::..@- #@..*:.+@       
                 :@@@-=++*.-+++:=-:##@@@#@*%: .@+*...=@       
                 :@..@#=:+::=:-=%@@@.....@@     *@-*+=@       
                 :@...:@@@@#:............:.@@   %@==*         
                 :@.........@@@@@@.........::@.               
                 %@@@@...:@@      @@@@.....@@@@@@             
               #@:...@@@@@            @@@@@.....@@            
             %*:........@+             =@:........%.          
            #@=#@@@@@@@@                 #@@@@@@@%*:-:    

WHAT'S THE NAME OF THIS KID? SERIOUSLY I DON'T REMEMBER."""
#change the awncer here
awncers = ["""LANCER""", """DANCER""", """PRANCER""", """MR. GENEROSITY"""]

while True:
    quizlayout()
    ask_awncer = input("A, B, C, or D? ").upper()

    if ask_awncer == "A":
        tickanim()
        break
        clearterm()
    elif ask_awncer == "B":
        tickanim()
        break
        clearterm()
    elif ask_awncer == "C":
        tickanim()
        break
        clearterm()
    elif ask_awncer == "D":
        tickanim()
        break
        clearterm()
    else:
        print("Invalid choice.")
        time.sleep(.5)
        clearterm()

#quest2
question = """WHICH SHOW WAS ASGORE'S FAVORITE!?"""
#change the awncer here
awncers = ["""COOKING SHOW""", """NASTY MUSIC VIDEOS""", """MONSTER MOVIES""", """COWBOY SHOW"""]

while True:
    quizlayout()
    ask_awncer = input("A, B, C, or D? ").upper()

    if ask_awncer == "A":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "B":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "C":
        #tickanim()
        uhohanim()
        break
        clearterm()
    elif ask_awncer == "D":
        tickanim()
        #uhohanim()
        break
        clearterm()
    else:
        print("Invalid choice.")
        time.sleep(.5)
        clearterm()

#quest3
question = """
                            %%@@%                                 
                           %##%%@@@@@@@@@@@%                      
                           ###%@@@@@@@@@@@@@@@@    @@%            
                           %%%@@@@@@@@@@@@@@@@@@@@@%%%%#          
                       %@@@@@@@%@@@@@@@@@@@@@@@@@%#####%          
                      @@@@@@@@@@%%%@@@@@@@@%%@@@@@%####           
                    @@@@%@@@@@@@%%##%%%%%%%%%@@@@@@@%%            
                   @@@%%%@@@@%%%%@%%######%%@@@@@@@@@@@%          
                  @@%%#*%@@@##%*+%%%%%%%%%%%%%@@@@@@@@%@%         
                 @@%%###%%%#%%####%%%%%%%%%%#**#%%@@@%%%@%        
                @@@%####*#%%#-  *%##%%%%%%######*%%%%%#%@@#       
               %@@@%%##%%#%%*.  +%%**####%%+..*%%#%%%#*%@%%       
              %@@@%%%##%%#*#%=.-#%%*%%#*#%*.  +#%%*%*+*#%%%       
              %@%%%%#++%%%#*#%%%%#*%%%%##%+. -#%%%+++*#%%%%       
              #%%##+=--+#%%%%#*##%%%%%%%#*%%%#**##%%*#%%%%%       
              #%*+=-----=*#%%%**%%#%#*+%%###***#%%%#%%%%%%#       
                **--------=###%*++=*####*#%%%%%%%##%%%%%%%        
               +=-----------=######%%#*##%%%%%%*=*#%%%%%%*        
            +==----------------=*###########*----*###%%%*         
      *+=:.. :=---------------------------------++*####*          
     #+.     =----------------------------------.:++**            
  %@@@%+.   .=--------------------------------       .=           
 %@@@@%#-   -------------.:::--------------.          ..:=        
%@@@@@%%*. :------------::-.   .===--=+++++:             .:-      
%%%%%@@%#=.-------------:-:           :++++=.             ...:    
%%%%%%%%*=-------------:-=-           .=++++=.            .+%@%   
 ##%%%##*+--------------==+-.         :+++++=:::        .=%@@@@%  
    #+  *-------------:=++++=.      :++*++++++=+-.     .+%@@@@@@# 
        =-------------:=++++*+.  .=+****+++++++++ -.  .=#%%%%%%@%#
      #%%%@@%%+=-------=+++++*+=+***++****+++++++   :.:*##%%%%%%%#
     %%%%%%%%%%@%#++++++++++*+++++++++******++++++    -+###%%%%%# 
    #%%%%%%%%#%%%%%##**###*******++*********#####%%@@%@%# *##%#   
    *%%%%%%%%#%%%%%########################%%#%%%%%%%@@@@%*       
     #%%%#%##%%%%%%#*++*****#################%%%%%%%#%%%%@%#      
      #%%%%%%%%%%%#*        =+++*********####%%%%%%#%%%%%%%%      
       +#%%%%%%##*=                      +*##%%%%%##%%%#%%#*      
            *+=                            *##%%%%%%%#%%%#*       
                                             *###%%%%%%#*         
                                                +**#*+                                    
BRAND A VALUES THIS RALSEI AT $8! WHAT'S THE TRUE VALUE!?
"""
#change the awncer here
awncers = ["""HIGHER""", """LOWER""", """PRICELESS""", """$32.00 MSRP"""]

while True:
    quizlayout()
    ask_awncer = input("A, B, C, or D? ").upper()

    if ask_awncer == "A":
        #uhohanim()
        tickanim()
        break
        clearterm()
    elif ask_awncer == "B":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "C":
        #tickanim()
        uhohanim()
        break
        clearterm()
    elif ask_awncer == "D":
        tickanim()
        #uhohanim()
        break
        clearterm()
    else:
        print("Invalid choice.")
        time.sleep(.5)
        clearterm()


#quest4
question = """WHAT IS THE NAME OF THIS SHOW'S HOST?"""
#change the awncer here
awncers = ["""MR. TV GUY""", """MR. LIL' NOSE""", """MR. TENNA""", """MR. EMAIL"""]

while True:
    quizlayout()
    ask_awncer = input("A, B, C, or D? ").upper()

    if ask_awncer == "A":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "B":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "C":
        tickanim()
        #uhohanim()
        break
        clearterm()
    elif ask_awncer == "D":
        #tickanim()
        uhohanim()
        break
        clearterm()
    else:
        print("Invalid choice.")
        time.sleep(.5)
        clearterm()

#quest5
question = """WHAT IS THE HIGHLY MEMORABLE HEADING OF TV TIME?"""
#change the awncer here
awncers = ["""DON'T TOUCH THAT DIAL!""", """MARVELOUS MYSTERY BOARD""", """MAGICAL MYSTERY BOARD""", """DON'T LICK THE SCREEN!"""]

while True:
    quizlayout()
    ask_awncer = input("A, B, C, or D? ").upper()

    if ask_awncer == "A":
        uhohanim()
        #tickanim()
        break
        clearterm()
    elif ask_awncer == "B":
        #uhohanim()
        tickanim()
        break
        clearterm()
    elif ask_awncer == "C":
        #tickanim()
        uhohanim()
        break
        clearterm()
    elif ask_awncer == "D":
        #tickanim()
        uhohanim()
        break
        clearterm()
    else:
        print("Invalid choice.")
        time.sleep(.5)
        clearterm()

print(f"Final Score: {score}/5")
time.sleep(7)
exit()
#final note because why not. I now understand why linus torvold said git also got its name because he just wanted to get hit by a bus or somthing idk cool man don't remember the exact quote but hey heres to hope the project is done. 
#mfw i finaly complete this project: https://youtu.be/toTkY8g8Stg?t=68