
# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_265.py

def get_segments(arr):
    asc = arr[1] > arr[0]
    prev = arr[0]
    start = 0
    segments = []
    for i, num in enumerate(arr[1:]):
        if (asc and num < prev) or (not asc and num > prev):
            segments.append((asc, i - start + 1))
            start = i + 1
            asc = not asc

        prev = num

    segments.append((asc, len(arr) - start))

    return segments


def get_bonuses(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return [1]

    segments = get_segments(arr)
    bonuses = list()
    for segment in segments:
        asc, length = segment
        seg_bonuses = list(range(length))
        if not asc:
            seg_bonuses.reverse()
        bonuses.extend(seg_bonuses)

    bonuses = [x + 1 for x in bonuses]

    return bonuses


tests = [
    [10, 40, 200, 1000, 60, 30],
    [10, 40, 200, 1000, 60, 30, 10, 5],
    [10, 40, 200, 1000, 60, 30, 5, 10],
    [10, 200, 40, 1000, 5, 10, 30, 60],
    [10, 200, 40, 1000, 5, 30, 10, 60]
]

for test in tests:
    print(test, get_bonuses(test))