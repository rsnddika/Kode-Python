from pytube import YouTube

url = 'https://www.youtube.com/watch?v=mI2f7U4TVtA'
my_video = YouTube(url)
print(my_video.title)

my_video = my_video.streams.get_lowest_resolution()
my_video.download()