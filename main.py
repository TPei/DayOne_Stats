__author__ = 'TPei'
import os
import xml.etree.ElementTree as ET
import pylab

'''
first step, support for unzipped DayOne backup file folder (.doentry files)
'''

'''
this is the path to an unzipped dayone backup directory
which contains a lot of .doentry files
'''

file_path = "/Users/thomas/Library/Containers/com.dayoneapp.dayone/Data/Library/Application Support/Backup/Journal_dayone/entries/"
entry_files = os.listdir(file_path)

dayone_entries = []

for file in entry_files:
    entry = open(file_path + file, "r")
    data = entry.read()

    root = ET.fromstring(data)
    dict_tag = root[0]
    dayone_entries.append((dict_tag.find("date").text, dict_tag.find("string").text))


y_coords = []
for entry in dayone_entries:
    words = entry[1].split()
    y_coords.append(len(words))

pylab.figure(1)
pylab.title("Words per Day One entry")
pylab.xlabel("number of entry")
pylab.ylabel("number of words")
pylab.plot(y_coords)
pylab.show()
