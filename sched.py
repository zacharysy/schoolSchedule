from datetime import date, datetime
import ui, appex, json, console

def getSchoolDay(schoolDay, refPoint, currentDate):
	#Number of days between days
	totalDays = (currentDate - refPoint).days 

	#How Many Days after one week
	remaining = totalDays % 7

	#Get the number of weekdays by getting the number of weeks and multiplying it by five and then adding the remaining days
	totalWeekdays = 5*((totalDays-remaining)/7) + remaining

	#Get the number of school days
	days = (totalWeekdays + schoolDay)%7

	if days == 0:
		days = 7
	
	return int(days)
	
def weekPeriod():
	day = date.today().weekday()
	period = []
	if day == 0:
		period.append("Mentoring")
		period.append("Rm S306")
	
	elif day == 1:
		period.append("PE")
		period.append("Tennis Court")
	
			
	elif day == 2:
		period.append("TOK")
		period.append("Rm S304")
		
	elif day == 3:
		period.append("CAS/EE")
		period.append("Rm S306")
		
	elif day == 4:
		period.append("ECA")
		period.append("wherever")

		
	else:
		return None
		
	period.append("15:00")
	period.append("16:00")
		
	return period
		
		
def getPeriods(day, time):
	#get file
	file = open("SchedList.json", "r")
	schedList = json.loads(file.read())
	file.close()
	
	curDay = schedList[str(day)]
	hour = time[:2]
	minute = time[3:]

	#get period
	if int(hour) >= 15 and int(hour) < 16:
		currentPeriod = weekPeriod()


	elif int(hour) < 7:
		nextPeriod = curDay["0"]
		followingPeriod = curDay["1"]
		
	else:
		for period in range(len(curDay)-1,-1,-1):
			period = str(period)

			startHour = curDay[period][2][:2]
			startMinute = curDay[period][2][3:]
			endHour = curDay[period][3][:2]
			endMinute = curDay[period][3][3:]

			if hour == startHour:
				if minute >= startMinute:  
					currentPeriod = curDay[period]
				
					try:
						nextPeriod = curDay[str(int(period)+1)]
					except:
						nextPeriod = weekPeriod()
					
					try:
						followingPeriod = curDay[str(int(period)+2)]
					except:
						if int(period) != len(curDay)-1:
							followingPeriod = weekPeriod()
							
					break
					
			elif hour == endHour:
				if minute <= endMinute:
					currentPeriod = curDay[period]
					
					try:
						nextPeriod = curDay[str(int(period)+1)]
					except:
						nextPeriod = weekPeriod()
						
					try:
						followingPeriod = curDay[str(int(period)+2)]
					except:
						followingPeriod = weekPeriod()
					break		
				

	#printing and formatting
	def format(time):
			hour = time[:2]
		
			if int(hour) > 12:
				hour = str(int(hour)-12)		
				return hour + time[2:] + "pm"		
			elif int(hour) == 12:
				return time + "pm"
			else:
				return time + "am"
	
	try:
		text = "CURRENT PERIOD: %s (%s)\nDURATION: %s-%s\n\n"%(currentPeriod[0],currentPeriod[1],format(currentPeriod[2]),format(currentPeriod[3]))
	except:
		text = "CURRENT PERIOD: none\n\n"
	try:
		text += "NEXT PERIOD: %s (%s)\nDURATION: %s-%s\n\n"%(nextPeriod[0],nextPeriod[1],format(nextPeriod[2]),format(nextPeriod[3]))
	except:
		text += "NEXT PERIOD: none\n\n"
	try:
		text += "FOLLOWING PERIOD: %s (%s)\nDURATION: %s-%s"%(followingPeriod[0],followingPeriod[1],format(followingPeriod[2]),format(followingPeriod[3]))
	except:
		text += "FOLLOWING PERIOD: none"
	
	return text

def make_widget_view():
	v = ui.View()
	label = ui.Label()
	label.name = 'label'
	v.add_subview(label)

	return v
	
def main():
	#Point of Reference (Only works when set on a monday or else it will mess up everything because it will mess up the remaining)
	year, month, day = 2016, 6, 6
	schoolDay = 4 % 7

	defaultDate = date(year, month, day)
	currentDate = date.today()
	
	day = getSchoolDay(schoolDay, defaultDate, currentDate)

	hour = str(datetime.now().hour)
	minute = str(datetime.now().minute)
	
	if len(hour) == 1:
		hour = "0" + str(hour)
	if len(minute) == 1:
		minute = "0" + str(minute)

	time = hour + ":" + minute
	
	text = "CURRENT DAY: Day " + str(day) + "\n"
	text += getPeriods(day,time)
	
	try:
		console.alert(text[:19] + "\n" + text[19:])
	except:
		print(text)

if __name__ == "__main__":
	main()

	
