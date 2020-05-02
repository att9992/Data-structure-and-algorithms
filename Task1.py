"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
check_list=set()
for i in texts:
    check_list.add(i[0])
    check_list.add(i[1])
for j in calls:
    check_list.add(j[0])
    check_list.add(j[1])
print(f'There are {len(check_list)} different telephone numbers in the records.')