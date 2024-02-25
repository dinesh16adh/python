import datetime

current = datetime.datetime.now()
hours = current.hour
print(hours)
if hours >= 0 and hours < 12:
    print("good morning")
elif hours >= 12 and hours < 16:
    print("good afternoon")
else:
    print("good night")
