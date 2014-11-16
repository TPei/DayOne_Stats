__author__ = 'TPei'
import os
import xml.etree.ElementTree as ET
import pylab
from dayone_directory import *

'''
first step, support for unzipped DayOne backup file folder (.doentry files)
'''

'''
this is the path to an unzipped dayone backup directory
which contains a lot of .doentry files
'''

file_path = get_file_path()
entry_files = os.listdir(file_path)

dayone_entries = []

for file in entry_files:
    entry = open(file_path + file, "r")
    data = entry.read()

    root = ET.fromstring(data)
    dict_tag = root[0]
    dayone_entries.append((dict_tag.find("date").text, dict_tag.find("string").text))

entry_dates = []
entry_word_count = []
for entry in dayone_entries:
    entry_dates.append(entry[0])

    words = entry[1].split()
    entry_word_count.append(len(words))

pylab.figure(1)
pylab.title("Words per Day One entry")
pylab.xlabel("number of entries")
pylab.ylabel("number of words")
pylab.plot(entry_word_count)
pylab.show()
