__author__ = 'TPei'
from average_words_per_weekday import average_words_per_weekday
from entries_per_weekday import entries_per_weekday
from total_words_per_weekday import total_words_per_weekday
from words_per_entry import words_per_entry
from words_per_entrydate import words_per_entrydate

def handle_input():
    print "Welcome to your personal DayOne Stats Analyzer"
    print "-----------------------------"
    print "The following Analyzation options are currently supported:"
    print "(Choose one by entering the corresponding number)"
    print ""
    print "Words per Entry (0)"
    print "Entries per Weekday (1)"
    print "Total Words per Weekday (2)"
    print "Average Words per Entry per Weekday (3)"
    print ""
    choice = input(">>> ")

    print ""
    if choice == 0:
        print "words per entry chosen"
        words_per_entry()
    elif choice == 1:
        print "entries per weekday chosen"
        entries_per_weekday()
    elif choice == 2:
        print "total words per weekday chosen"
        total_words_per_weekday()
    elif choice == 3:
        print "average words per entry per weekdaychosen"
        average_words_per_weekday()
    else:
        print "Unfortunately, this is not a valid option"
        handle_input()

if __name__ == '__main__':
    handle_input()