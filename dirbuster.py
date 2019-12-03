#!/usr/bin/env python

import requests
import sys

url = sys.argv[1]
dwordlist = r'/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt'
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

if url == '-h' or url == "--help" or url == '-help':
    print("usage: python dirbuster.py <url> <wordlist>\nif no wordlist was entered it will be using the defaul wordlist ("+dwordlist+")")
    exit()
elif len(sys.argv) == 2:
    wordlist = dwordlist
    print("using the default wordlist ("+dwordlist+")")
else:
    wordlist = sys.argv[2]

wl = open(wordlist).read().split('\n')

if url[-1] != '/':
    url += '/'
    
for word in wl:
    if '#' in word:
        pass
    else:
        url1 = url + word
        r = requests.get(url1, headers=ua)
        if r.status_code != 404:
            print("directory found: " + url1, "status code: " + str(r.status_code))
