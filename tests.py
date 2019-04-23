import datetime

import is_that


def test_a_list():
    assert is_that.a_list([])
    assert is_that.a_list(["test"])
    assert is_that.a_list(["test"], ["test1"], ["test2"], ["test3"])
    assert not is_that.a_list(["test"], ["test1"], ["test2"], "test3")
    assert not is_that.a_list("")
    assert not is_that.a_list(True)
    assert not is_that.a_list(False)
    assert not is_that.a_list(0)
    assert not is_that.a_list(0.0)


def test_a_bool():
    assert is_that.a_bool(True)
    assert is_that.a_bool(False)
    assert is_that.a_bool(False, True, False)
    assert not is_that.a_bool([])
    assert not is_that.a_bool(["test"])
    assert not is_that.a_bool("")
    assert not is_that.a_bool(0)
    assert not is_that.a_bool(0.0)


def test_a_string():
    assert is_that.a_string("")
    assert is_that.a_string("test")
    assert is_that.a_string("", "")
    assert is_that.a_string("test", "", "test")
    assert not is_that.a_string(0)
    assert not is_that.a_string("test", 0)
    assert not is_that.a_string(True)


def test_a_number():
    assert is_that.a_number(42)
    assert is_that.a_number(42.0)
    assert is_that.a_number(42, 42)
    assert is_that.a_number(42.0, 42.0)
    assert is_that.a_number(42, 42.0)
    assert is_that.a_number(42, 42.0, 42j, 42)
    assert not is_that.a_number(True)
    assert not is_that.a_number(1, True, 1j)
    assert not is_that.a_number(42, 42.0, "test", 42, 42)


def test_an_int():
    assert is_that.an_int(42)
    assert is_that.an_int(42, 42)
    assert not is_that.an_int(True)
    assert not is_that.an_int(42, 42.0)
    assert not is_that.an_int(42.0, 42)
    assert not is_that.an_int(42, 42.0, 42, 42)
    assert not is_that.an_int(42, 42.0, "test", 42, 42)


def test_a_float():
    assert is_that.a_float(42.0)
    assert is_that.a_float(42.0, 42.0)
    assert not is_that.a_float(42, 42.0)
    assert not is_that.a_float(42.0, 42)
    assert not is_that.a_float(42, 42.0, 42, 42)
    assert not is_that.a_float(42, 42.0, "test", 42, 42)


def test_a_complex():
    assert is_that.a_complex(42j)
    assert is_that.a_complex(42j, 42 + 4j)
    assert not is_that.a_complex(42, 42.0)
    assert not is_that.a_complex(42.0, 42)
    assert not is_that.a_complex(42, 42.0, 42, 42)
    assert not is_that.a_complex(42, 42.0, "test", 42, 42)


def test_a_bytes():
    assert is_that.a_bytes(b"test")
    assert is_that.a_bytes(b"test", b"test")
    assert not is_that.a_bytes(b"test", "test")
    assert not is_that.a_bytes("test", b"test")
    assert not is_that.a_bytes("test", "test")
    assert not is_that.a_bytes(b"test", 1)


def test_a_bytearray():
    assert is_that.a_bytearray(bytearray("test", "utf-8"))
    assert is_that.a_bytearray(bytearray(b"test"))
    assert is_that.a_bytearray(bytearray([0, 1, 2]), bytearray(True), bytearray(b"test"))
    assert not is_that.a_bytearray(bytearray(b"test"), b"test", "test")
    assert not is_that.a_bytearray("test", bytearray(b"test"))
    assert not is_that.a_bytearray("test", "test")
    assert not is_that.a_bytearray(bytearray(b"test"), 1)


def test_a_tuple():
    assert is_that.a_tuple((0, "test", 1))
    assert is_that.a_tuple(("test",), (0, "test"), (True, False))
    assert not is_that.a_tuple("test", True)
    assert not is_that.a_tuple(("test",), 0, 1)
    assert not is_that.a_tuple(0, (1,))
    assert not is_that.a_tuple("test", 1)


