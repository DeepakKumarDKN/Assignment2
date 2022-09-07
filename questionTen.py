from datetime import datetime

dt = datetime.today()
print(dt)
print()

newDate = dt.strftime("%d %b %Y")
newDate22 =dt.strftime("%B %d %Y")
print(newDate)
print(newDate22)

newDate1 = dt.strftime("%d-%b-%Y")
print(newDate1)

newDate2 = dt.strftime("%d-%m-%Y and %H:%M %p")
newDate3 = dt.strftime("%d-%m-%Y and %I:%M %p")
print(newDate2)
print(newDate3)