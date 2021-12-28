# simple python app to keep track of anime(or series)
# ##############################################################################################
# to make this work, label the anime you want to track with "[Live]" and the program will
# take care of the rest

import os, re, shelve, sys
import subprocess, pprint

player = r"E:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
MainDir = r"C:\Users\dd\downloads\Video"

# todo: get current anime with regex
AllFiles = os.listdir(MainDir)
liveanime = re.compile(r'\[LIVE\]', re.IGNORECASE)


def liveFinder():
	for i in AllFiles:
		found = liveanime.findall(i)
		if found:
			return i
		else:
			found = False

Active = liveFinder()
try:
	Directory = os.path.join(MainDir, Active)
except TypeError:
	print('\nError!!!\nNo anime/series/shows beign tracked!\n\n',
	'Add "[Live]" to the anime folder you want to track then launch AnimeTracker V2\n')
	sys.exit()

# get a list of episodes
file = shelve.open("C:/users/dd/Documents/AnimeTracker/counter")
counter = file['counter']
Episode_list = os.listdir(Directory)

# Set counter to specific number/episode
# counter = 5
# file["counter"] = counter


# sort the list of episodes
episode_num = re.compile(r"\s\d+")
for i in range(1, len(Episode_list) ):
	Episode_list[i] = episode_num.sub((" " + str(i)), Episode_list[i])

# play anime
def startVLC():
	Current_episode = Episode_list[counter]
	episode_path = os.path.join(Directory, Current_episode)
	print(f"\nPlaying: {Current_episode}")
	vlc = subprocess.Popen([player, episode_path])
	return vlc
	
if counter - len(Episode_list) == 0:
	print("\nYou are currently on the last episode! Play?")
else:
	print(f"\n--> {len(Episode_list) - counter} Episodes left")
	print(f"You are currently on EP {counter}\n\nProceed to Play? ")
while True:
	play = input("reply with 'y' or 'n'.\n\t-> ")
	if not play or play.lower() == 'y':
		vlc = startVLC()
		vlc.wait()
		counter += 1
		break
	elif play.lower() == "n":
		print("\nSee you later...")
		sys.exit()
	else:
		print("invalid input!")
		continue

# case with no more episodes
if counter > len(Episode_list):
	print('You have finished the Season.\n',
	'Remember to track a new season/show. Thank you.')
	rename = liveanime.sub("", Directory)

# wait for show to finish then ask to play next
while True:
	print(f"\n\nPlay Episode {counter} next?")
	next = input("reply with 'y' or 'n'.\n\t-> ")
	if not next or next.lower() == 'y':
		vlc = startVLC()
		vlc.wait()
		counter += 1
		continue
	elif next.lower() == 'n':
		print("\nSee you later...")
		break
	else:
		print("invalid Input!")
		continue

# update episode in db
file['counter'] = counter
file.close()

# todo: update anime dir after season is over
# todo: make a better sorter
	# sorter that first renames all episodes to the same name but diff ep#
'''
def Pruner(ep):	
	EpPrume = re.compile(r'\d+|{\d}2')
	EpSuffix = re.compile(r'\.\w+')
	EpInsert = re.compile(r".*ep", re.IGNORECASE)	
	for i in range(len(ep)):
		try:
			new_name = EpInsert.findall(ep[i])
		except IndexError:
			continue

	for i in range(len(ep)):
		ep_num = EpPrume.search(ep[i])
		ep_suffix = EpSuffix.search(ep[i])
		ep[i] = f"{new_name[0]} {int(ep_num.group())}{str(ep_suffix.group())}"
	
	return ep
'''
# so far, pruner works but needs work on identifying ep num