def test_a_set():
    assert is_that.a_set(set())
    assert is_that.a_set({"test"})
    assert is_that.a_set({"test", "test1", 0, 1})
    assert is_that.a_set({"test"}, {"test1"}, {"test2"}, {"test3"})
    assert not is_that.a_set({"test"}, ["test1"], ["test2"], "test3")
    assert not is_that.a_set("")
    assert not is_that.a_set(True)
    assert not is_that.a_set(False)
    assert not is_that.a_set(0)
    assert not is_that.a_set(0.0)


def test_a_dict():
    assert is_that.a_dict({})
    assert is_that.a_dict({"test": 1})
    assert is_that.a_dict({"test": True, "test1": False, "test2": 0, "test3": 1})
    assert is_that.a_dict({"test": 0}, {"test1": 1}, {"test2": 2}, {"test3": 3})
    assert not is_that.a_dict({"test"}, ["test1"], ["test2"], "test3")
    assert not is_that.a_dict("")
    assert not is_that.a_dict(True)
    assert not is_that.a_dict(False)
    assert not is_that.a_dict(0)
    assert not is_that.a_dict(0.0)


def test_a_frozenset():
    assert is_that.a_frozenset(frozenset({}))
    assert is_that.a_frozenset(frozenset({"test": 1}))
    assert is_that.a_frozenset(frozenset({"test": True, "test1": False, "test2": 0, "test3": 1}))
    assert is_that.a_frozenset(frozenset({"test": 0}), frozenset({"test1"}), frozenset(["test2", 2]))
    assert is_that.a_frozenset(frozenset(["test"]), frozenset(["test1"]), frozenset(["test2"]), frozenset(["test3"]))
    assert is_that.a_frozenset(frozenset(["test"]), frozenset(["test1"]), frozenset(["test2"]), frozenset(["test3"]))
    assert not is_that.a_frozenset(["test"], ["test1"], ["test2"], ["test3"])
    assert not is_that.a_frozenset({"test"}, ["test1"], ["test2"], "test3")
    assert not is_that.a_frozenset("")
    assert not is_that.a_frozenset(True)
    assert not is_that.a_frozenset(False)
    assert not is_that.a_frozenset(0)
    assert not is_that.a_frozenset(0.0)


def test_a_range():
    assert is_that.a_range(range(0, 42))
    assert is_that.a_range(range(0, 42), range(0, 42))
    assert not is_that.a_range(range(0, 42), ["test1"], ["test2"], "test3")
    assert not is_that.a_range("")
    assert not is_that.a_range(True)
    assert not is_that.a_range(False)
    assert not is_that.a_range(0)
    assert not is_that.a_range(0.0)


def test_a_memoryview():
    assert is_that.a_memoryview(memoryview(bytearray([0, 1, 2])))
    assert is_that.a_memoryview(memoryview(bytearray(True)), memoryview(bytearray("test", "utf-8")))
    assert is_that.a_memoryview(memoryview(bytearray(b"test")), memoryview(bytearray(False)))
    assert not is_that.a_memoryview(bytearray(b"test"))
    assert not is_that.a_memoryview(bytearray("test", "utf-8"))
    assert not is_that.a_memoryview(True)
    assert not is_that.a_memoryview(True, "test", 0)
    assert not is_that.a_memoryview(True, False, 0, 1)


def test_a_date():
    assert is_that.a_date(datetime.date.today())
    assert is_that.a_date(datetime.date.today(), datetime.date(1970, 1, 1))
    assert is_that.a_date(datetime.date.fromtimestamp(0))
    assert not is_that.a_date(datetime.date.today(), datetime.datetime.now())
    assert not is_that.a_date(datetime.datetime.today(), datetime.date.today())
    assert not is_that.a_date(datetime.datetime.now())
    assert not is_that.a_date(0)
    assert not is_that.a_date("test")
    assert not is_that.a_date(True)


