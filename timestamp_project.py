import time
timestamp=int(time.strftime('%H'))
print("Your time is:",timestamp,"'Clock")
if(timestamp > 12 and timestamp < 16):
     print("Good afternoon")
elif(timestamp > 17 and timestamp < 24):
     print("Good evening")
elif(timestamp < 12):
     print("Good morning")
elif(timestamp == 24):
     print("Good morning")