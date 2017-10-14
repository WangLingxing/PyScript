#!/usr/bin/python3
# 添加无序列表前面的标记，拷贝段落后，运行，结果在粘贴板中

import pyperclip
text = pyperclip.paste()

# 按照换行符分割,添加星标
lines = text.split('\n')
for i  in range(len(lines)):
    lines[i] = '* ' + (lines[i]).strip()

text = '\n'.join(lines)

pyperclip.copy(text)



