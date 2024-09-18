import spotify

music = spotify.Spotify(url="https://open.spotify.com/intl-fr/track/60AVJqYgyAlCckC6Nh2tgO?si=144213ae0a3a4547")

print(music.get_image())