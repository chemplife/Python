'''
Given 2 calendars of a day for 2 people, with booked timeslots.
Find all timeslots for which both people are available to have the meeting during their working time.
Time format: Military

Sample Input:
cal1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
work_day1 = ['9:00', '20:00']
cal2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
work_day2 = ['10:00', '18:30']
meeting_duration = 30

Sample Output:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
'''

'''
My Solution
Assuming all calendar timeslots are in ascending order and within the work_day of respective person.
Time is in String format

1. Find a duration that works for both the people.
workable_Time = ['10:00', '18:30']
	-> compare work_day1[0]: work_day2[0] -> Greater time-> workable_time[0]
	-> compare work_day1[1]: work_day2[1] -> Greater time-> workable_time[1]

2. Check the blocked times for both people during the workable_time
-> booked = [['10:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00'],\
			['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]

	slots =	[[['10:00', '10:30'], ['10:00', '11:30']], [['12:00', '13:00']],\
			[['12:30', '14:30']], [['14:30', '15:00']], [['16:00', '17:00'], ['16:00', '18:00']]]

3. Pick the biggest val[1] in list of element 0 [s], and the smallest val[0] in list of element 1 [t]; if s>=t: move on to the next list of element
	Biggest val[1] in list of element 1, and the smallest val[0] in list of element 2; if s>=t: move on to the next list of element (yields 0 slots)
	Biggest val[1] in list of element 2, and the smallest val[0] in list of element 3; if s>=t: move on to the next list of element (yields 0 slots)
	Biggest val[1] in list of element 3, and the smallest val[0] in list of element 4; if s>=t: move on to the next list of element (yields 0 slots)
	Biggest val[1] in list of element 4, and workable_time[1]; if s>=t: move on to the next list of element (yields 0 slots)
	[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
'''

def compare_time(time1, time2):
	t1 = [int(t) for t in time1.split(':')]
	# t1 = [9, 0]
	t2 = [int(t) for t in time2.split(':')]
	# t2 = [10, 0]
	t_1 = t1[0]*60 + t1[1]
	t_2 = t2[0]*60 + t2[1]

	if t_1 > t_2:
		return 1
	elif t_1 < t_2:
		return -1
	else:
		return 0

def find_slots(cal1, cal2, workable_time):
	booked = []
	slots = []
	cals = [cal1, cal2]
	for cal in cals:
		count = 0
		for slot in len(cal):
			if count = 0:
				r_0 = compare_time(workable_time[0], slot[0])
				r_1 = compare_time(workable_time[0], slot[1])
				if len(booked) == 0:
					booked[count][0] = workable_time[0] if r_0 >= 0 else slot[0]
					booked[count][1] = workable_time[1] if r_1 >= 0 else slot[1]
				else:
					booked[len(booked)][0] = workable_time[0] if r_0 >= 0 else slot[0]
					booked[len(booked)][1] = workable_time[1] if r_1 >= 0 else slot[1]	#5:33
			else:
				r_0 = compare_time(workable_time[1], slot[0])
				r_1 = compare_time(workable_time[1], slot[1])
				if r_0 < 0 or r_1 < 0:
					break
				booked[count][0] = slot[0]
				booked[count][1] = slot[1]
				if r_1 == 0:
					break
			count += 1
	# booked = [['10:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00'],\
	#		['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]

	# Rearrage on the basis of ele[0]
	# [['10:00', '10:30'], ['10:00', '11:30'], ['12:00', '13:00'], ['12:30', '14:30'], ]	#5:44

	for slot in booked:


	#slots =	[[['10:00', '10:30'], ['10:00', '11:30']], [['12:00', '13:00']],\
	#		[['12:30', '14:30']], [['14:30', '15:00']], [['16:00', '17:00'], ['16:00', '18:00']]]

if __name__ == "__main__":
	cal1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
	work_day1 = ['9:00', '20:00']
	cal2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
	work_day2 = ['10:00', '18:30']
	meeting_duration = 30

	workable_time = []
	for i in len(work_day1):
		result = compare_time(work_day1[i], work_day2[i])
		if result >= 0:
			workable_time[i] = work_day1[i]
		else:
			workable_time[i] = work_day2[i]
	# workable_Time = ['10:00', '18:30']
	find_slots(cal1, cal2, workable_time)