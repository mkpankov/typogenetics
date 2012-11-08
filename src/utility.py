"""Utility package"""

def string_chars_indices(s):
    """Creates a dict containing indices of all characters in lists"""
    d = dict()
    for i,l in enumerate(s):
        t = d.get(l, [])
        if t == []:
            t = [i]
        else:
            t += [i]
        d[l] = t
    return d


def find_fail_max(string_list, sub, start=0, end=None):
    string = ''.join(string_list)
    if end == None:
        end = len(string)
    result = string.find(sub,start,end)
    if result == -1:
        return len(string)
    else:
        return result
assert find_fail_max(list('abc'), 'b') == 1
assert find_fail_max(list('abc'), 'd') == 3

def stringify_list(l):
    return ''.join(l)
assert stringify_list(['A','B','C']) == 'ABC'
