import datetime
a = datetime.datetime.now()
a = str(a).split(' ')[1].split(':')
print(int(a[1]))