def test_a_datetime():
    assert is_that.a_datetime(datetime.datetime.now())
    assert is_that.a_datetime(datetime.datetime.today(), datetime.datetime.now())
    assert is_that.a_datetime(datetime.datetime.fromtimestamp(0))
    assert not is_that.a_datetime(datetime.date.today(), datetime.datetime.now())
    assert not is_that.a_datetime(datetime.datetime.today(), datetime.date.today())
    assert not is_that.a_datetime(datetime.date.today())
    assert not is_that.a_datetime(0)
    assert not is_that.a_datetime("test")
    assert not is_that.a_datetime(True)


def test_a_time():
    assert is_that.a_time(datetime.time())
    assert is_that.a_time(datetime.time(0, 1, 2))
    assert is_that.a_time(datetime.time(0), datetime.time(0, 1))
    assert not is_that.a_time(datetime.date.today(), datetime.datetime.now())
    assert not is_that.a_time(datetime.datetime.today(), datetime.date.today())
    assert not is_that.a_time(datetime.date.today())
    assert not is_that.a_time(0)
    assert not is_that.a_time("test")
    assert not is_that.a_time(True)


def test_a_timedelta():
    assert is_that.a_timedelta(datetime.timedelta())
    assert is_that.a_timedelta(datetime.timedelta(0))
    assert is_that.a_timedelta(datetime.timedelta(seconds=42), datetime.timedelta(minutes=42))
    assert not is_that.a_timedelta(datetime.time())
    assert not is_that.a_timedelta(datetime.time(0, 1, 2))
    assert not is_that.a_timedelta(datetime.time(0), datetime.time(0, 1))
    assert not is_that.a_timedelta(datetime.date.today(), datetime.datetime.now())
    assert not is_that.a_timedelta(datetime.datetime.today(), datetime.date.today())
    assert not is_that.a_timedelta(datetime.date.today())
    assert not is_that.a_timedelta(0)
    assert not is_that.a_timedelta("test")
    assert not is_that.a_timedelta(True)


def test_a_timezone():
    assert is_that.a_timezone(datetime.timezone(datetime.timedelta()))
    assert is_that.a_timezone(datetime.timezone(offset=datetime.timedelta()), datetime.timezone(datetime.timedelta()))
    assert not is_that.a_timezone(datetime.timedelta())
    assert not is_that.a_timezone(datetime.timedelta(0))
    assert not is_that.a_timezone(datetime.timedelta(seconds=42), datetime.timedelta(minutes=42))
    assert not is_that.a_timezone(datetime.time())
    assert not is_that.a_timezone(datetime.time(0, 1, 2))
    assert not is_that.a_timezone(datetime.time(0), datetime.time(0, 1))
    assert not is_that.a_timezone(datetime.date.today(), datetime.datetime.now())
    assert not is_that.a_timezone(datetime.datetime.today(), datetime.date.today())
    assert not is_that.a_timezone(datetime.date.today())
    assert not is_that.a_timezone(0)
    assert not is_that.a_timezone("test")
    assert not is_that.a_timezone(True)


def test_a_function():
    # TODO: FILL ME IN!
    pass


def test_an_exception():
    assert is_that.an_exception(Exception())
    assert is_that.an_exception(Exception(), Exception())
    assert not is_that.an_exception(Exception(), 0)
    assert not is_that.an_exception(Exception(), True)
    assert not is_that.an_exception(True)
    assert not is_that.an_exception("test")


def test_true():
    assert is_that.true(0 == 0)
    assert is_that.true(0 == 0, True, 0 != 1)
    assert is_that.true(True)
    assert not is_that.true(False)
    assert not is_that.true(0 == 1)
    assert not is_that.true(0)
    assert not is_that.true("test")


def test_false():
    assert is_that.false(0 != 0)
    assert is_that.false(0 != 0, False, 0 == 1)
    assert is_that.false(False)
    assert not is_that.false(True)
    assert not is_that.false(0 == 0)
    assert not is_that.false(0)
    assert not is_that.false("test")


