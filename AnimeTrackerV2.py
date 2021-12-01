# simple python app to manage anime

from datetime import datetime
import os

CurrEpp = 17
file = 'Watch Baby Steps 2nd Season Episode ' + str(CurrEpp) + '.mp4'

# Location of the anime to be viewed must be updated after each season!
# ----------------------------------------------------
os.chdir("C:\\Users\\dd\\Videos\\Baby Steps\\Season 2")
# ----------------------------------------------------

# This shows the episode & show that is going to be played,
# remember to update after each episode!!!

time = datetime.now()
print(time.strftime('%c'))

print('\nCurrent Anime: Baby Steps',
	  "\n-------------------------\n",
	  'Current Episode: ',
	  CurrEpp,
	  "\n-------------------------\n")

print('hit enter to continue')
pause = input()
# !!!!!!!!!!Next Episode:  !!!!!!!!!!!!!!!!!

# The launch function of this program, also remember to update!!!!!!
# TODO : include code to launch the anime directory
# TODO : include code to launch the anime tracker in vs code or any text editor.
# @notepad.exe .\\Anime_Tracker.bat %
# ================================================
os.execvp(file, )
# ================================================

++CurrEpp
