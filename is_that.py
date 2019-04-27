#!/usr/bin/env python

# is_that.py
# Author: Ulas Can Cengiz (@ulsc)
# Version: 0.1.0

"""
if function name is_that not pointing a direction: "is_that that {value} and {args} {function_name}?"
e.g. "is_that that 1 and 2, 3, 4 a number?
if function name is_that pointing a direction: "is_that that {value} {function_name} {args}?"
e.g "is_that that 1 equal 2, 3, 4?
"""

import datetime
import re


# Type Checks
def a_list(value, *args):
    if not args:
        return isinstance(value, list)
    else:
        if isinstance(value, list):
            return same_type(value, *args)
        else:
            return False


def a_bool(value, *args):
    if not args:
        return isinstance(value, bool)
    else:
        if isinstance(value, bool):
            return same_type(value, *args)
        else:
            return False


def a_string(value, *args):
    if not args:
        return isinstance(value, str)
    else:
        if isinstance(value, str):
            return same_type(value, *args)
        else:
            return False


def an_int(value, *args):
    if not args:
        # Because bool is_that a subclass of int in Python
        return isinstance(value, int) and not isinstance(value, bool)
    else:
        if isinstance(value, int):
            for arg in args:
                if isinstance(arg, bool) or not isinstance(arg, int):
                    return False
            return True
        else:
            return False


def a_float(value, *args):
    if not args:
        return isinstance(value, float)
    else:
        if isinstance(value, float):
            return same_type(value, *args)
        else:
            return False


def a_complex(value, *args):
    if not args:
        return isinstance(value, complex)
    else:
        if isinstance(value, complex):
            return same_type(value, *args)
        else:
            return False


def a_number(value, *args):
    if not args:
        return (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)) and not isinstance(
            value, bool)
    else:
        if isinstance(value, int) or isinstance(value, float):
            for arg in args:
                if isinstance(arg, bool) or (
                        not isinstance(arg, int) and not isinstance(arg, float) and not isinstance(arg, complex)):
                    return False
            return True
        else:
            return False


def a_bytes(value, *args):
    if not args:
        return isinstance(value, bytes)
    else:
        if isinstance(value, bytes):
            return same_type(value, *args)
        else:
            return False


def a_bytearray(value, *args):
    if not args:
        return isinstance(value, bytearray)
    else:
        if isinstance(value, bytearray):
            return same_type(value, *args)
        else:
            return False


def a_tuple(value, *args):
    if not args:
        return isinstance(value, tuple)
    else:
        if isinstance(value, tuple):
            return same_type(value, *args)
        else:
            return False


def a_set(value, *args):
    if not args:
        return isinstance(value, set)
    else:
        if isinstance(value, set):
            return same_type(value, *args)
        else:
            return False


def a_dict(value, *args):
    if not args:
        return isinstance(value, dict)
    else:
        if isinstance(value, dict):
            return same_type(value, *args)
        else:
            return False


def a_frozenset(value, *args):
    if not args:
        return isinstance(value, frozenset)
    else:
        if isinstance(value, frozenset):
            return same_type(value, *args)
        else:
            return False


def a_range(value, *args):
    if not args:
        return isinstance(value, range)
    else:
        if isinstance(value, range):
            return same_type(value, *args)
        else:
            return False


def a_memoryview(value, *args):
    if not args:
        return isinstance(value, memoryview)
    else:
        if isinstance(value, memoryview):
            return same_type(value, *args)
        else:
            return False


def a_date(value, *args):
    if not args:
        # Because datetime is_that a subclass of date in Python
        return isinstance(value, datetime.date) and not isinstance(value, datetime.datetime)
    else:
        if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
            return same_type(value, *args)
        else:
            return False


def a_datetime(value, *args):
    if not args:
        return isinstance(value, datetime.datetime)
    else:
        if isinstance(value, datetime.datetime):
            return same_type(value, *args)
        else:
            return False


def a_time(value, *args):
    if not args:
        return isinstance(value, datetime.time)
    else:
        if isinstance(value, datetime.time):
            return same_type(value, *args)
        else:
            return False


def a_timedelta(value, *args):
    if not args:
        return isinstance(value, datetime.timedelta)
    else:
        if isinstance(value, datetime.timedelta):
            return same_type(value, *args)
        else:
            return False


def a_timezone(value, *args):
    if not args:
        return isinstance(value, datetime.timezone)
    else:
        if isinstance(value, datetime.timezone):
            return same_type(value, *args)
        else:
            return False


def a_function(value):
    # TODO: ARGS!
    return callable(value)


def an_exception(value, *args):
    if not args:
        return isinstance(value, Exception)
    else:
        if isinstance(value, Exception):
            return same_type(value, *args)
        else:
            return False


# Value Checks
def true(value, *args):
    if not isinstance(value, bool) or not same_type(value, *args):
        return False
    if not args:
        return value is True
    elif value is True:
        return equal(value, *args)
    return False


def false(value, *args):
    if not isinstance(value, bool) or not same_type(value, *args):
        return False
    if not args:
        return value is False
    elif value is False:
        return equal(value, *args)
    return False


