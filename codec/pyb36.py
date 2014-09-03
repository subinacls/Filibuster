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

""":synopsis: Base-36 codec.
:module: mom.codec.base36

.. autofunction:: b36encode
.. autofunction:: b36decode

"""

from __future__ import absolute_import

# pylint: disable-msg=R0801
try:  # pragma: no cover
	import psyco

	psyco.full()
except ImportError:  # pragma: no cover
	psyco = None
# pylint: enable-msg=R0801

import mom_compat
import mom_builtin
import mom_string
import mom_base


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"

EMPTY_BYTE = mom_compat.EMPTY_BYTE

# Follows ASCII order.
ASCII36_BYTES = (mom_string.DIGITS +
                 mom_string.ASCII_UPPERCASE).encode("ascii")
# Therefore, b"1" represents b"\0".
if mom_compat.HAVE_PYTHON3:
	ASCII36_BYTES = tuple(mom_builtin.byte(x) for x in ASCII36_BYTES)


def b36encode(raw_bytes, base_bytes=ASCII36_BYTES, _padding=True):
	return mom_base.base_encode(raw_bytes, 36, base_bytes, base_bytes[0], _padding)


def b36decode(encoded, base_bytes=ASCII36_BYTES):
	encoded = EMPTY_BYTE.join(encoded.split())
	return mom_base.uint_to_base256(int(encoded, 36), encoded, base_bytes[0])
