# phoneAndEmailExtractor.py -  Extracts phone numbers and email addresses copied to  the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())
phoneNumbers = [] #list to store phone numbers
emailAddresses= [] #list to store email addresses

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    phoneNumbers.append(phoneNum)

for groups in emailRegex.findall(text):
    emailAddresses.append(groups[0])

if len(phoneNumbers) > 0 or len(emailAddresses) > 0:
    if len(phoneNumbers) > 0:
        print('Extracted phone numbers are:')
        print('\n'.join(phoneNumbers))
        print()
    if len(phoneNumbers) > 0:
        print('Extracted email addresses are:')
        print('\n'.join(emailAddresses))
else:
    print('No phone numbers or email addresses found.')