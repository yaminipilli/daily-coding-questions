"""Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2"""


def minimum_rooms(intervals):
    starting_times, ending_times = [], []

    starting_times = [i[0] for i in intervals]
    ending_times = [i[1] for i in intervals]

    starting_times.sort()
    ending_times.sort()

    starting_index = ending_index =  0
    max_rooms = current_rooms = 0

    while starting_index < len(starting_times) and ending_index < len(ending_times):
        
        if starting_times[starting_index] < ending_times[ending_index]:
            current_rooms += 1
            starting_index += 1
        else:
            current_rooms -= 1
            ending_index += 1
        
        max_rooms = (current_rooms)

    return max_rooms


intervals= [(30, 75), (0, 50), (60, 150)]
print(minimum_rooms(intervals))




