"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max = 0
index = 0
for i in calls:
    if int(i[3]) > max:
        max = int(i[3])
        location = index
    index += 1
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(calls[location][0],calls[location][3]))