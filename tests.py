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
    # TODO: FILL ME IN!
    pass


def test_a_date():
    # TODO: FILL ME IN!
    pass


def test_a_datetime():
    # TODO: FILL ME IN!
    pass


def test_a_time():
    # TODO: FILL ME IN!
    pass


def test_a_timedelta():
    # TODO: FILL ME IN!
    pass


def test_a_tzinfo():
    # TODO: FILL ME IN!
    pass


def test_a_function():
    # TODO: FILL ME IN!
    pass


def test_true():
    # TODO: FILL ME IN!
    pass


def test_false():
    # TODO: FILL ME IN!
    pass


def test_none():
    # TODO: FILL ME IN!
    pass


def test_same_type():
    # TODO: FILL ME IN!
    pass


def test_equal():
    # TODO: FILL ME IN!
    pass


def test_even():
    assert is_that.even(0)
    assert is_that.even(2)
    assert is_that.even(2.0)
    assert is_that.even(-2)
    assert not is_that.even(1)
    assert not is_that.even(2.0000000001)
    assert not is_that.even(True)
    assert not is_that.even(False)
    assert not is_that.even([])


def test_odd():
    assert is_that.odd(1)
    assert is_that.odd(3)
    assert is_that.odd(3.0)
    assert is_that.odd(-3)
    assert not is_that.odd(0)
    assert not is_that.odd(2)
    assert not is_that.odd(3.0000000001)
    assert not is_that.odd(True)
    assert not is_that.odd([])


def test_whole_number():
    assert is_that.whole_number(0)
    assert is_that.whole_number(1)
    assert is_that.whole_number(-1)
    assert is_that.whole_number(1.0)
    assert not is_that.whole_number(1.1)
    assert not is_that.whole_number("")


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
    # TODO: FILL ME IN!
    pass


def test_under_or_equal():
    # TODO: FILL ME IN!
    pass


def test_over():
    # TODO: FILL ME IN!
    pass


def test_over_or_equal():
    # TODO: FILL ME IN!
    pass


def test_between():
    # TODO: FILL ME IN!
    pass


def test_between_or_equal():
    # TODO: FILL ME IN!
    pass


def test_multiple_of():
    assert is_that.multiple_of(1, 1)
    assert is_that.multiple_of(2, 1)
    assert is_that.multiple_of(450, 10)
    assert not is_that.multiple_of(2, 0)


def test_empty():
    assert is_that.empty([])
    assert is_that.empty({})
    assert is_that.empty(list())
    assert is_that.empty(dict())
    assert is_that.empty(set())
    assert not is_that.empty(["test"])
    assert not is_that.empty({"test": "test"})
    assert not is_that.empty({"test"})


def test_file_exists():
    # TODO: FILL ME IN!
    pass


def test_palindrome():
    # TODO: FILL ME IN!
    pass


def test_uppercase():
    # TODO: FILL ME IN!
    pass


def test_lowercase():
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
