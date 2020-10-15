#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = 'алигортм'
    n = s.find('и')
    s = s[:n] + s[n+1:n+4] + s[n] + s[n+4:]
    print(s)
