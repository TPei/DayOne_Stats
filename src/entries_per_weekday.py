__author__ = 'TPei'
import xml.etree.ElementTree as ET

import numpy as np
import matplotlib.pyplot as plt

from src.dayone_directory import *
from dayone_date_parser import *


def entries_per_weekday():

    file_path = get_file_path()
    entry_files = os.listdir(file_path)

    dayone_entries = []

    for file in entry_files:
        entry = open(file_path + file, "r")
        data = entry.read()

        root = ET.fromstring(data)
        dict_tag = root[0]
        dayone_entries.append((dict_tag.find("date").text, dict_tag.find("string").text))

    entry_days = []
    for i in range(0, 7):
        entry_days.append(0)

    for entry in dayone_entries:
        entry_days[get_weekday(get_date(entry[0]))] += 1


    fig = plt.figure()
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(entry_days))                # the x locations for the groups
    width = 0.5              # the width of the bars

    ## the bars
    date_bars = ax.bar(ind, entry_days, width)

    # axes and labels
    ax.set_xlim(-width, len(ind)+width)
    ax.set_ylim(0, max(entry_days) + 10)
    ax.set_ylabel('Number of Entries')
    ax.set_title('Total Number of Entries per Weekday')
    xTickMarks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)


    plt.show()

if __name__ == '__main__':
    entries_per_weekday()