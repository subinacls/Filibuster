#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 Yesudeep Mangalapilly <yesudeep@gmail.com>
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


""":synopsis: ASCII-85 and RFC1924 Base85 encoding and decoding functions.
:module: mom.codec.base85
:see: http://en.wikipedia.org/wiki/Ascii85
:see: http://tools.ietf.org/html/rfc1924
:see: http://www.piclist.com/techref/method/encode.htm


Functions
---------
.. autofunction:: b85encode
.. autofunction:: b85decode
.. autofunction:: rfc1924_b85encode
.. autofunction:: rfc1924_b85decode
.. autofunction:: ipv6_b85encode
.. autofunction:: ipv6_b85decode
"""

from __future__ import absolute_import
from __future__ import division

# pylint: disable-msg=R0801
try:  #pragma: no cover
	import psyco

	psyco.full()
except ImportError:  #pragma: no cover
	psyco = None
# pylint: enable-msg=R0801

import array
import struct

import mom_compat
import mom_builtin
import mom_string


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"

__all__ = [
	"b85encode",
	"b85decode",
	"rfc1924_b85encode",
	"rfc1924_b85decode",
	"ASCII85_PREFIX",
	"ASCII85_SUFFIX",
	"ipv6_b85encode",
	"ipv6_b85decode",
]

b = mom_builtin.b
ZERO_BYTE = mom_compat.ZERO_BYTE
UINT128_MAX = mom_compat.UINT128_MAX
UINT32_MAX = mom_compat.UINT32_MAX
EMPTY_BYTE = mom_compat.EMPTY_BYTE

EXCLAMATION_CHUNK = b("!!!!!")
ZERO_GROUP_CHAR = b("z")

# Use this if you want the base85 codec to encode/decode including
# ASCII85 prefixes/suffixes.
ASCII85_PREFIX = b("<~")
ASCII85_SUFFIX = b("~>")

# ASCII85 characters.
ASCII85_BYTES = array.array("B", [(num + 33) for num in mom_builtin.range(85)])

RFC1924_BYTES = array.array("B", (mom_string.DIGITS +
                                  mom_string.ASCII_UPPERCASE +
                                  mom_string.ASCII_LOWERCASE +
                                  "!#$%&()*+-;<=>?@^_`{|}~").encode("ascii"))

if mom_compat.HAVE_PYTHON3:  # pragma: no cover
	# Python 3 bytes when indexed yield integers, not single-character
	# byte strings.
	ASCII85_ORDS = dict((x, x - 33) for x in ASCII85_BYTES)
	RFC1924_ORDS = dict((x, i) for i, x in enumerate(RFC1924_BYTES))
else:
	# Indexing into Python 2 bytes yields single-character byte strings.
	ASCII85_ORDS = dict((mom_builtin.byte(x), x - 33) for x in ASCII85_BYTES)
	RFC1924_ORDS = dict((mom_builtin.byte(x), i)
	                    for i, x in enumerate(RFC1924_BYTES))

POW_85 = (
	1,
	85,
	7225,
	614125,
	52200625,
	4437053125,
	377149515625,
	32057708828125,
	2724905250390625,
	231616946283203125,
	19687440434072265625, #L ->
	1673432436896142578125,
	142241757136172119140625,
	12090549356574630126953125,
	1027696695308843560791015625,
	87354219101251702667236328125,
	7425108623606394726715087890625,
	631134233006543551770782470703125,
	53646409805556201900516510009765625,
	4559944833472277161543903350830078125,
)


def _check_compact_char_occurrence(encoded, zero_char, chunk_size=5):
	counter = 0
	for i, char in enumerate(encoded):
		if char == zero_char[0]:
			if counter % chunk_size:
				raise ValueError("zero char `%r` occurs in the middle of a chunk "
				                 "at index %d" % (zero_char, i))
			else:
				counter = 0
		else:
			counter += 1


