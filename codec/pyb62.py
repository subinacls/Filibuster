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

""":synopsis: Base-62 7-bit ASCII-safe representation for compact human-input.
:module: mom.codec.base62

Functions
---------
.. autofunction:: b62encode
.. autofunction:: b62decode
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

import mom_compat
import mom_builtin
import mom_string
import mom_base


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"


# Follows ASCII order.
ASCII62_BYTES = (mom_string.DIGITS +
                 mom_string.ASCII_UPPERCASE +
                 mom_string.ASCII_LOWERCASE).encode("ascii")
# Therefore, b"0" represents b"\0".
ASCII62_ORDS = dict((x, i) for i, x in enumerate(ASCII62_BYTES))

ALT62_BYTES = (mom_string.DIGITS +
               mom_string.ASCII_LOWERCASE +
               mom_string.ASCII_UPPERCASE).encode("ascii")
# Therefore, b"0" represents b"\0".
ALT62_ORDS = dict((x, i) for i, x in enumerate(ALT62_BYTES))

if mom_compat.HAVE_PYTHON3:
	ASCII62_BYTES = tuple(mom_builtin.byte(x) for x in ASCII62_BYTES)
	ALT62_BYTES = tuple(mom_builtin.byte(x) for x in ALT62_BYTES)

POW_62 = tuple(62 ** power for power in range(512))


def b62encode(raw_bytes,
              base_bytes=ASCII62_BYTES,
              _padding=True):
	return mom_base.base_encode(raw_bytes, 62, base_bytes, base_bytes[0], _padding)


def b62decode(encoded,
              base_bytes=ASCII62_BYTES,
              base_ords=ASCII62_ORDS):
	return mom_base.base_decode(encoded, 62, base_ords, base_bytes[0], POW_62)