def test_none():
    assert is_that.none(None)
    assert is_that.none(None, None)
    assert is_that.none(None, None, None)
    assert not is_that.none(None, 0, None)
    assert not is_that.none(True)
    assert not is_that.none(0 == 0)
    assert not is_that.none(0)
    assert not is_that.none("test")


def test_same_type():
    assert is_that.same_type(0)
    assert is_that.same_type(0, 0)
    assert is_that.same_type(True, False)
    assert not is_that.same_type(0, False)
    assert not is_that.same_type("test", False)


def test_equal():
    assert is_that.equal(0)
    assert is_that.equal(0, 0)
    assert is_that.equal(True, True)
    assert not is_that.equal(True, False)
    assert not is_that.equal(0, False)
    assert not is_that.equal("test", False)


def test_even():
    assert is_that.even(0)
    assert is_that.even(0, 0.0, 2, 4)
    assert is_that.even(2)
    assert is_that.even(2.0)
    assert is_that.even(-2)
    assert is_that.even(-2, 0, 2, -42.0, 42.0)
    assert not is_that.even(1)
    assert not is_that.even(2.0000000001)
    assert not is_that.even(2, 2.0000000001, 2)
    assert not is_that.even(2, True)
    assert not is_that.even(True)
    assert not is_that.even(False)
    assert not is_that.even(2, [])


def test_odd():
    assert is_that.odd(1)
    assert is_that.odd(1, 1.0, 3, 5)
    assert is_that.odd(3)
    assert is_that.odd(3.0)
    assert is_that.odd(-3)
    assert is_that.odd(-3, 1, 3, -1.0, 1.0)
    assert not is_that.odd(2)
    assert not is_that.odd(3.0000000001)
    assert not is_that.odd(3, 3.0000000001, 3)
    assert not is_that.odd(3, True)
    assert not is_that.odd(True)
    assert not is_that.odd(False)
    assert not is_that.odd(3, [])


def test_whole_number():
    assert is_that.whole_number(0)
    assert is_that.whole_number(0, 1, 2, 3)
    assert is_that.whole_number(1)
    assert is_that.whole_number(1, -1, -3)
    assert is_that.whole_number(-1)
    assert is_that.whole_number(-1, 0, -1.000)
    assert is_that.whole_number(1.0)
    assert not is_that.whole_number(1.1)
    assert not is_that.whole_number(1, 1.1, 2)
    assert not is_that.whole_number("", 1.1, -2)


def test_positive():
    assert is_that.positive(1)
    assert is_that.positive(1, 2)
    assert is_that.positive(1, 1.0)
    assert is_that.positive(1, 2.0, 3)
    assert not is_that.positive("1")
    assert not is_that.positive(0)
    assert not is_that.positive(0, 1)
    assert not is_that.positive(0, -1)
    assert not is_that.positive(0, 0.0, 0, 0.1)
    assert not is_that.positive(0, 0.0, 0, -0.1)
    assert not is_that.positive(0, "0.0", 0, 0.0)


def test_negative():
    assert is_that.negative(-1)
    assert is_that.negative(-1, -2)
    assert is_that.negative(-1, -1.0)
    assert is_that.negative(-1, -2.0, -3)
    assert not is_that.negative("-1")
    assert not is_that.negative(0)
    assert not is_that.negative(0, 1)
    assert not is_that.negative(0, -1)
    assert not is_that.negative(0, 0.0, 0, 0.1)
    assert not is_that.negative(0, 0.0, 0, -0.1)
    assert not is_that.negative(0, "0.0", 0, 0.0)


def test_zero():
    assert is_that.zero(0)
    assert is_that.zero(0, 0)
    assert is_that.zero(0, 0.0)
    assert is_that.zero(0, 0.0, 0)
    assert not is_that.zero("0")
    assert not is_that.zero(1)
    assert not is_that.zero(0, 1)
    assert not is_that.zero(0, 0.0, 0, 0.1)
    assert not is_that.zero(0, "0.0", 0, 0.0)


