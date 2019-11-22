import os, re, sys, math
from tinytag import TinyTag

# globals 
videos = []
duration = 0

# Regex for videos
videoRegex = re.compile(r'.mp4$|avi$|webm$|flv$')

# Start
print('Please enter a directory(absolute path): ')
directory = input()
if (os.path.exists(directory)):
    os.chdir(directory)
else:
    print('Sorry, this path does not exist')
    sys.exit()

# Put directory files in a list
content = os.listdir('.')

# Push into the videos array the absolute path for every video
for file in content:
    if (videoRegex.search(file)):
        video = os.path.join(os.path.abspath('.'), file)
        videos.append(video)

# Calculate the time for each video and add it
if len(videos) > 0:
    for video in videos:
        tag = TinyTag.get(video)
        duration += float("%.2f" % (tag.duration / 60))
    durationMinutes = math.floor(float("{0:.2f}".format(duration)))
    durationHours = duration / 60
    durationHours = float("{0:.1f}".format(durationHours))
    print('Estimated Watchtime: ' + str(durationHours) + ' Hours or ' + str(durationMinutes) + ' Minutes')
else:
    print('No videos found in this directory')        