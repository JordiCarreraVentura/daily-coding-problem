# This problem was asked by Quora.
# 
# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
# 
# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

def f(test):
    parts = test.split('/')
    path = []
    while parts:
        part = parts.pop(0).strip()
        if not part:
            continue
        if part == '.':
            continue
        elif part == '..':
            path.pop()
        else:
            path.append(part)
    return '/%s/' % '/'.join(path)


if __name__ == '__main__':
    
    tests = [
        '/usr/bin/../bin/./scripts/../',
        '/Users/jordi/Laboratorio/Python/daily-coding-problem',
        '/Users/jordi/Laboratorio/../..',
        '/Users/jordi/Laboratorio/../Laboratorio/././Python',
        '/Users/jordi/Laboratorio/../Laboratorio/./Python',
        '/Users/jordi/Laboratorio/../Laboratorio/./Python/../Python',
        '/Users/jordi/Laboratorio/Python/../../..',
    ]
    
    for test in tests:
        print test
        print f(test)
        print
