__author__ = 'TPei'

def get_date(date_string):
    """
    creates a datetime object from dayone xml date format
    :param date_string: %yyyy-%mm-%ddT%hh:%mm:%ssZ
    :return: datetime object
    """

    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    import datetime
    return datetime.datetime(int(year), int(month), int(day))


def get_weekday(_datetime):
    """
    creates a datetime object from dayone xml date format
    :param datetime object
    :return: weekday (0-6)
    """
    return _datetime.weekday()

if __name__ == '__main__':
    """
    monday = 0
    ...
    sunday = 6
    """
    print get_date("2014-11-12T13:12:05Z")
    print get_weekday(get_date("2014-11-12T13:12:05Z"))

