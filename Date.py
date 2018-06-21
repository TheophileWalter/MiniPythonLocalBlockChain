# coding=utf-8
#!/bin/python3

import datetime
from time import gmtime, strftime


class Date:

    # Method : init
    # Params : self
    def __init__(self):
        return
    
    # Method : get current date
    # Params : self
    def get_date(self):
        timeZone = str(strftime("%z", gmtime()))
        currentDate = "%a-%b-%d--%H:%M:%S--"+timeZone[:3]+"-%Y"
        return datetime.datetime.now().strftime(currentDate)


# TESTS
if __name__ == '__main__':
    d = Date()
    print(d.get_date())