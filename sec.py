#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
@description: script for get and parse files of the SEC website
@author: Manuel Parra
@date:
@licence:

The MIT License

Copyright (c) 2019

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial of the software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABLILITY, WHETHER IN AN ACTION OF CONTRAC, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import csv
import ssl
import time

# get year
ts = time.time() # time in seconds
time_st = time.gmtime(ts)
year = time_st.tm_year

# ignore SSL certificate erros
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.sec.gov/Archives/edgar/full-index/"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
rows = table('a')

links = list()
for row in rows:
    links.append(url + row.get('href', None))

qtrs = list()
for url in links:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    rows = table('a')
    for row in rows:
        qtrs.append(url + row.get('href', None))

    if (url[-5:-1] == str(year)): break
