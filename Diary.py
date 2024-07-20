import os
import datetime

path = os.getcwd() + r'\My_Diary'

def create_file(num):
    entry = f'\\Entry {num}.txt'
    file_path = path + entry
    with open(file_path, 'w') as file:
        print('Type your entry now: \n')
        writing = input()
        lines = [str(datetime.date.today()), writing]
        file.write(f'Today\'s Date: {datetime.date.today()}\n\nDear Diary, \n\t{writing}')


print('Welcome to your Diary!\n')
if os.path.exists(path):
    print('Acessing your Diary Folder...')
else:
    os.mkdir(path)
    print('Diary Folder Created!')


file_list = os.listdir(path)
if len(file_list) == 0:
    create_file(1)
else:
    lastentry = file_list[len(file_list) - 1]
    if lastentry[7:9].isdigit():
        create_file(int(lastentry[6:9]) + 1)
    elif lastentry[7:8].isdigit():
        create_file(int(lastentry[6:8]) + 1)
    else: 
        create_file(int(lastentry[6:7]) + 1)