def none(value, *args):
    if value is not None or not same_type(value, *args):
        return False
    if not args:
        return value is None
    elif value is None:
        return same_type(value, *args)
    return False


def same_type(value, *args):
    if not args:
        return True
    for arg in args:
        if type(value) != type(arg):
            return False
    return True


def equal(value, *args):
    if not args:
        return True
    for arg in args:
        if value != arg or type(value) != type(arg):
            return False
    return True


def even(value, *args):
    if isinstance(value, bool):
        return False
    elif not isinstance(value, int) and not (isinstance(value, float) and value.is_integer()):
        return False
    elif int(value) % 2 != 0:
        return False
    for arg in args:
        if isinstance(arg, bool):
            return False
        elif not isinstance(arg, int) and not (isinstance(arg, float) and arg.is_integer()):
            return False
        elif int(arg) % 2 != 0:
            return False
    return True


def odd(value, *args):
    if isinstance(value, bool):
        return False
    elif not isinstance(value, int) and not (isinstance(value, float) and value.is_integer()):
        return False
    elif int(value) % 2 != 1:
        return False
    for arg in args:
        if isinstance(arg, bool):
            return False
        elif not isinstance(arg, int) and not (isinstance(arg, float) and arg.is_integer()):
            return False
        elif int(arg) % 2 != 1:
            return False
    return True


def whole_number(value, *args):
    if not a_number(value):
        return False
    if not args:
        return value % 1 == 0
    elif value % 1 == 0:
        for arg in args:
            if not a_number(arg) or arg % 1 != 0:
                return False
        return True
    else:
        return False


def positive(value, *args):
    if not a_number(value):
        return False
    if not args:
        return value > 0
    elif value > 0:
        for arg in args:
            if not a_number(arg) or arg <= 0:
                return False
        return True
    else:
        return False


def negative(value, *args):
    if not a_number(value):
        return False
    if not args:
        return value < 0
    elif value < 0:
        for arg in args:
            if not a_number(arg) or arg >= 0:
                return False
        return True
    else:
        return False


def zero(value, *args):
    if not a_number(value):
        return False
    if not args:
        return value == 0
    elif value == 0:
        for arg in args:
            if not a_number(arg) or arg != 0:
                return False
        return True
    else:
        return False


def under(value, check):
    if a_complex(value) or a_complex(check):
        return False
    if a_number(value) and a_number(check):
        return value < check
    else:
        return False


def under_or_equal(value, check):
    if a_complex(value) or a_complex(check):
        return False
    if a_number(value) and a_number(check):
        return value <= check
    else:
        return False


def over(value, check):
    if a_complex(value) or a_complex(check):
        return False
    if a_number(value) and a_number(check):
        return value > check
    else:
        return False


def over_or_equal(value, check):
    if a_complex(value) or a_complex(check):
        return False
    if a_number(value) and a_number(check):
        return value >= check
    else:
        return False


def between(value, check_min, check_max):
    if a_complex(value) or a_complex(check_min) or a_complex(check_max):
        return False
    if a_number(value) and a_number(check_min) and a_number(check_max):
        return check_max > value > check_min
    else:
        return False


def between_or_equal(value, check_min, check_max):
    if a_complex(value) or a_complex(check_min) or a_complex(check_max):
        return False
    if a_number(value) and a_number(check_min) and a_number(check_max):
        return check_max >= value >= check_min
    else:
        return False


def multiple_of(value, check):
    if a_complex(value) or a_complex(check):
        return False
    if whole_number(value) and whole_number(check) and not zero(check):
        return value % check == 0
    return False


def empty(value, *args):
    if not isinstance(value, list) and not isinstance(value, dict) and not isinstance(value, set):
        return False
    elif not args:
        return len(value) == 0
    else:
        if len(value) != 0:
            return False
        for arg in args:
            if not isinstance(arg, list) and not isinstance(arg, dict) and not isinstance(arg, set):
                return False
            elif len(arg) != 0:
                return False
        return True


def file_exists(value, *args):
    if not a_string(value, *args):
        return False
    try:
        open(value, 'r')
    except FileNotFoundError:
        return False
    if args:
        for arg in args:
            try:
                open(arg, 'r')
            except FileNotFoundError:
                return False
    return True


def palindrome(value, *args):
    if not a_string(value, *args):
        return False
    if value != value[::-1]:
        return False
    if args:
        for arg in args:
            if arg != arg[::-1]:
                return False
    return True


def uppercase(value, *args):
    if not a_string(value, *args):
        return False
    if not value.isupper():
        return False
    if args:
        for arg in args:
            if not arg.isupper():
                return False
    return True


def lowercase(value, *args):
    if not a_string(value, *args):
        return False
    if not value.islower():
        return False
    if args:
        for arg in args:
            if not arg.islower():
                return False
    return True


def titlecase(value, *args):
    if not a_string(value, *args):
        return False
    if not value.istitle():
        return False
    if args:
        for arg in args:
            if not arg.istitle():
                return False
    return True


