import pychart
import math
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
    # a lot of loops but it's only run once
    curr_max = -5
    for time in performance_data:
        for item in time:
            if item > curr_max: curr_max = item
    return curr_max


#DO NOT USE ONLY 5 LEVELS
#CAN USE RANGE OF PMW
def digitize(performance_data, max_amp):
    # a lot of loops but it's only run once
    ratio = max_volume/5
    for time in performance_data:
        time //= ratio

# Force/power - linear
# dB to power - logarithmic
# power*=10 as dB+=10
# PWM granularity: 100???
# make parametre for this
#

#PWM: 100% = 25N
# 50% = 12.5N
# Lowest = 20% = 5N

#20 thru 88

def get_pwm_from_amplitude(amp):
    #
    
#need functions for 
#tracking how long a note has been playing 
#whether the note has gotten too quiet

def track_note_length (hold_arr, curr_index, )

def estimate_volume(hold_arr, og_vol, key_index, fade_param = -0.2):
    note_length = hold_arr[key_index]
    curr_vol = math.e**(og_vol*fade_param)

def separate_syllables (note0, note1, max_volume = 5):
    #determines whether the key needs to be replayed
    #potential to improve this with ML
    # difference = 2 # tweak with this param; must not exceed max_volume
    return (note1 if (abs(note0 - note1) > difference) else 0)

# much opportunity to optimize if we need to use C or other lower level
language
def data_to_performance (data, performance, hold_arr, initial_volumes):
    # first time stamp
    performance[0] = data[0]
    i = 0
    #set flags in hold array and set initial volumes
    for key in performance[0]:
        if key:
            hold_arr[i]+=1
            initial_volumes[i] = key
        i+=1

    # get projected volumes for each key and compare to speech volume
    for time in range(len(data)):
        for key_index in range(1, 69):
            prev_vol = data[time-1][key_index]
            curr_vol = data[time][key_index]
            # note1 = separate_syllables(note0, note1)
            estimated_vol = estimate_volume(hold_arr, initial_volumes, key_index)
            if estimated_vol:
            #key has not finished decaying
                if !curr_vol:
                    # no sound
                    if hold_arr[key] != 0:
                        #LIFT
                        #currently playing
                        performance[time][key] = -1
                        hold_arr[key] = 0
                    else if hold_arr[key] == 0:
                        #STAY UNPRESSED
                        #not currently playing
                        performance[time][key] = 0 

                if curr_vol:
                    # has sound
                    if estimated_vol < curr_vol:
                        #RE-PRESS
                        # not loud enough, need repress
                        performance[time][key] = curr_vol
                        hold_arr[key] = 1
                    
                    else if estimated_vol >= curr_vol:
                        #keep
                        #STAY PRESSED
                        performance[time][key] = 0
                        hold_arr[key]++
    return performance

#TODO & to test
#multidimensional distance
#total amplitude summation (try different averages)
#number of total keys changed

def init(input_file):
    # global hold_arr
    hold_arr = [0] * 69

    # global initial_volumes
    initial_volumes = [0] * 69

   

    # global data
    data = parse_input(input_file)

    max_map = find_max_amp(data)
    speech_time = len(data)

    # global performance
    performance = [[0] * 69 for i in range(speech_time)]

    
    initial_volumes = data[0]
    # digitize(data, max_amp)
    performance = data_to_performance(data)

    outfile = open("output.txt", "w+")
    outfile.write(performance)
    outfile.close

def main():
     input_file = sys.argv[1] #cmd line input
     init(input_file)
     return 0

if __name__ == "__main__":
    main()


