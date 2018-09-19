#!/usr/bin/python3
import sys
import datetime

def format_me(date, format):

    def format_date():
        print (datetime.date.strftime(date, "%Y-%m-%d"))
    return format_date()