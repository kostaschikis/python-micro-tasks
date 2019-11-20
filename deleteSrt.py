import os, re, sys

# Globals
srtRegex = re.compile(r'.(tr|pt|ja|it|es).srt$')

# Start
print('Please enter a directory(absolute path): ')
directory = input()
if (os.path.exists(directory)):
    os.chdir(directory)
else:
    print('Sorry, this path does not exist')
    sys.exit()

content = os.listdir(directory)

for srt in content:
    if (srtRegex.search(srt)):
        subtitle = os.path.join(os.path.abspath('.'), srt)
        os.remove(subtitle)
print('Successfully deleted all unnecessary srt\'s')        