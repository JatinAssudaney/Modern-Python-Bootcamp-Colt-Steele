songs = [
    {
        "title": "happy birthday", "playcount": 1
    },
    {
        "title": "Survive", "playcount": 6
    },
    {
        "title": "YMCA", "playcount": 99
    },
    {
        "title": "Toxic", "playcount": 31
    }]

# order = sorted(songs,key = lambda s : s["playcount"],reverse=True)
order = min(songs, key=lambda s: s["playcount"])
print(order)
