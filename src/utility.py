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

def replace_by_index(s, i, r):
    return s[:i] + r + s[i+1:]