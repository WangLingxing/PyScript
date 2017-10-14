#/usr/bin/python3
#拷贝对应名称的数据到粘贴板

WORDS = {'email': 'EmailPassWord',
         'blog': 'BlogPassword',
         'Love you':'Soso'}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: py wordsCopy.py [KeyWords] - copy the content to clipboard use keywords')
    sys.exit()

keywords = sys.argv[1]

if keywords in WORDS:
    pyperclip.copy(WORDS[keywords])
    print('Password for ' + keywords + ' copied to clipboard.')
else:
    print('There is no keywords named ' + keywords)
