from datetime import datetime
time_now = datetime.now()

print("Good Morning! The current time is:", time_now.strftime("%H:%M"))

if time_now.hour < 12:
    print("Good Morning!")
elif 12 <= time_now.hour < 18:
    print("Good Afternoon!")
elif 18 <= time_now.hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")

