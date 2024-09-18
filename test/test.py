import spotify

music = spotify.Spotify(url="https://www.youtube.com/watch?v=lCA7Fhgx8g4&ab_channel=Jakubication", parser="html.parser")

print(music.get_html())