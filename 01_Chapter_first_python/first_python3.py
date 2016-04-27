#!/usr/Bin/env python3
# -*- coding: utf-8 -*-

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'Mib', 'Gib', 'Tib', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes = True):
    '''Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024

        if False, use multiples of 1000
        Returns: string
    '''

    if size < 0:
        raise ValueError('number must be non-negative')

    multipe = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multipe]:
        size /= multipe
        if size < multipe:
            return  '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(100000000000, False))
    print(approximate_size(100000000000))