def test_under():
    assert is_that.under(0, 1)
    assert is_that.under(-1, 0)
    assert is_that.under(0, 0.1)
    assert is_that.under(-2, 4)
    assert not is_that.under("0", 1)
    assert not is_that.under(1, "2")
    assert not is_that.under(0, -1)
    assert not is_that.under(0, 0.0)
    assert not is_that.under(0, "1.0")


def test_under_or_equal():
    assert is_that.under_or_equal(0, 0)
    assert is_that.under_or_equal(0, 1)
    assert is_that.under_or_equal(-1, 0)
    assert is_that.under_or_equal(0, 0.1)
    assert is_that.under_or_equal(-2, 4)
    assert not is_that.under_or_equal("0", 0)
    assert not is_that.under_or_equal("0", 1)
    assert not is_that.under_or_equal(1, "2")
    assert not is_that.under_or_equal(0, -1)
    assert not is_that.under_or_equal(0.1, 0.0)
    assert not is_that.under_or_equal(0, "1.0")


def test_over():
    assert is_that.over(1, 0)
    assert is_that.over(1, 0)
    assert is_that.over(0, -1)
    assert is_that.over(0.1, 0)
    assert is_that.over(4, -2)
    assert not is_that.over("0", 0)
    assert not is_that.over("1", 0)
    assert not is_that.over(2, "1")
    assert not is_that.over(0, 0)
    assert not is_that.over(0, 0.0)
    assert not is_that.over(0, "1.0")


def test_over_or_equal():
    assert is_that.over_or_equal(1, 0)
    assert is_that.over_or_equal(0, 0)
    assert is_that.over_or_equal(1, 0)
    assert is_that.over_or_equal(0, -1)
    assert is_that.over_or_equal(0.1, 0)
    assert is_that.over_or_equal(4, -2)
    assert not is_that.over_or_equal("0", 0)
    assert not is_that.over_or_equal("1", 0)
    assert not is_that.over_or_equal(2, "1")
    assert not is_that.over_or_equal(0, 1)
    assert not is_that.over_or_equal(0, 0.1)
    assert not is_that.over_or_equal(0, "1.0")


def test_between():
    assert is_that.between(1, 0, 2)
    assert is_that.between(1, 0, 2)
    assert is_that.between(0, -1, 1)
    assert is_that.between(0.1, 0, 0.2)
    assert is_that.between(4, -2, 42)
    assert not is_that.between("0", 0, 1)
    assert not is_that.between("1", 0, 0)
    assert not is_that.between(2, 2, 2)
    assert not is_that.between(0, 0, 1)
    assert not is_that.between(0, 0.0, 1.0)
    assert not is_that.between(0, "1.0", "test")


def test_between_or_equal():
    assert is_that.between_or_equal(1, 0, 2)
    assert is_that.between_or_equal(1, 0, 2)
    assert is_that.between_or_equal(1, 1, 2)
    assert is_that.between_or_equal(2, 1, 2)
    assert is_that.between_or_equal(2, 2, 2)
    assert is_that.between_or_equal(0, -1, 1)
    assert is_that.between_or_equal(0.1, 0, 0.2)
    assert is_that.between_or_equal(4, -2, 42)
    assert not is_that.between_or_equal("0", 0, 1)
    assert not is_that.between_or_equal("1", 0, 0)
    assert not is_that.between_or_equal(0, 1, 1)
    assert not is_that.between_or_equal(-0.1, 0.0, 1.0)
    assert not is_that.between_or_equal(0, "1.0", "test")


def test_multiple_of():
    assert is_that.multiple_of(1, 1)
    assert is_that.multiple_of(2, 1)
    assert is_that.multiple_of(42, 2)
    assert is_that.multiple_of(420, 20)
    assert not is_that.multiple_of(2, 0)
    assert not is_that.multiple_of(1, 2)
    assert not is_that.multiple_of(1, 3)


