playlist = {
    'title': 'patagonia bus',
    'author': 'Colt Steele',
    'songs': [
        {
            'title': 'song1', 'artist': ['blue'], 'duration': 4.5
        },
        {
            'title': 'song2', 'artist': ['blue', 'djcat'], 'duration': 2.5
        },
        {
            'title': 'song3', 'artist': ['blue', 'djcat', 'divine'], 'duration': 5.5
        }
    ]
}

for song in playlist['songs']:
    print(songs['title'])
    totalLength += songs['duration']

print(totalLength)
