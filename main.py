from pytube import YouTube
#put the link here
url = ''
my_video = YouTube(url)
#thumbnail and title
print(my_video.title)
print(my_video.thumbnail_url)
#resolution
my_video = my_video.streams.get_highest_resolution()

my_video.download()
