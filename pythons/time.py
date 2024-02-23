import datetime
current = datetime.datetime.now()
print(current)

hours = current.hour
print(hours)
if(hours<12):
    print("goodmorning")
elif(hours<16):
    print(" goodafternoon")

else:
    print("goodnight")