def test_empty():
    assert is_that.empty([])
    assert is_that.empty([], [])
    assert is_that.empty({})
    assert is_that.empty([], {}, set())
    assert is_that.empty(list())
    assert is_that.empty(dict())
    assert is_that.empty(set())
    assert not is_that.empty(0)
    assert not is_that.empty(0, [])
    assert not is_that.empty([], {"test": "test"}, {42})
    assert not is_that.empty(["test"])
    assert not is_that.empty({"test": "test"})
    assert not is_that.empty({"test"})


def test_file_exists():
    assert is_that.file_exists("is_that.py")
    assert is_that.file_exists("is_that.py", "is_that.py")
    assert is_that.file_exists("is_that.py", "README.md", "LICENSE")
    assert not is_that.file_exists("test")
    assert not is_that.file_exists("test", "is_that.py")
    assert not is_that.file_exists(0, "is_that.py")
    assert not is_that.file_exists("is_that.py", "test")
    assert not is_that.file_exists("is_that.py", [])
    assert not is_that.file_exists(0, 1)


def test_palindrome():
    assert is_that.palindrome("")
    assert is_that.palindrome("a")
    assert is_that.palindrome("a", "")
    assert is_that.palindrome("anna")
    assert is_that.palindrome("anna", "civic", "kayak")
    assert not is_that.palindrome("test")
    assert not is_that.palindrome("test", "anna")


def test_uppercase():
    assert is_that.uppercase("TEST")
    assert is_that.uppercase("TEST", "TEST")
    assert not is_that.uppercase("test")
    assert not is_that.uppercase("TEST", "test")
    assert not is_that.uppercase("test", "TEST")
    assert not is_that.uppercase(True, "TEST")
    assert not is_that.uppercase("42", "TEST")


def test_lowercase():
    # TODO: FILL ME IN!
    pass


def test_titlecase():
    # TODO: FILL ME IN!
    pass


def test_contains():
    # TODO: FILL ME IN!
    pass


def test_begins_with():
    # TODO: FILL ME IN!
    pass


def test_ends_with():
    # TODO: FILL ME IN!
    pass


def test_alphanumeric():
    # TODO: FILL ME IN!
    pass


def test_email():
    assert is_that.email("test@test.com")
    assert is_that.email("TEST@test.com")
    assert is_that.email("TEST@TEST.com")
    assert is_that.email("TEST@TEST.COM")
    assert is_that.email("TeSt@TeSt.CoM")


def test_btc_address():
    # TODO: FILL ME IN!
    pass


def test_credit_card():
    # TODO: FILL ME IN!
    pass


def test_ipv4():
    # TODO: FILL ME IN!
    pass


def test_ipv6():
    # TODO: FILL ME IN!
    pass


def test_ip():
    # TODO: FILL ME IN!
    pass


def test_hex_color():
    # TODO: FILL ME IN!
    pass


def test_social_security_number():
    # TODO: FILL ME IN!
    pass


def test_url():
    # TODO: FILL ME IN!
    pass


def test_us_zip_code():
    # TODO: FILL ME IN!
    pass


def test_future():
    # TODO: FILL ME IN!
    pass


def test_past():
    # TODO: FILL ME IN!
    pass


def test_in_date_range():
    # TODO: FILL ME IN!
    pass


def test_today():
    # TODO: FILL ME IN!
    pass


def test_yesterday():
    # TODO: FILL ME IN!
    pass


def test_last_week():
    # TODO: FILL ME IN!
    pass


def test_last_month():
    # TODO: FILL ME IN!
    pass


def test_last_quarter():
    # TODO: FILL ME IN!
    pass


def test_last_year():
    # TODO: FILL ME IN!
    pass


def test_tomorrow():
    # TODO: FILL ME IN!
    pass


def test_next_week():
    # TODO: FILL ME IN!
    pass


def test_next_month():
    # TODO: FILL ME IN!
    pass


def test_next_quarter():
    # TODO: FILL ME IN!
    pass


def test_next_year():
    # TODO: FILL ME IN!
    pass


def test_leap_year():
    # TODO: FILL ME IN!
    pass


def test_weekday():
    # TODO: FILL ME IN!
    pass


def test_weekend():
    # TODO: FILL ME IN!
    pass
