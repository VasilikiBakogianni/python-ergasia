import datetime
def daTE(dTE):
    return "%02d/%02d/%4d" % (dTE.day, dTE.month, dTE.year)

# Encode the current weekday into number(Monday -->0...Sunday -->6)
today = datetime.date.today()
day = today.day
month = today.month
year = today.year
weekday = today.weekday()

#Shows day of week and full date
fullDay = datetime.date.today()
thisDay = datetime.datetime.now()
print 'Today it is:' ,thisDay.strftime("%A"),fullDay

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Check the remaining months of the current year
#Is the full date valid?
listOfDates= []
for x in range(month+1, 13):
    try:
        daTe = datetime.date(year, x, day)
        if daTe.weekday == weekday:
            listOfDates.append(daTe)
    except:
        continue    
    
# Same for the remaining ten years
for i in range(year+1, year+11):
    for j in range(1, 13):  
        try:
            daTe = datetime.date(i, j, day)
            if daTe.weekday() == weekday:
                listOfDates.append(daTe)
        except:
            continue
  
print('In the next ten years there will also be', len(listOfDates), "dates that their day will be", day, days[weekday]+"s!")