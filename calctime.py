import os, re, sys
from tinytag import TinyTag

# globals 
videos = []
duration = 0

# Start
print('Please enter a directory(absolute path): ')
directory = input()
if (os.path.exists(directory)):
    os.chdir(directory)
else:
    print('Sorry, this path does not exist')
    sys.exit()

# Regex for mp4
mp4Regex = re.compile(r'\.mp4$')

# Put directory files in a list
content = os.listdir('.')

# Push into the array of videos the absolute path for every video
for file in content:
    if (mp4Regex.search(file)):
        video = os.path.join(os.path.abspath('.'), file)
        videos.append(video)

# Calculate the time for each video and add it
if len(videos) > 0:
    for video in videos:
        tag = TinyTag.get(video)
        duration += float("%.2f" % (tag.duration / 60))

durationMinutes = float("{0:.2f}".format(duration))
durationHours = duration / 60
durationHours = float("{0:.2f}".format(durationHours))

print('Estimated Watchtime: ' + str(durationHours) + ' Hours or ' + str(durationMinutes) + ' Minutes')