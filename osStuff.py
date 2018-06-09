import os

from datetime import datetime


# Makes directory but can't make parents if they don't exist
# os.mkdir('newDir')

# Remove directory but can't make parents if they don't exist
#os.rmdir('newDir')


#Makes Sub directories and parents if they don't exist
#os.makedirs('newDir2/Sub-Dir-1')
#os.removedirs('newDir2/Sub-Dir-1')


print(os.stat('demo.txt'))

# Store timestamp of file
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# Rename File
#os.rename('test.txt', 'demo.txt')

"""
# List Working Directory
print(os.listdir())

print(os.getcwd())
"""

"""
# Change working directory
os.chdir('/home/jpon/PycharmProjects/')

print(os.getcwd())
"""

"""
# Walk through each directory and print out directory & filenames
for dirpath, dirnames, filenames in os.walk('/home/jpon/PycharmProjects/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
"""
print(os.environ.get('HOME'))

"""
# Manual way to specify path, but can be prone to errors if one forgets the "/". Use join instead
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)
"""

# Join file path using os function
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# Print directory vs filename
print(os.path.split('/tmp/tmp2/test.txt'))

# Print directory and filename vs extension
print(os.path.splitext('/tmp/tmp2/test.txt'))

