#!/usr/bin/python

import csv
from collections import namedtuple
import re
import sys

filename = sys.argv[1]
fh = open(filename, 'r')

f_reader = csv.reader(fh, delimiter='\t')

headings = f_reader.next()

for i, heading  in enumerate(headings):
    headings[i] = re.sub("[^A-Za-z]", '_', heading)

row_datatype = namedtuple('PasswordEntry', ', '.join(headings))

data = []
for row in f_reader:
    data.append(row_datatype(*row))

print len(data)

