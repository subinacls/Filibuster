#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Released into the public domain.

""":synopsis: Deals with a lot of cross-version issues.
:module: mom._compat

Should not be used in public code. Use the wrappers in mom.
"""

# DO NOT REMOVE THIS LINE.
from __future__ import absolute_import

import os
import struct
import sys


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"

try:
	INT_MAX = sys.maxsize
except AttributeError:
	INT_MAX = sys.maxint

INT64_MAX = (1 << 63) - 1
INT32_MAX = (1 << 31) - 1
INT16_MAX = (1 << 15) - 1
UINT128_MAX = (1 << 128) - 1    # 340282366920938463463374607431768211455L
UINT64_MAX = 0xffffffffffffffff  # ((1 << 64) - 1)
UINT32_MAX = 0xffffffff  # ((1 << 32) - 1)
UINT16_MAX = 0xffff  # ((1 << 16) - 1)
UINT8_MAX = 0xff


# Determine the word size of the processor.
if INT_MAX == INT64_MAX:
	# 64-bit processor.
	MACHINE_WORD_SIZE = 64
	UINT_MAX = UINT64_MAX
elif INT_MAX == INT32_MAX:
	# 32-bit processor.
	MACHINE_WORD_SIZE = 32
	UINT_MAX = UINT32_MAX
else:
	# Else we just assume 64-bit processor keeping up with modern times.
	MACHINE_WORD_SIZE = 64
	UINT_MAX = UINT64_MAX

try:
	LONG_TYPE = long
except NameError:
	LONG_TYPE = int


# They fucking removed long too!
try:
	INT_TYPE = long
	INTEGER_TYPES = (int, long)
except NameError:
	INT_TYPE = int
	INTEGER_TYPES = (int,)

try:
	# Python 2.6 or higher.
	BYTES_TYPE = bytes
except NameError:
	# Python 2.5
	BYTES_TYPE = str

try:
	# Not Python3
	UNICODE_TYPE = unicode
	BASESTRING_TYPE = basestring
	HAVE_PYTHON3 = False

	def byte_ord(byte_):

		return ord(byte_)
except NameError:

	# Python3.
	def byte_ord(byte_):

		return byte_

	UNICODE_TYPE = str
	BASESTRING_TYPE = (str, bytes)
	HAVE_PYTHON3 = True

# Integral range.
try:
	# Python 2.5+
	xrange(0)
	range = xrange
except NameError:
	range = range

# Fake byte literals for python2.5
if str is UNICODE_TYPE:

	def byte_literal(literal):

		return literal.encode("latin1")
else:

	def byte_literal(literal):

		return literal

ZERO_BYTE = byte_literal("\x00")
EMPTY_BYTE = byte_literal("")
EQUAL_BYTE = byte_literal("=")
PLUS_BYTE = byte_literal("+")
HYPHEN_BYTE = byte_literal("-")
FORWARD_SLASH_BYTE = byte_literal("/")
UNDERSCORE_BYTE = byte_literal("_")
DIGIT_ZERO_BYTE = byte_literal("0")

HAVE_LITTLE_ENDIAN = bool(struct.pack("h", 1) == "\x01\x00")

try:
	# Check whether we have reduce as a built-in.
	__reduce_test__ = reduce((lambda num1, num2: num1 + num2), [1, 2, 3, 4])
except NameError:
	# Python 3k
	from functools import reduce
reduce = reduce

try:
	# Python 2.x
	from itertools import imap as map
except ImportError:
	# Python 3.x
	map = map

if getattr(dict, "iteritems", None):

	def dict_each(func, iterable):

		for key, value in iterable.iteritems():
			func(key, value)
else:

	def dict_each(func, iterable):

		for key, value in iterable.items():
			func(key, value)

try:
	next = next
except NameError:

	# Taken from
	# http://goo.gl/ZNDXN
	class Throw(object):
		"""Bleh."""
		pass

	throw = Throw()  # easy sentinel hack

	def next(iterator, default=throw):

		try:
			iternext = iterator.next.__call__

		except AttributeError:
			raise TypeError("%s object is not an iterator" % type(iterator).__name__)
		try:
			return iternext()
		except StopIteration:
			if default is throw:
				raise
			return default

try:
	# Operating system unsigned random.
	os.urandom(1)

	def generate_random_bytes(count):

		return os.urandom(count)
except AttributeError:
	try:
		__urandom_device__ = open("/dev/urandom", "rb")

		def generate_random_bytes(count):

			return __urandom_device__.read(count)
	except IOError:
		#Else get Win32 CryptoAPI PRNG
		try:
			import win32prng

			def generate_random_bytes(count):

				random_bytes = win32prng.generate_random_bytes(count)
				assert len(random_bytes) == count
				return random_bytes
		except ImportError:
			win32prng = None

			# What the fuck?!
			def generate_random_bytes(_):

				raise NotImplementedError("What the fuck?! No PRNG available.")


def get_word_alignment(num, force_arch=64,
                       _machine_word_size=MACHINE_WORD_SIZE):
	if force_arch == 64 and _machine_word_size >= 64 and num > UINT32_MAX:
		# 64-bit unsigned integer.
		return 64, 8, UINT64_MAX, "Q"
	elif num > UINT16_MAX:
		# 32-bit unsigned integer
		return 32, 4, UINT32_MAX, "L"
	elif num > UINT8_MAX:
		# 16-bit unsigned integer.
		return 16, 2, UINT16_MAX, "H"
	else:
		# 8-bit unsigned integer.
		return 8, 1, UINT8_MAX, "B"

