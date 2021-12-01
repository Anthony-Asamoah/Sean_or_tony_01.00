# pw.py - an insecure password locker.

library = {
    'gmail' : 'xyzxyzxyz123',
    'yahoo' : 'abcabcabc456',
    'hotmail' : '987050toto'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in library:
    pyperclip.copy(library[account])
    print('Password for', account, 'copied to clipboard.', sep=' ')

else:
    print('No account found with name: ', account)
