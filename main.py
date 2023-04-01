from pytube import YouTube

url = 'https://www.youtube.com/watch?v=tZ5FBBnHfm4&t=408s&ab_channel=Junferno'
my_video = YouTube(url)
#thumbnail and title
print(my_video.title)
print(my_video.thumbnail_url)
#resolution
my_video = my_video.streams.get_highest_resolution()

my_video.download()