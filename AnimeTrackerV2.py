# simple python app to manage anime

import os
import re
import subprocess
import shelve

# todo: get a list of episodes
file = shelve.open("C:/users/dd/Documents/AnimeTracker/counter")
# counter = 0
# file["counter"] = counter
counter = file['counter']
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
play = subprocess.Popen([player, episode_path])

# todo: update episode in db
# counter += 1
# file['counter'] = counter
# todo: update anime dir after season is over



print(f"\nPlaying #{counter}: {Current_episode}")

file.close()
