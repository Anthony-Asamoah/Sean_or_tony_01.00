# A simple program to select a meal based on the time of day

from random import randint
from datetime import datetime

hour = datetime.now().hour  # Create a datetime object to get the hour of day

# Dictionary to hold meals and their times
MainMenu = {
	"Breakfast": ['Bread & Egg', 'Kooko', 'Waakye','Jollof','Waakye & Jollof'],
	"Brunch": ['Waakye','Jollof', 'G)b3', 'Koliko','Waakye & Jollof'],
	"Lunch": ['Waakye','Jollof','Waakye & Jollof', 'G)b3', 'Koliko','Pork and Fries', 'Banku', 'Fufu'],
	"Dinner": ['Indomie', 'Fried Rice', 'Assorted Fried Rice', 'Kenkey', 'Jollof','Waakye/Jollof', 'Waakye', 'Banku', 'Fries', ],
	"Extra": ['Bread & Egg', 'Indomie', 'Tea'],
}
Fancy =['Pizza', 'Burgers', 'Ice Cream', 'Pie', 'Spring Rolls', 'Pastries', 'Cake']

# List to get meals per time of day
available = []
if hour in range(6, 10):
	mealtime = 'Breakfast'
	available += MainMenu.get(mealtime)
elif hour in range(10, 13):
	mealtime = 'Brunch'
	available += MainMenu.get(mealtime)
elif hour in range(13, 18):
	mealtime = 'Lunch'
	available += MainMenu.get(mealtime)
elif hour in range(18, 21):
	mealtime = 'Dinner'
	available += MainMenu.get(mealtime)
elif hour in range(21, 24):
	mealtime = 'Extra'
	available += MainMenu.get(mealtime)
else:
	mealtime = 'Fasting!'
	available.append(mealtime)

# Variable to store suggested meal
suggestion1 = available[randint(0, len(available) - 1)]
suggestion2 = available[randint(0, len(available) - 1)]
# To ensure both suggestions are not the same
while suggestion2 == suggestion1:
	suggestion2 = available[randint(0, len(available) - 1)]

# variable to hold the output statement, this is just for a custon pretty printing
sentence = f'It\'s time for {mealtime.lower()}. Thus, i suggest {suggestion1.capitalize()}, or some {suggestion2.capitalize()}.\nOtherwise; {Fancy[randint(0, len(Fancy) - 1)]}'

# Give output
print(
	'\n',
	' Something to eat? '.center(len(sentence), '/'),
	f'\n\n{sentence}',
	f'\n', ''.center(len(sentence), '_')
	)
