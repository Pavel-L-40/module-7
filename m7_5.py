import os
import time

directory = os.getcwd()

for i in os.walk(directory):
    print(i)

file_path = os.path.join('m7_1.py')

file_time = os.path.getatime('m7_1.py')
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
print(formatted_time)

file_size = os.path.getsize('m7_1.py')
print(file_size)

print(os.path.dirname(directory))
