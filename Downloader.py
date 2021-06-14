from pytube import YouTube
def Downloader(url):
    my_video = YouTube(url)
    print('************************* Video Title ********************************')
    print(my_video.title)
    print('************************* Video ThumbNail ******************************')
    print(my_video.thumbnail_url)
    print('************************* Wait Untill Video download *******************')
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    print('*************************** Video Downloaded *****************************')
Downloader('https://www.youtube.com/watch?v=e90SNkIZPBg')


