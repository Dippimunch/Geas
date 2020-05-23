import math


day = 24
week = 168 
month = 720 #30 days
year = 8640 #360 days

clock = 7134

week_count = 0
month_count = 0
year_count = math.floor(clock / year)

if clock >= year:
    day_count = clock - (year * year_count)
else:
    day_count = math.floor(clock / day)
    

print("year: %i" % (year_count))
print("day : %i" % (day_count))
#print("hour: %i" % (hour_count))
