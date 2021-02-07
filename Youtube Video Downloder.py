import pytube
link = "video link"
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download(r'O:\Youtube Video Down')