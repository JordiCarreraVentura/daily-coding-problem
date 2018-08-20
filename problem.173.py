# Write a function to flatten a nested dictionary. Namespace the keys with a period.
# 
# For example, given the following dictionary:
# 
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
# 
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.


from collections import OrderedDict

def f(history, test):
    curr = [(True, [], test)]
    while True:
        new = []
        for active, history, space in curr:
            if not active:
                new.append((active, history, space))
                continue
            for key, val in space.items():
                if isinstance(val, dict):
                    for _key, _val in val.items():
                        new_key = [x for x in history] + [key, _key]
                        if isinstance(_val, dict):
                            _new = (True, new_key, _val)
                        else:
                            _new = (False, new_key, _val)
                        new.append(_new)
                else:
                    _new = (False, [x for x in history] + [key], val)
                    new.append(_new)
        curr = new
        if not [state for state, _, _ in curr if state]:
            break
    return OrderedDict([
        ('.'.join(key), val)
        for _, key, val in sorted(curr, key=lambda x: x[-1])
    ])


if __name__ == '__main__':

    import json
    
    test = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    
    test = {
        "foobar": {
            "qwerty": 7,
            "asdfasdf": 55,
            "asdf": {
                'x': 1,
                'y': 2,
                'z': 3
            }
        },
        "key": 3,
        "foo": {
            "a": 5,
            "b": {
                "c": 44,
                "d": {
                    "garfield": 100,
                }
            },
            "bar": {
                "baz": 8,
                "starcraft": 918
            }
        }
    }
    
    data = f([], test)
    print data
    print json.dumps(data, indent=4)
