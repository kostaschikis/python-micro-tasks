# Micro-Tasks Automation 💻✔
I made these programs just for my personal use to automate some boring stuff but maybe they'll come in handy for another person out there.  

## ● watchtime.py 📄
Have you ever had a folder with a bunch of videos in it and wondered how many hours of watch time do they add up?<br>
This simple script does exactly that. It calculates the watch time of all videos combined within a directory<br>
Just insert the **absolute path** of the folder you want to calculate when the program asks you to.<br>
e.g. `C:\Users\Username\Videos\Captures`<br>
Used [TinyTag](https://github.com/devsnd/tinytag) to extract video metadata    
  
## ● deletesubs.py 📄
Have you ever downloaded a movie or a series that ships with a lot of subtitle files(.srt files) that you dont need?<br>
This script keeps only the english .srt files and deletes all the other within a directory.<br>
Again, you just insert the **absolute path** of the directory that contains the subtitles and the media when the program asks you to.<br> 
e.g. `C:\Users\Username\Movies\TheMovie`<br>

### More scripts to come... 

# Install Dependencies
1. `pip3 install pipenv(if you dont have pipenv)`
2. `pipenv shell`
3. `pipenv install`