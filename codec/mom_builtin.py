#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":synopsis: Deals with a lot of cross-version issues.
:module: mom.builtins

Encodings
---------
.. autofunction:: bin
.. autofunction:: hex
.. autofunction:: byte
.. autofunction:: byte_ord


Bits and bytes size counting
----------------------------
.. autofunction:: bytes_leading
.. autofunction:: bytes_trailing
.. autofunction:: integer_bit_length
.. autofunction:: integer_bit_size
.. autofunction:: integer_byte_length
.. autofunction:: integer_byte_size

Type detection predicates
-------------------------
.. autofunction:: is_bytes
.. autofunction:: is_bytes_or_unicode
.. autofunction:: is_integer
.. autofunction:: is_sequence
.. autofunction:: is_unicode

Number predicates
-----------------
People screw these up too. Useful in functional programming.

.. autofunction:: is_even
.. autofunction:: is_negative
.. autofunction:: is_odd
.. autofunction:: is_positive

"""

from __future__ import absolute_import

# pylint: disable-msg=R0801
import mom_compat

try:  # pragma: no cover
	import psyco

	psyco.full()
except ImportError:  # pragma: no cover
	psyco = None
# pylint: enable-msg=R0801

import struct


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"

__all__ = [
	"byte",
	"byte_ord",
	"bytes",
	"bytes_leading",
	"bytes_trailing",
	"bin",
	"hex",
	"integer_byte_length",
	"integer_byte_size",
	"integer_bit_length",
	"is_sequence",
	"is_unicode",
	"is_bytes",
	"is_bytes_or_unicode",
	"is_integer",
	"is_even",
	"is_negative",
	"is_odd",
	"is_positive",
]


# Integral range
range = mom_compat.range
map = mom_compat.map
reduce = mom_compat.reduce
next = mom_compat.next
bytes = mom_compat.BYTES_TYPE

# Fake byte literal support.
b = mom_compat.byte_literal

byte_ord = mom_compat.byte_ord

dict_each = mom_compat.dict_each


def byte(number):
	return struct.pack("B", number)


def bytes_leading(raw_bytes, needle=mom_compat.ZERO_BYTE):
	if not is_bytes(raw_bytes):
		raise TypeError("argument must be raw bytes: got %r" %
		                type(raw_bytes).__name__)
	leading = 0
	# Indexing keeps compatibility between Python 2.x and Python 3.x
	needle_byte = needle[0]
	for raw_byte in raw_bytes:
		if raw_byte == needle_byte:
			leading += 1
		else:
			break
	return leading


def bytes_trailing(raw_bytes, needle=mom_compat.ZERO_BYTE):
	if not is_bytes(raw_bytes):
		raise TypeError("argument must be raw bytes: got %r" %
		                type(raw_bytes).__name__)
	trailing = 0
	# Indexing keeps compatibility between Python 2.x and Python 3.x
	needle_byte = needle[0]
	for raw_byte in reversed(raw_bytes):
		if raw_byte == needle_byte:
			trailing += 1
		else:
			break
	return trailing


def bin(number, prefix="0b"):
	if number is None:
		raise TypeError("'%r' object cannot be interpreted as an index" %
		                type(number).__name__)
	prefix = prefix or ""
	if number < 0:
		number = -number
		prefix = "-" + prefix
	bit_string = ""
	while number > 1:
		bit_string = str(number & 1) + bit_string
		number >>= 1
	bit_string = str(number) + bit_string
	return prefix + bit_string


def hex(number, prefix="0x"):
	prefix = prefix or ""
	if number < 0:
		number = -number
		prefix = "-" + prefix

	# Make sure this is an int and not float.
	_ = number & 1

	hex_num = "%x" % number
	return prefix + hex_num.lower()


def is_sequence(obj):
	try:
		list(obj)
		return True
	except TypeError:  #, exception:
		#assert "is not iterable" in bytes(exception)
		return False


def is_unicode(obj):
	return isinstance(obj, mom_compat.UNICODE_TYPE)


def is_bytes(obj):
	return isinstance(obj, mom_compat.BYTES_TYPE)


def is_bytes_or_unicode(obj):
	return isinstance(obj, mom_compat.BASESTRING_TYPE)


def is_integer(obj):
	return isinstance(obj, mom_compat.INTEGER_TYPES) and not isinstance(obj, bool)


def integer_byte_length(number):
	quanta, remainder = divmod(integer_bit_length(number), 8)
	if remainder:
		quanta += 1
	return quanta


def integer_byte_size(number):
	quanta, remainder = divmod(integer_bit_length(number), 8)
	if remainder or number == 0:
		quanta += 1
	return quanta


def integer_bit_length(number):
	if number == 0:
		return 0
	if number < 0:
		number = -number
		# Make sure this is an int and not float.
	_ = number & 1
	hex_num = "%x" % number
	return ((len(hex_num) - 1) * 4) + {
		"0": 0, "1": 1, "2": 2, "3": 2,
		"4": 3, "5": 3, "6": 3, "7": 3,
		"8": 4, "9": 4, "a": 4, "b": 4,
		"c": 4, "d": 4, "e": 4, "f": 4,
	}[hex_num[0]]
	#return int(math.floor(math.log(n, 2))+1)


def integer_bit_size(number):
	if number == 0:
		return 1
	return integer_bit_length(number)


def integer_bit_count(number):
	number = abs(number)
	count = 0
	while number:
		number &= number - 1
		count += 1
	return count


def is_even(num):
	return not (num & 1)


def is_odd(num):
	return bool(num & 1)


def is_positive(num):
	if not isinstance(num, mom_compat.INTEGER_TYPES + (bool, float)):
		raise TypeError("unsupported operand type: %r", type(num).__name__)
	return num > 0


def is_negative(num):
	if not isinstance(num, mom_compat.INTEGER_TYPES + (bool, float)):
		raise TypeError("unsupported operand type: %r", type(num).__name__)
	return num < 0
