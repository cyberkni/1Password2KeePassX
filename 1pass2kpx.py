#!/usr/bin/python
#
# This program converts a TSV formatted export file from 1Password to
# a XML file for KeePassX. This convertion is lossy since not all
# attributes in 1Password have corresponding attributes in KeePassX.
#
# The following values are carried over: title, username, password, URL, notes

# This list is all the properties which are not copied over from 1Password:
# ['contentsHash', 'securityLevel', 'htmlAction', 'htmlMethod', 'htmlName', 'htmlID', 'expiry_yy', 'expiry_mm', 'cardholder', 'cvv', 'type', 'ccnum', 'passwordHistory', 'name', 'number', 'phoneLocal', 'bank', 'validFrom_mm', 'validFrom_yy', 'phoneTollFree']

import csv
from collections import namedtuple
from lxml import etree
from lxml.etree import Element, ElementTree
import re
import sys
import time
import uuid

mapping = {'title': 'title',
           'username' : 'username',
           'url': 'URL_Location',
           'password': 'password',
           'comment': 'notes'}

def encode(val):
  for s, r in {'&': '&amp;', '>': '&gt;',
               '<': '&lt;', '"': '&quot;',
               "'": "&apos;"}.iteritems():
    val.replace(s, r)
  return val

def build_element(name, value):
  p = Element(name)
  p.text = value
  return p

def load_data(source):
  data = []
  
  with open(source, 'r') as infile:
    f_reader = csv.reader(infile, delimiter='\t')
    headings = f_reader.next()
  
    for i, heading  in enumerate(headings):
      headings[i] = re.sub("[^A-Za-z]", '_', heading)
  
    row_datatype = namedtuple('PasswordEntry', ', '.join(headings))
  
    for row in f_reader:
      data.append(row_datatype(*row))
    return data

def dump_xml(data, outfile):
  root = Element('database')
  tree = ElementTree(root)
  group = Element('group')
  root.append(group)
  group.append(build_element('title', 'All'))
  group.append(build_element('icon', '1'))
  group.append(build_element('expire', 'Never'))
  for password in data:
    entry = Element('entry')
    entry.append(build_element('icon', '1'))
    for target, source in mapping.iteritems():
      value = getattr(password, source)
      entry.append(build_element(target, encode(value)))
    for target in ['creation', 'lastaccess']: 
      entry.append(build_element(target, time.strftime("%Y-%m-%dT%H:%M:%S")))
    group.append(entry)
    
  tree.write(outfile, encoding='UTF-8', pretty_print=True)

def main(argv):
  if len(argv) < 2:
    print "Usage: ./%s <input tsv file> <output xml>"
    sys.exit(-1)
  
  source = argv[1]
  outfile = argv[2]
  data = load_data(source)
  dump_xml(data, outfile)

if __name__ == "__main__":
  main(sys.argv)
