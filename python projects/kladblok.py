import time

t = time.localtime()
current_time_hour = time.strftime("%H", t)
current_time_minute = time.strftime("%M", t)
print(current_time_hour)
print(current_time_minute)

            