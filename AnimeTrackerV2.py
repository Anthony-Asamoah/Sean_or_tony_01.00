# simple python app to manage anime

import os, re, shelve, sys
import subprocess

# todo: Set counter to specific number/episode
# counter = 14
# file["counter"] = counter

# todo: get a list of episodes
file = shelve.open("C:/users/dd/Documents/AnimeTracker/counter")
counter = file['counter']
counter = int(counter)
player = r"E:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
Directory = r"C:\Users\dd\Downloads\Video\Haikyuu S1"
Episode_list = os.listdir(Directory)

# todo: sort the list of episodes
episode_num = re.compile(r"\s\d+")
for i in range(len(Episode_list)):
	Episode_list[i] = episode_num.sub((" " + str(i)), Episode_list[i])

Current_episode = Episode_list[counter]
episode_path = os.path.join(Directory, Current_episode)

# todo: play anime
print(f"\nYou are currently on EP {counter}\n\nProceed to Play? ")


def startVLC():
	print(f"\nPlaying: {Current_episode}")
	vlc = subprocess.Popen([player, episode_path])
	return vlc


while True:
	play = input("reply with 'y' or 'n'.\n\t-> ")
	if not play or play.lower() == 'y':
		vlc = startVLC()
		# vlc.wait()
		break
	elif play.lower() == "n":
		print("\nSee you later...")
		sys.exit()
	else:
		print("invalid input!")
		continue

# todo: wait for show to finish then ask to play next
while True:
	counter += 1
	print(f"\\nPlay Episode {counter} next?")
	next = input("reply with 'y' or 'n'.\n\t-> ")
	while next.lower() not in ['n', 'y']:
		print("invalid Input!")
	if next == 'y':
		startVLC()
		# vlc.wait()
		continue
	else:
		print("\nSee you later...")
		break

# todo: update episode in db
file['counter'] = counter
file.close()

# todo: update anime dir after season is over
