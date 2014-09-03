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

""":synopsis: Base-58 repr for unambiguous display & compact human-input.
:module: mom.codec.base58

Functions
---------
.. autofunction:: b58encode
.. autofunction:: b58decode
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
import mom_base


__author__ = "yesudeep@google.com (Yesudeep Mangalapilly)"


# Follows ASCII order.
ASCII58_BYTES = ("123456789"
                 "ABCDEFGHJKLMNPQRSTUVWXYZ"
                 "abcdefghijkmnopqrstuvwxyz").encode("ascii")
# Therefore, b"1" represents b"\0".
ASCII58_ORDS = dict((x, i) for i, x in enumerate(ASCII58_BYTES))

ALT58_BYTES = ("123456789"
               "abcdefghijkmnopqrstuvwxyz"
               "ABCDEFGHJKLMNPQRSTUVWXYZ").encode("ascii")
# Therefore, b"1" represents b"\0".
ALT58_ORDS = dict((x, i) for i, x in enumerate(ALT58_BYTES))

if mom_compat.HAVE_PYTHON3:
	ASCII58_BYTES = tuple(mom_builtin.byte(x) for x in ASCII58_BYTES)
	ALT58_BYTES = tuple(mom_builtin.byte(x) for x in ALT58_BYTES)

POW_58 = tuple(58 ** power for power in mom_builtin.range(512))


def b58encode(raw_bytes,
              base_bytes=ASCII58_BYTES, _padding=True):
	return mom_base.base_encode(raw_bytes, 58, base_bytes, base_bytes[0], _padding)


def b58decode(encoded,
              base_bytes=ASCII58_BYTES,
              base_ords=ASCII58_ORDS):
	return mom_base.base_decode(encoded, 58, base_ords, base_bytes[0], POW_58)
