time=int(input("enter the time:"))
if(time>=6 and time<=12):
    print("Good Morning")
elif(time>=13 and time<=15):
    print("Good Afternoon")
elif(time>=16 and time<=20):
    print("Good evening")
else:
    print("Good night")