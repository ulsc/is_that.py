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
        return isinstance(value, datetime.date)
    else:
        if isinstance(value, datetime.date):
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


def a_tzinfo(value, *args):
    if not args:
        return isinstance(value, datetime.tzinfo)
    else:
        if isinstance(value, datetime.tzinfo):
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


def none(value):
    # TODO: ARGS!
    return value is None


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
        if value != arg:
            return False
    return True


def even(value):
    # TODO: ARGS!
    if isinstance(value, int) and not isinstance(value, bool):
        return value % 2 == 0
    elif isinstance(value, float) and value.is_integer():
        return int(value) % 2 == 0
    return False


def odd(value):
    # TODO: ARGS!
    if isinstance(value, int) and not isinstance(value, bool):
        return value % 2 == 1
    elif isinstance(value, float) and value.is_integer():
        return int(value) % 2 == 1
    return False


def whole_number(value):
    # TODO: ARGS!
    if not a_number(value):
        return False
    return value % 1 == 0


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
    if a_number(value) and a_number(check):
        return value < check
    else:
        return False


def under_or_equal(value, check):
    if a_number(value) and a_number(check):
        return value <= check
    else:
        return False


def over(value, check):
    if a_number(value) and a_number(check):
        return value > check
    else:
        return False


def over_or_equal(value, check):
    if a_number(value) and a_number(check):
        return value >= check
    else:
        return False


def between(value, check_min, check_max):
    if a_number(value) and a_number(check_min) and a_number(check_max):
        return check_max > value > check_min
    else:
        return False


def between_or_equal(value, check_min, check_max):
    if a_number(value) and a_number(check_min) and a_number(check_max):
        return check_max >= value >= check_min
    else:
        return False


def multiple_of(value, check):
    if whole_number(value) and whole_number(check) and not zero(check):
        return value % check == 0
    return False


def empty(value):
    # TODO: ARGS!
    if not isinstance(value, list) and isinstance(value, dict) and isinstance(value, set):
        return False
    else:
        return len(value) == 0


def file_exists(value):
    # TODO: ARGS!
    try:
        open(value, 'r')
        return True
    except FileNotFoundError:
        return False


def palindrome(value, *args):
    # TODO: FILL ME IN!
    pass


def uppercase(value, *args):
    # TODO: FILL ME IN!
    pass


def lowercase(value, *args):
    # TODO: FILL ME IN!
    pass


def contains(value, *args):
    # TODO: FILL ME IN!
    pass


def begins_with(value, check):
    # TODO: FILL ME IN!
    pass


def ends_with(value, check):
    # TODO: FILL ME IN!
    pass


# Regex Checks
def alphanumeric(value):
    # TODO: ARGS!
    if not a_string(value):
        return False
    if re.compile("[a-zA-Z0-9]+").match(value):
        return True
    return False


def email(value):
    # TODO: ARGS!
    if not a_string(value):
        return False
    if re.compile(
            "([a-z0-9!#$%&'*+/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)",
            re.IGNORECASE).match(value):
        return True
    return False


def btc_address(value):
    # TODO: ARGS!
    if not a_string(value):
        return False
    if re.compile("(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])").match(value):
        return True
    return False


def credit_card(value):
    # TODO: ARGS!
    if not a_string(value):
        return False
    if re.compile("((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])").match(value):
        return True
    return False


def ipv4(value, *args):
    # TODO: FILL ME IN!
    pass


def ipv6(value, *args):
    # TODO: FILL ME IN!
    pass


def ip(value, *args):
    # TODO: FILL ME IN!
    pass


def hex_color(value, *args):
    # TODO: FILL ME IN!
    pass


def social_security_number(value, *args):
    # TODO: FILL ME IN!
    pass


def url(value, *args):
    # TODO: FILL ME IN!
    pass


def us_zip_code(value, *args):
    # TODO: FILL ME IN!
    pass


# Date Checks
def future(value):
    # TODO: ARGS!
    if a_date(value):
        return value > datetime.datetime.now().date()
    elif a_datetime(value):
        return value > datetime.datetime.now()
    else:
        return False


def past(value):
    # TODO: ARGS!
    if a_date(value):
        return value < datetime.datetime.now().date()
    elif a_datetime(value):
        return value < datetime.datetime.now()
    else:
        return False


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