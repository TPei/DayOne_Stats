__author__ = 'TPei'
import xml.etree.ElementTree as ET

import pylab

from src.dayone_directory import *


def words_per_entry():

    file_path = get_file_path()
    entry_files = os.listdir(file_path)

    dayone_entries = []

    for file in entry_files:
        entry = open(file_path + file, "r")
        data = entry.read()

        root = ET.fromstring(data)
        dict_tag = root[0]
        dayone_entries.append((dict_tag.find("date").text, dict_tag.find("string").text))

    dayone_entries = sorted(dayone_entries)

    y_coords = []
    for entry in dayone_entries:
        words = entry[1].split()
        y_coords.append(len(words))

    pylab.figure(1)
    pylab.title("Words per Day One entry")
    pylab.xlabel("number of entries")
    pylab.ylabel("number of words")
    pylab.plot(y_coords)
    pylab.show()

if __name__ == '__main__':
    words_per_entry()
