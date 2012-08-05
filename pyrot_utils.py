"""Utilities for ROT translation"""
import string

def rot(n, s):
    """Translates string s using ROT-n"""
    lowers = string.lowercase
    rotlowers = string.maketrans(lowers, lowers[n:] + lowers[:n])
    return string.translate(string.lower(s), rotlowers)

def rotcheck(s, t, n):
    """check whether rot-n translates s --> t"""
    l = string.lowercase
    tt = string.maketrans(l, l[n:] + l[:n])
    mbt = string.translate(string.lower(s), tt)
    if mbt == t:
        return 1
    else:
        return 0
