
# Problem #360

> This problem was asked by Spotify.
> 
> You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. For example, the list *\[4, 1, 7\]* indicates that a user likes song 4 the best, followed by songs 1 and 7.
> 
> Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.
> 
> For example, suppose your input is


```python
data = [
    [1, 7, 3],
    [2, 1, 6, 7, 9],
    [3, 9, 5]
]
```

In this case a satisfactory playlist could be *\[2, 1, 6, 7, 3, 9, 5\]*.


```python
def average(values):
    return sum(values) / float(len(values))
```


```python
def f(data):
    
    def __get_preferences_by_song(data):
        preferences_by_song = dict([])
        for preferences in data:
            for i, song in enumerate(preferences):
                if not preferences_by_song.has_key(song):
                    preferences_by_song[song] = []
                preferences_by_song[song].append(i)
        for song, preferences in preferences_by_song.items():
            if len(preferences) < len(data):
                preferences += [
                    max([len(prefs) for prefs in data])
                    for i in range(len(preferences), len(data))
                ]
        return preferences_by_song
    
    preferences_by_song = __get_preferences_by_song(data)
    interleaved = sorted(
        preferences_by_song.keys(),
        key=lambda song: average(preferences_by_song[song])
    )
    
    return interleaved
    

print f(data)
```

    1 [0, 1, 5] 2.0
    3 [2, 0, 5] 2.33333333333
    7 [1, 3, 5] 3.0
    2 [0, 5, 5] 3.33333333333
    9 [4, 1, 5] 3.33333333333
    5 [2, 5, 5] 4.0
    6 [2, 5, 5] 4.0
    [1, 3, 7, 2, 9, 5, 6]

