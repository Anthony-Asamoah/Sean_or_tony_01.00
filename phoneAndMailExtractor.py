#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re
from datetime import datetime

#Phone Number Regex.
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\)) # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.)? # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# Email regex.
emailRegex = re.compile(r'''
(\S+) # local part
(@\S+)  # domain
''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matchedEmails = emailRegex.findall(text)
matchedPhoneNums = phoneRegex.findall(text)

# Arrange and format emails and numbers as a string
dateobject = datetime.now()
date = dateobject.strftime('%c')

All_Info = f'{date}'

emails = ""
for i in range(len(matchedEmails)):
	emails += "".join(matchedEmails[i]) + "\n"
if len(emails) < 1:
	print("No emails found")

phoneNumbers = ''
for i in range(len(matchedPhoneNums)):
	phoneNumbers += str(matchedPhoneNums[i][0]) + "\n"
if len(phoneNumbers) < 1:
	print("No Phone Numbers found")

if len(phoneNumbers) or len(emails) > 0:
	# join emails and phone numbers into one string
	if len(phoneNumbers) > 0:
		All_Info += "\n\n" + " Phone Numbers ".center(50, '=') + "\n" + phoneNumbers

	if len(emails) > 0:
		All_Info += "\n\n" + " Emails ".center(50, "=") + "\n" + emails

	# Copy results to the clipboard if numbers or emails were found.
	pyperclip.copy(All_Info)

	#print emails
	print("\n", All_Info)

else:
	print('Nothing to copy; Operation aborted!')