def _b85encode_chunks(raw_bytes,
                      base85_bytes,
                      padding=False,
                      pow_85=POW_85,
                      zero_byte=ZERO_BYTE):
	num_uint32, remainder = divmod(len(raw_bytes), 4)
	if remainder:

		padding_size = 4 - remainder
		raw_bytes += zero_byte * padding_size
		num_uint32 += 1
	else:
		padding_size = 0

	encoded = array.array("B", [0] * num_uint32 * 5)

	i = 0
	for uint32 in struct.unpack(">" + "L" * num_uint32, raw_bytes):
		encoded[i] = base85_bytes[uint32 // pow_85[4]]  # Don't need %85.is<85
		encoded[i + 1] = base85_bytes[(uint32 // pow_85[3]) % 85]
		encoded[i + 2] = base85_bytes[(uint32 // pow_85[2]) % 85]
		encoded[i + 3] = base85_bytes[(uint32 // 85) % 85]     # 85**1 = 85
		encoded[i + 4] = base85_bytes[uint32 % 85]             # 85**0 = 1
		i += 5

	if padding_size and not padding:
		# Only as much padding added before encoding is removed after encoding.
		encoded = encoded[:-padding_size]

	return encoded.tostring()


def _b85decode_chunks(encoded, base85_bytes, base85_ords):
	length = len(encoded)
	num_uint32s, remainder = divmod(length, 5)
	if remainder:
		padding_byte = mom_builtin.byte(base85_bytes[84])  # "u"(ASCII85);"~"(RFC1924)
		padding_size = 5 - remainder
		encoded += padding_byte * padding_size
		num_uint32s += 1
		length += padding_size
	else:
		padding_size = 0

	#uint32s = [0] * num_uint32s
	uint32s = array.array("I", [0] * num_uint32s)
	j = 0
	chunk = EMPTY_BYTE
	try:
		for i in mom_builtin.range(0, length, 5):
			chunk = encoded[i:i + 5]

			uint32_value = ((((base85_ords[chunk[0]] *
			                   85 + base85_ords[chunk[1]]) *
			                  85 + base85_ords[chunk[2]]) *
			                 85 + base85_ords[chunk[3]]) *
			                85 + base85_ords[chunk[4]])

			if uint32_value > UINT32_MAX:  # 2**32 - 1
				raise OverflowError("Cannot decode chunk `%r`" % chunk)

			uint32s[j] = uint32_value
			j += 1
	except KeyError:
		raise OverflowError("Cannot decode chunk `%r`" % chunk)

	raw_bytes = struct.pack(">" + "L" * num_uint32s, *uint32s)
	if padding_size:
		# Only as much padding added before decoding is removed after decoding.
		raw_bytes = raw_bytes[:-padding_size]
	return raw_bytes


def b85encode(raw_bytes,
              prefix=None,
              suffix=None,
              _base85_bytes=ASCII85_BYTES,
              _padding=False,
              _compact_zero=True,
              _compact_char=ZERO_GROUP_CHAR):
	prefix = prefix or EMPTY_BYTE
	suffix = suffix or EMPTY_BYTE
	if not (mom_builtin.is_bytes(prefix) and mom_builtin.is_bytes(suffix)):
		raise TypeError("Prefix/suffix must be bytes: got prefix %r, %r" %
		                (type(prefix).__name__, type(suffix).__name__))
	if not mom_builtin.is_bytes(_compact_char):
		raise TypeError("compat character must be raw byte: got %r" %
		                type(_compact_char).__name__)
	if not mom_builtin.is_bytes(raw_bytes):
		raise TypeError("data must be raw bytes: got %r" %
		                type(raw_bytes).__name__)

	# Encode into ASCII85 characters.
	encoded = _b85encode_chunks(raw_bytes, _base85_bytes, _padding)
	encoded = (encoded.replace(EXCLAMATION_CHUNK, _compact_char)
	           if _compact_zero else encoded)
	return prefix + encoded + suffix


def b85decode(encoded,
              prefix=None,
              suffix=None,
              _base85_bytes=ASCII85_BYTES,
              _base85_ords=ASCII85_ORDS,
              _uncompact_zero=True,
              _compact_char=ZERO_GROUP_CHAR):
	prefix = prefix or EMPTY_BYTE
	suffix = suffix or EMPTY_BYTE

	if not (mom_builtin.is_bytes(prefix) and mom_builtin.is_bytes(suffix)):
		raise TypeError("Prefix/suffix must be bytes: got prefix %r, %r" %
		                (type(prefix).__name__, type(suffix).__name__))
	if not mom_builtin.is_bytes(_compact_char):
		raise TypeError("compat character must be raw byte: got %r" %
		                type(_compact_char).__name__)
	if not mom_builtin.is_bytes(encoded):
		raise TypeError("Encoded sequence must be bytes: got %r" %
		                type(encoded).__name__)

	# ASCII-85 ignores whitespace.
	encoded = EMPTY_BYTE.join(encoded.split())

	# Strip the prefix and suffix.
	if prefix and encoded.startswith(prefix):
		encoded = encoded[len(prefix):]
	if suffix and encoded.endswith(suffix):
		encoded = encoded[:-len(suffix)]

	# Replace all the "z" occurrences with "!!!!!"
	if _uncompact_zero:
		_check_compact_char_occurrence(encoded, _compact_char)
		encoded = encoded.replace(_compact_char, EXCLAMATION_CHUNK)

	return _b85decode_chunks(encoded, _base85_bytes, _base85_ords)


def rfc1924_b85encode(raw_bytes,
                      _padding=False):
	if not mom_builtin.is_bytes(raw_bytes):
		raise TypeError("data must be raw bytes: got %r" %
		                type(raw_bytes).__name__)
	return _b85encode_chunks(raw_bytes, RFC1924_BYTES, _padding)


def rfc1924_b85decode(encoded):
	if not mom_builtin.is_bytes(encoded):
		raise TypeError("Encoded sequence must be bytes: got %r" %
		                type(encoded).__name__)
		# Ignore whitespace.
	encoded = EMPTY_BYTE.join(encoded.split())
	return _b85decode_chunks(encoded, RFC1924_BYTES, RFC1924_ORDS)


def ipv6_b85encode(uint128,
                   _base85_bytes=RFC1924_BYTES):
	if uint128 < 0:
		raise ValueError("Number is not a 128-bit unsigned integer: got %d" %
		                 uint128)
	if uint128 > UINT128_MAX:
		raise OverflowError("Number is not a 128-bit unsigned integer: %d" %
		                    uint128)

	return struct.pack("BBBBBBBBBBBBBBBBBBBB",
	                   _base85_bytes[(uint128 // POW_85[19])],
	                   # Don't need %85. Already < 85
	                   _base85_bytes[(uint128 // POW_85[18]) % 85],
	                   _base85_bytes[(uint128 // POW_85[17]) % 85],
	                   _base85_bytes[(uint128 // POW_85[16]) % 85],
	                   _base85_bytes[(uint128 // POW_85[15]) % 85],
	                   _base85_bytes[(uint128 // POW_85[14]) % 85],
	                   _base85_bytes[(uint128 // POW_85[13]) % 85],
	                   _base85_bytes[(uint128 // POW_85[12]) % 85],
	                   _base85_bytes[(uint128 // POW_85[11]) % 85],
	                   _base85_bytes[(uint128 // POW_85[10]) % 85],
	                   _base85_bytes[(uint128 // POW_85[9]) % 85],
	                   _base85_bytes[(uint128 // POW_85[8]) % 85],
	                   _base85_bytes[(uint128 // POW_85[7]) % 85],
	                   _base85_bytes[(uint128 // POW_85[6]) % 85],
	                   _base85_bytes[(uint128 // POW_85[5]) % 85],
	                   _base85_bytes[(uint128 // POW_85[4]) % 85],
	                   _base85_bytes[(uint128 // POW_85[3]) % 85],
	                   _base85_bytes[(uint128 // POW_85[2]) % 85],
	                   _base85_bytes[(uint128 // 85) % 85], # 85**1 == 85
	                   _base85_bytes[uint128 % 85], # 85**0 == 1
	)


def ipv6_b85decode(encoded,
                   _base85_ords=RFC1924_ORDS):
	if not mom_builtin.is_bytes(encoded):
		raise TypeError("Encoded sequence must be bytes: got %r" %
		                type(encoded).__name__)

	# Ignore whitespace.
	encoded = EMPTY_BYTE.join(encoded.split())

	if len(encoded) != 20:
		raise ValueError("Not 20 encoded bytes: %r" % encoded)

	try:
		#v, w, x, y, z = encoded[0:5]
		# v = encoded[0]..z = encoded[4]
		uint128 = ((((_base85_ords[encoded[0]] *
		              85 + _base85_ords[encoded[1]]) *
		             85 + _base85_ords[encoded[2]]) *
		            85 + _base85_ords[encoded[3]]) *
		           85 + _base85_ords[encoded[4]])

		uint128 = (((((uint128 * 85 + _base85_ords[encoded[5]]) *
		              85 + _base85_ords[encoded[6]]) *
		             85 + _base85_ords[encoded[7]]) *
		            85 + _base85_ords[encoded[8]]) *
		           85 + _base85_ords[encoded[9]])

		uint128 = (((((uint128 * 85 + _base85_ords[encoded[10]]) *
		              85 + _base85_ords[encoded[11]]) *
		             85 + _base85_ords[encoded[12]]) *
		            85 + _base85_ords[encoded[13]]) *
		           85 + _base85_ords[encoded[14]])

		uint128 = (((((uint128 * 85 + _base85_ords[encoded[15]]) *
		              85 + _base85_ords[encoded[16]]) *
		             85 + _base85_ords[encoded[17]]) *
		            85 + _base85_ords[encoded[18]]) *
		           85 + _base85_ords[encoded[19]])
	except KeyError:
		raise OverflowError("Cannot decode `%r -- may contain stray "
		                    "ASCII bytes" % encoded)

	if uint128 > UINT128_MAX:
		raise OverflowError("Cannot decode `%r` -- may contain stray "
		                    "ASCII bytes" % encoded)
	return uint128

