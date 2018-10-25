from datetime import date, datetime

class Subject(object):
	def __init__(self,name,location,start,end):
		self.name = name
		self.location = location
		self.start = start
		self.end = end

def getPeriods(day, time, schedList):
	curDay = schedList[day]
	hour = int(time[:2])
	minute = int(time[3:])
	currentPeriod = None

	#get period
	if hour < int(curDay[0].start[:2]):
		nextPeriod = curDay[0]
		followingPeriod = curDay[1]

	else:
		for period in curDay:
			startHour = int(period.start[:2])
			startMinute = int(period.start[3:])
			endHour = int(period.end[:2])
			endMinute = int(period.end[3:])

			if hour == startHour and minute >= startMinute:
				currentPeriod = period

				try:
					nextPeriod = curDay[curDay.index(period) + 1]
				except:
					nextPeriod = None

				try:
					followingPeriod = curDay[curDay.index(period) + 2]
				except:
					followingPeriod = None

				break

			elif hour == endHour and minute <= endMinute:
				currentPeriod = period

				try:
					nextPeriod = curDay[curDay.index(period) + 1]
				except:
					nextPeriod = None

				try:
					followingPeriod = curDay[curDay.index(period) + 2]
				except:
					followingPeriod = None

					break


	#printing and formatting
	def format(time):
			hour = int(time[:2])

			if hour > 12:
				hour = str(hour-12)
				return hour + time[2:] + "pm"
			elif hour == 12:
				return time + "pm"
			else:
				return time + "am"

	if currentPeriod == None:
		try:
			for period in curDay:
				if int(period.start[:2]) > hour:
					nextPeriod = period
					followingPeriod = curDay[curDay.index(period) + 1]
					break

		except:
			None

	try:
		text = "CURRENT PERIOD: %s | %s\nDURATION: %s-%s\n\n"%(currentPeriod.name,currentPeriod.location,format(currentPeriod.start),format(currentPeriod.end))
	except:
		text = "CURRENT PERIOD: none\n\n"
	try:
		text += "NEXT PERIOD: %s | %s\nDURATION: %s-%s\n\n"%(nextPeriod.name,nextPeriod.location,format(nextPeriod.start),format(nextPeriod.end))
	except:
		text += "NEXT PERIOD: none\n\n"
	try:
		text += "FOLLOWING PERIOD: %s | %s\nDURATION: %s-%s"%(followingPeriod.name,followingPeriod.location,format(followingPeriod.start),format(followingPeriod.end))
	except:
		text += "FOLLOWING PERIOD: none"

	return text

def main():
	currentDate = date.today()

	day = currentDate.weekday()

	hour = str(datetime.now().hour)
	minute = str(datetime.now().minute)

	if len(hour) == 1:
		hour = "0" + str(hour)
	if len(minute) == 1:
		minute = "0" + str(minute)

	time = hour + ":" + minute


	#Create Subjects (Name, Location, Start Time, End Time)
	calcI = Subject("Honors Calculus I", "231 Hayes Healy Center", "11:30", "12:20")
	calcITut = Subject("Honors Calculus I Tutorial", "114 O'Shaugnessy Hall", "15:30", "16:20")
	artHist = Subject("Art History Usem", "215 Riley Hall", "11:00", "12:15")
	chem = Subject("Chemistry", "101 Jordan Hall of Science", "09:25", "10:15")
	chemLab = Subject("Chemistry Lab", "302 Jordan Hall of Science", "15:30", "18:15")
	chemTut = Subject("Chemistry Tut", "217 DeBartolo Hall", "14:00", "14:50")
	eng = Subject("Engineering Systems I", "110 Stinson Remick Hall", "14:00", "15:15")
	theo = Subject("Theology", "240 DeBartolo Hall", "10:30", "11:20")
	moreauFYE = Subject("Moreau First Year Experience", "201 O'Shaugnessy Hall", "14:00", "14:50")


	schedList = [[chem,theo,calcI,moreauFYE], #Monday
							 [artHist,eng,chemLab], #Tuesday
							 [chem,theo,calcI], #Wednesday
							 [artHist,eng,calcITut], #Thursday
							 [chem,theo,calcI,chemTut]] #Friday

	text = "\n"+ getPeriods(day,time,schedList)


	print(text)

if __name__ == "__main__":
	main()
