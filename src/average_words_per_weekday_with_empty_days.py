from __future__ import division
__author__ = 'TPei'
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from src.dayone_directory import *
from src.dayone_date_parser import *
import datetime

def average_words_per_weekday_with_empty_days():

    file_path = get_file_path()
    entry_files = os.listdir(file_path)

    # tupel of all dayone entries (date, text)
    dayone_entry_pairs = []

    for file in entry_files:
        entry_pair = open(file_path + file, "r")
        data = entry_pair.read()

        root = ET.fromstring(data)
        dict_tag = root[0]
        dayone_entry_pairs.append((dict_tag.find("date").text, dict_tag.find("string").text))

    # total count of words by weekday
    weekday_word_count = []

    # total number of entries by weekday
    weekday_entry_count = []
    for i in range(0, 7):
        weekday_word_count.append(0)
        weekday_entry_count.append(0)

    # all days where an entry exists
    entry_days_since_first_entry = []

    for entry_pair in dayone_entry_pairs:
        entry_date = get_date(entry_pair[0])
        entry_days_since_first_entry.append(entry_date)

        single_entry_word_count = entry_pair[1].split()

        weekday_word_count[get_weekday(entry_date)] += len(single_entry_word_count)
        weekday_entry_count[get_weekday(entry_date)] += 1

    # current date going from first entry date to today
    current_date_iterator = min(entry_days_since_first_entry)

    # counting how often the weekday occured since first entry
    seven_day_count = [0, 0, 0, 0, 0, 0, 0]

    while current_date_iterator <= datetime.datetime.today():
        current_date_iterator += datetime.timedelta(days=1)

        seven_day_count[get_weekday(current_date_iterator)] += 1

    # divide workday word count by number of weekday occurences since first entry
    for i in range(0, 7):
        weekday_word_count[i] /= seven_day_count[i]

    fig = plt.figure()
    ax = fig.add_subplot(111)


    ## necessary variables
    ind = np.arange(len(weekday_word_count))                # the x locations for the groups
    width = 0.5              # the width of the bars

    ## the bars
    date_bars = ax.bar(ind, weekday_word_count, width)

    # axes and labels
    ax.set_xlim(-width, len(ind)+width)
    ax.set_ylim(0, max(weekday_word_count) + max(weekday_word_count) / 10)
    ax.set_ylabel('Wordcount')
    ax.set_title('Average Number of Words per Entry per Weekday')
    xTickMarks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)


    plt.show()

if __name__ == '__main__':
    average_words_per_weekday()