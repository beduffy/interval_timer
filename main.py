import sys
import os
import time

def say_something(something):
    cmd = 'espeak "{}"'.format(something)
    print(cmd)
    os.system(cmd)

# say_something('hey dan how is your day going')

num_exercises = 5
num_sets = 3
amount_of_time_pre_stretch = 20
amount_of_time_stretch = 30
amount_of_time_rest = 60 + 10
amount_of_time_rest = 60

# subtracting final rest
total_time_minutes = (5 * 3 * (amount_of_time_pre_stretch + amount_of_time_stretch + amount_of_time_rest) - amount_of_time_rest) / 60.0
print('Total time: {}'.format(total_time_minutes))

# sys.exit()
exercise_names = ['bridge', 'middle splits', 'front splits left', 'front splits right', 'pancake']

say_something('Starting in 10 seconds')
# time.sleep(10)
# TODO print beep countdown

for set_num in range(1, num_sets + 1):
    for exercise_num in range(1, num_exercises + 1):
        say_something('Exercise number {}... {} set number {}. Start pre stretch'.format(exercise_num, exercise_names[exercise_num], set_num))
        time.sleep(amount_of_time_pre_stretch)
        say_something('Stretch {} seconds'.format(amount_of_time_stretch))
        time.sleep(amount_of_time_stretch)

        if exercise_num == num_exercises and set_num == num_sets: 
            break
        say_something('Rest {} seconds'.format(amount_of_time_rest))
        time.sleep(amount_of_time_rest)

say_something('We are done. Finito')