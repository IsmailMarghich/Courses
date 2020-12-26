#Give N number of activities with their start and end times, 
# we need to select the maximum number of activities that can be performed by a single person
# assuming that a person can only work on a single activity at a time

#sort activities based on finish time
#select first activity from sorted array
#for all remaining activities:
#if the start of tthis activity is greater or equal to the finish of previous selected activity
#select this activity and print it
activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
              ]


def printMaxActivities(activities):
    activities.sort(key=lambda x: x[2]) #lambda function to sort list by second index (end time)
    i = 0 #index starts at 0
    first = activities[i][0] #grab first activity and print
    print(first)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]: #check if next activity start time is greater than first activity end time
            print(activities[j][0]) #then print the activity
            i = j #we take our new activity as current activity
#sorting a 2d array is O(NlogN) time complexity and space complexity is O(1) because no extra memory is required 
printMaxActivities(activities)