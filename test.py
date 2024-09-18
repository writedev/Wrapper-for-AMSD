import AMSD.spotify as spotify

music = spotify.Spotify(url="https://open.spotify.com/playlist/1u9WM7cJGDxk8sRNl1S7CM?si=6253ef20bb7e49bb")

print(music.get_all())