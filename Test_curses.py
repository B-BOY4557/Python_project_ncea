import curses
from curses import wrapper

#init 
def main(stdscr): #this is the output to dispay to the terminal
    stdscr.clear() 
    stdscr.refresh() 
    

wrapper(main)
