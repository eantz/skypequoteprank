import time, win32clipboard
from datetime import datetime

message = raw_input("your message : ")
author = raw_input("author : ")
date = raw_input("date : ")

date_epoch = 0

if date == "":
	now = datetime.now()
	date_epoch = time.mktime(now.timetuple())
else :
	date_epoch = time.mktime(datetime.strptime(date, '%d%m%Y %H%M').timetuple())

quote = '<quote author="%s" timestamp="%d">%s</quote>' % (author, date_epoch, message)

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardData(1,quote)
win32clipboard.SetClipboardData(7,quote)
win32clipboard.SetClipboardData(win32clipboard.RegisterClipboardFormat("skypeMessageFragment"),quote)
win32clipboard.CloseClipboard()
