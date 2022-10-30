# class note:
#     def __init__ (self, freq, amp):
#         self.freq = freq # index of the key with 0 <= freq <= 68
#         self.amp = amp # relative amplitude
# class timestamp:
#     def __init__ (self, )

# class performance:
#     def __init__ (self, length, notes):
#         self.length = length # number of time periods
#         self.timestamps = timestamps # time indexed array
#         self.range = 69 # number of keys played
# We really don't need those LMAO I was on vicodin

# Most operations done on the data are in-place and destructive

def parse_input(filename):
    #parses the input file into a 2D list
    file = open(filename, "r")
    data = []
    for line in file:
        temp = [entry.rstrip() for entry in line.split()]
        data.append(temp)
    return data

def find_max_amp(performance_data):
    # a lot of loops but only run once
    curr_max = -5
    for time in performance_data:
        for item in time:
            if item > curr_max: curr_max = item
    return curr_max

def digitize(performance_data, max_amp):
    # a lot of loops but only run once
    ratio = max_volume/5
    for time in performance_data:
        time //= ratio


def separate_syllables (note0, note1, max_volume = 5):
    #determines whether the key needs to be replayed
    #potential to improve this with ML
    difference = 2 # tweak with this param; must not exceed max_volume
    return (note1 if (abs(note0 - note1) > difference) else 0)

# much opportunity to optimize if we need to use C or other lower level
language
def data_to_performance (data):
    for time in range(len(data)):
        for i in range(69):
            note0 = data[time-1][i]
            note1 = data[time][i]
            note1 = separate_syllables(note0, note1)
    return data


def main():
    input_file = sys.argv[1]
    data = parse_input(input_file)
    max_map = find_max_amp(data)
    digitize(data, max_amp)
    data_to_performance(data)
    

if __name__ == "__main__":
    main()




