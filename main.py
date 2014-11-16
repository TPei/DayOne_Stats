from src import entries_per_weekday, total_words_per_weekday, words_per_entry, average_words_per_weekday, average_words_per_weekday_with_empty_days

__author__ = 'TPei'


def handle_input():
    print ""
    print "Welcome to your personal DayOne Stats Analyzer"
    print "-----------------------------"
    print "The following Analyzation options are currently supported:"
    print "(Choose one by entering the corresponding number)"
    print ""
    print "Words per Entry (0)"
    print "Entries per Weekday (1)"
    print "Total Words per Weekday (2)"
    print "Average Words per Entry per Weekday (3)"
    print "Average Words per Entry per Weekday when considering non-entry days (4)"
    print ""
    choice = input(">>> ")

    execute_choice(choice)


def execute_choice(choice):
    print ""
    if choice == 0:
        print "words per entry chosen"
        words_per_entry.words_per_entry()
    elif choice == 1:
        print "entries per weekday chosen"
        entries_per_weekday.entries_per_weekday()
    elif choice == 2:
        print "total words per weekday chosen"
        total_words_per_weekday.total_words_per_weekday()
    elif choice == 3:
        print "average words per entry per weekday chosen"
        average_words_per_weekday.average_words_per_weekday()
    elif choice == 4:
        print "average words per entry per weekday with empty chosen"
        average_words_per_weekday_with_empty_days.average_words_per_weekday_with_empty_days()
    else:
        print "Unfortunately, this is not a valid option"
        handle_input()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        execute_choice(int(sys.argv[1]))
    else:
        handle_input()