def contains(value, *args):
    if not args:
        return False
    if not a_string(value, *args):
        return False
    for arg in args:
        if arg not in value:
            return False
    return True


def startswith(value, *args):
    if not args:
        return False
    if not a_string(value, *args):
        return False
    for arg in args:
        if len(value) == 0:
            if len(arg) != 0:
                return False
        else:
            if not value.startswith(arg) or len(arg) == 0:
                return False
    return True


def endswith(value, *args):
    if not args:
        return False
    if not a_string(value, *args):
        return False
    for arg in args:
        if len(value) == 0:
            if len(arg) != 0:
                return False
        else:
            if not value.endswith(arg) or len(arg) == 0:
                return False
    return True


# Regex Checks
def alphanumeric(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^[a-zA-Z0-9]+$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def email(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", re.IGNORECASE)
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def btc_address(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])$",
                       re.IGNORECASE)
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def credit_card(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^(?:(4[0-9]{12}(?:[0-9]{3})?)|"
                       r"(5[1-5][0-9]{14})|"
                       r"(6(?:011|5[0-9]{2})[0-9]{12})|"
                       r"(3[47][0-9]{13})|(3(?:0[0-5]|[68][0-9])[0-9]{11})|"
                       r"((?:2131|1800|35[0-9]{3})[0-9]{11}))$", re.IGNORECASE)
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def ipv4(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def ipv6(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(
        r"^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,7}:|"
        r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|"
        r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|"
        r"([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|"
        r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|"
        r":((:[0-9a-fA-F]{1,4}){1,7}|:)|"
        r"fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]+|"
        r"::(ffff(:0{1,4})?:)?((25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9])\.){3}(25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9])|"
        r"([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|"
        r"(2[0-4]|1?[0-9])?[0-9])\.){3}(25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9]))$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def ip(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(
        r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,7}:|"
        r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|"
        r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|"
        r"([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|"
        r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|"
        r":((:[0-9a-fA-F]{1,4}){1,7}|:)|"
        r"fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]+|"
        r"::(ffff(:0{1,4})?:)?((25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9])\.){3}(25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9])|"
        r"([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|"
        r"(2[0-4]|1?[0-9])?[0-9])\.){3}(25[0-5]|(2[0-4]|"
        r"1?[0-9])?[0-9]))$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def hex_color(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def tckn(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^[1-9][0-9]{10}$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def social_security_number(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def url(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^(http[s]?://[www.]?)?[a-z0-9]+([\-.][a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


def us_zip_code(value, *args):
    if not a_string(value, *args):
        return False
    regex = re.compile(r"^(\d{5})([- ])?(\d{4})?$")
    if not regex.match(value):
        return False
    if args:
        for arg in args:
            if not regex.match(arg):
                return False
    return True


# Date Checks
def future(value, *args):
    if not isinstance(value, datetime.date):
        return False
    if not args:
        if isinstance(value, datetime.datetime):
            return value > datetime.datetime.now()
        return value > datetime.datetime.now().date()
    if isinstance(value, datetime.datetime):
        if value <= datetime.datetime.now():
            return False
    if value <= datetime.datetime.now().date():
        return False
    for arg in args:
        if not isinstance(arg, datetime.date):
            return False
        elif isinstance(arg, datetime.datetime):
            if arg <= datetime.datetime.now():
                return False
        elif arg <= datetime.datetime.now().date():
            return False
    return True


def past(value, *args):
    now = datetime.datetime.now()
    if not isinstance(value, datetime.date):
        return False
    if not args:
        if isinstance(value, datetime.datetime):
            return value < now
        return value < now.date()
    if isinstance(value, datetime.datetime):
        if value >= now:
            return False
    if value >= now.date():
        return False
    for arg in args:
        if not isinstance(arg, datetime.date):
            return False
        elif isinstance(arg, datetime.datetime):
            if arg >= now:
                return False
        elif arg >= now.date():
            return False
    return True


def in_date_range(value, check_min, check_max):
    if (a_date(value) or a_datetime(value)) and same_type(value, check_min, check_max):
        return check_max > value > check_min
    else:
        return False


def today(value, *args):
    # TODO: FILL ME IN!
    pass


def yesterday(value, *args):
    # TODO: FILL ME IN!
    pass


def last_week(value, *args):
    # TODO: FILL ME IN!
    pass


def last_month(value, *args):
    # TODO: FILL ME IN!
    pass


def last_quarter(value, *args):
    # TODO: FILL ME IN!
    pass


def last_year(value, *args):
    # TODO: FILL ME IN!
    pass


def tomorrow(value, *args):
    # TODO: FILL ME IN!
    pass


def next_week(value, *args):
    # TODO: FILL ME IN!
    pass


def next_month(value, *args):
    # TODO: FILL ME IN!
    pass


def next_quarter(value, *args):
    # TODO: FILL ME IN!
    pass


def next_year(value, *args):
    # TODO: FILL ME IN!
    pass


def leap_year(value, *args):
    # TODO: FILL ME IN!
    pass


def weekday(value, *args):
    # TODO: FILL ME IN!
    pass


def weekend(value, *args):
    # TODO: FILL ME IN!
    pass
