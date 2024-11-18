from datetime import datetime
import pytz     #   pip install pytz

moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
a = str(moscow_time).split()[1].split('.')[0].split(':')


print(a)