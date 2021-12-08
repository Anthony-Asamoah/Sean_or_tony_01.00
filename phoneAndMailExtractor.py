#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

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
emails = ""
for i in range(len(matchedEmails)):
	emails += "".join(matchedEmails[i]) + "\n"

phoneNumbers = ''
for i in range(len(matchedPhoneNums)):
	phoneNumbers += str(matchedPhoneNums[i][0]) + "\n"

# join emails and phone numbers into one string
All_Info = " Emails ".center(50, "=") + "\n" + emails \
		   + "\n\n" + " Phone Numbers ".center(50, '=') + "\n" + phoneNumbers

# Copy results to the clipboard.
pyperclip.copy(All_Info)

#print emails
print(All_Info)
