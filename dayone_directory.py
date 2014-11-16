__author__ = 'TPei'
import getpass
import os


def get_file_path():
    """
    find default dayone entries folder, which is in the users' iCloud drive
    /Users/<username>/Library/Mobile Documents/<some semi-cryptic dayoneapp folder>/Documents/Journal_dayone/entries/
    :return:
    """
    username = getpass.getuser()

    file_path = "/Users/" + username + "/Library/Mobile Documents/"
    folders = os.listdir(file_path)

    for folder in folders:
        if "dayoneapp" in folder:
            return file_path + folder + "/Documents/Journal_dayone/entries/"

if __name__ == '__main__':
    print get_file_path()