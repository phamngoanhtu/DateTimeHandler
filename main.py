r"""DTHandler is used for formatting timestamp and calculate the difference between two days.
This exports:
    - DTHandler.normalize: change the format to MM-DD-YYYY / MM-DD-YYYY HH:MM:SS (excluded timezone)

This is version 0.5 Latest Updated: 29-01-2022 2:05:00 UTC +7
written by PhamNgoAnhTu
"""
import sys


from termcolor import colored
from datetime import datetime
from datetime import timedelta


class DTHandler:
    def __init__(self):
        self.timestamp = datetime.now()

    def get_timestamp(self, date_obj):
        self.timestamp = self.normalize(date_obj)
        return self.timestamp

    # Detect if timestamp is string datatime or Python datatime
    # Then, they all will be converted to Python datetime
    # Format: MM-DD-YYYY / MM-DD-YYYY HH:MM:SS (excluded timezone)
    def normalize(self, date_obj):
        # Check if date_obj is a string or a Python Date
        if isinstance(date_obj, str):
            # Convert from string to Datetime Python
            # strptime: string parser, this will convert a string format to datetime.
            # strftime: string formatter, this will format a datetime object to string.
            try:
                normalized_date_object = datetime.strptime(date_obj, '%d-%m-%Y %H:%M:%S')
            except ValueError:
                try:
                    normalized_date_object = datetime.strptime(date_obj, '%d-%m-%Y')
                except ValueError:
                    output = colored("The Date Object is a string or PyDate as DD-MM-YYYY or DD-MM-YYYY HH:MM:SS", 'red')
                    print(output)
                    sys.exit()

        elif isinstance(date_obj, datetime):
            # Convert from Datetime to string DD-MM-YYY Format
            # Convert back to Datetime
            try:
                normalized_date_object = date_obj.strftime('%d-%m-%Y %H:%M:%S')
                normalized_date_object = datetime.strptime(normalized_date_object, '%d-%m-%Y %H:%M:%S')
            except ValueError:
                try:
                    normalized_date_object = timestamp.strftime('%d-%m-%Y')
                    normalized_date_object = datetime.strptime(normalized_date_object, '%d-%m-%Y')
                except ValueError:
                    output = colored("The Date Object is a string or PyDate as DD-MM-YYYY or DD-MM-YYYY HH:MM:SS", 'red')
                    print(output)
                    sys.exit()

        else:
            output = colored("The Date Object is a string or PyDate as DD-MM-YYYY or DD-MM-YYYY HH:MM:SS", 'red')
            print(output)
            sys.exit()
        return normalized_date_object

    # monthNum_to_monthName is used for converting month number to month name, example: 12-01-2022 -> 12-Jan-2022
    def monthNum_to_monthName(self, month_stamp):
        month_Name = self.get_timestamp(month_stamp)
        month_Name = datetime.strftime(month_Name, '%d-%b-%Y %H:%M:%S')
        print("\nTimestamp in Name:", month_Name)

    # compare_date is used for calculate any string datetime with current time and return day number
    def compare_date(self, given_date):
        given_date = datetime.strptime(given_date, '%d-%m-%Y')
        delta = datetime.now() - given_date
        print("\nThe number of days between 2 date is:", delta.days)
        return delta.days

    def conversion(self, second):
        _second = second - (60 * self.second_to_minute(second))
        minute = self.second_to_minute(second)
        _minute = minute - (60 * self.minute_to_hour(minute))
        hour = self.minute_to_hour(minute)
        _hour = hour - (24 * self.hour_to_day(hour))
        day = self.hour_to_day(hour)
        print("\nAfter conversion, It will be {3} day(s), {2} hour(s), {1} minute(s), {0} second(s)".format(_second, _minute, _hour, day))

    def second_to_minute(self, second):
        return second // 60

    def minute_to_hour(self, minute):
        return minute // 60

    def hour_to_day(self, hour):
        return hour // 24

    # string_to_SQLServer is used to convert string datetime into SQL server datetime
    def string_to_SQLServer(self, string_datetime):
        SQL_datetime = datetime.strptime(string_datetime, '%d-%m-%Y %H:%M:%S')
        print("\nSQL Datetime:", SQL_datetime)

    # next_week_day is used to find next week from a datetime input
    def next_week_day(self, date_obj):
        current_week_date = self.get_timestamp(date_obj)
        date_in_week = current_week_date.weekday()
        next_week_day = current_week_date + timedelta(days=7 - date_in_week)
        return next_week_day


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = DTHandler()
        self.data = self.data.get_timestamp(data)
        self.next = None  # Initialize next as null


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None

    # This function prints contents of linked list
    # starting from head
    def print_list(self):
        temp = self.head
        while temp:
            print("\n", temp.data)
            temp = temp.next

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    # This function prints out the youngest datetime in the list
    def youngest_datetime(self):
        temp = self.head
        youngest_datetime = temp.data
        youngest_datetime_age = self.calculate_age(youngest_datetime)
        while temp:
            _datetime = temp.data
            age = self.calculate_age(_datetime)

            if age < youngest_datetime_age:
                youngest_datetime = _datetime
            temp = temp.next
        print("\nYoungest Datetime:", youngest_datetime)

    # This function returns days difference between datetime with current date
    def calculate_age(self, given_date):
        delta = datetime.now() - given_date
        return delta

#######################################################################


x = DTHandler()
timestamp = x.get_timestamp("19-11-2002")
x.monthNum_to_monthName(datetime.now())
x.compare_date("19-11-2002")
x.conversion(365)
x.string_to_SQLServer('19-11-2020 23:00:23')
print("\nThe next week of day starts from", x.next_week_day(datetime.now()))

LinkedList = LinkedList()
LinkedList.append("19-11-2002")
LinkedList.append("20-11-2002")
LinkedList.print_list()
LinkedList.youngest_datetime()
