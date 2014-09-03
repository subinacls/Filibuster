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

""":synopsis: Routines for converting between integers and bytes.
:module: mom.codec.integer

Number-bytes conversion
-----------------------
These codecs are "lossy" as they don't preserve prefixed padding zero bytes.
In a more mathematical sense,

    ``g(f(x))`` is **almost** an identity function, but not exactly.

where ``g`` is the decoder and ``f`` is a encoder.

.. autofunction:: bytes_to_uint
.. autofunction:: uint_to_bytes
"""


from __future__ import absolute_import
from __future__ import division

# pylint: disable-msg=R0801
try:  # pragma: no cover
	import psyco

	psyco.full()
except ImportError:  # pragma: no cover
	psyco = None
# pylint: enable-msg=R0801

import binascii
import struct

import mom_compat
import mom_builtin


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"

__all__ = [
	"bytes_to_uint",
	"uint_to_bytes",
]

ZERO_BYTE = mom_compat.ZERO_BYTE
EMPTY_BYTE = mom_compat.EMPTY_BYTE


def bytes_to_uint(raw_bytes):
	if not mom_builtin.is_bytes(raw_bytes):
		raise TypeError("argument must be raw bytes: got %r" %
		                type(raw_bytes).__name__)
		# binascii.b2a_hex is written in C as is int.
	return int(binascii.b2a_hex(raw_bytes), 16)


def uint_to_bytes(number, fill_size=0, chunk_size=0, overflow=False):
	if number < 0:
		raise ValueError("Number must be an unsigned integer: %d" % number)

	if fill_size and chunk_size:
		raise ValueError("You can either fill or pad chunks, but not both")

	# Ensure these are integers.
	_ = number & 1 and chunk_size & 1 and fill_size & 1

	raw_bytes = EMPTY_BYTE

	# Pack the integer one machine word at a time into bytes.
	num = number
	word_bits, _, max_uint, pack_type = mom_compat.get_word_alignment(num)
	pack_format = ">%s" % pack_type
	while num > 0:
		raw_bytes = struct.pack(pack_format, num & max_uint) + raw_bytes
		num >>= word_bits
		# Obtain the index of the first non-zero byte.
	zero_leading = mom_builtin.bytes_leading(raw_bytes)
	if number == 0:
		raw_bytes = ZERO_BYTE
		# De-padding.
	raw_bytes = raw_bytes[zero_leading:]

	length = len(raw_bytes)
	if fill_size > 0:
		if not overflow and length > fill_size:
			raise OverflowError("Need %d bytes for number, but fill size is %d" %
			                    (length, fill_size))
		raw_bytes = raw_bytes.rjust(fill_size, ZERO_BYTE)
	elif chunk_size > 0:
		remainder = length % chunk_size
		if remainder:
			padding_size = chunk_size - remainder
			raw_bytes = raw_bytes.rjust(length + padding_size, ZERO_BYTE)
	return raw_bytes
