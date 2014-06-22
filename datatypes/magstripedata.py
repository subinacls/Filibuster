#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information

I needed a way to make some test data for MagStrip - this is not formatted correctly needs help

    Track 1:
        Start sentinel — one character (generally '%')
        Format code="B" — one character (alpha only)
        Primary account number (PAN) — up to 19 characters. Usually, but not always, matches the credit card number printed on the front of the card.
        Field Separator — one character (generally '^')
        Name — two to 26 characters
        Field Separator — one character (generally '^')
        Expiration date — four characters in the form YYMM.
        Service code — three characters
        Discretionary data —
            may include Pin Verification Key Indicator (PVKI, 1 character),
            PIN Verification Value (PVV, 4 characters),
            Card Verification Value or Card Verification Code (CVV or CVC, 3 characters)
        End sentinel — one character (generally '?')
        Longitudinal redundancy check (LRC) — it is one character and a validity character calculated from other data on the track.

    Track 2:
        This format was developed by the banking industry (ABA).
        This track is written with a 5-bit scheme (4 data bits + 1 parity),
        which allows for sixteen possible characters,
        which are the numbers 0-9, plus the six characters  : ; < = > ? .
        The selection of six punctuation symbols may seem odd,
        but in fact the sixteen codes simply map to the ASCII range 0x30
        through 0x3f, which defines ten digit characters plus those six symbols.
        Start sentinel — one character (generally ';')
        Primary account number (PAN) — up to 19 characters. Usually, but not always, matches the credit card number printed on the front of the card.
        Separator — one char (generally '=')
        Expiration date — four characters in the form YYMM.
        Service code — three digits. The first digit specifies the interchange rules, the second specifies authorisation processing and the
        third specifies the range of services
        Discretionary data — as in track one
        End sentinel — one character (generally '?')
        Longitudinal redundancy check (LRC) — it is one character and a validity character calculated from other data on the track.

    Most reader devices do not return this value when the card is swiped to the presentation layer,
        and use it only to verify the input internally to the reader. Service code values common in financial cards:

            First digit

            1: International interchange OK
            2: International interchange, use IC (chip) where feasible
            5: National interchange only except under bilateral agreement
            6: National interchange only except under bilateral agreement, use IC (chip) where feasible
            7: No interchange except under bilateral agreement (closed loop)
            9: Test

            Second digit

            0: Normal
            2: Contact issuer via online means
            4: Contact issuer via online means except under bilateral agreement

            Third digit

            0: No restrictions, PIN required
            1: No restrictions
            2: Goods and services only (no cash)
            3: ATM only, PIN required
            4: Cash only
            5: Goods and services only (no cash), PIN required
            6: No restrictions, use PIN where feasible
            7: Goods and services only (no cash), use PIN where feasible
"""

import random
import __builtin__

class magstripgen():

    def __init__(self):
        pass

    def makemagdata(self):
        newtrack = ""
        tlist = []

        # track: 1
        #    format: B
        st1sentinel = ["%"] # represents start of sentinel data section
        fcode = ["B"] # sets this track data type
        t1pan = ["0400000000000000","04000000000000000","040000000000000000","0400000000000000000"] # represents card number
        t1fsep = ["^"] # seperation character
        t1name = ["AB","Test User"] # card holders name
        t1expdate = ["0000","2011"] # expiration date
        t1scode = {"intr":["1","2","5","6","7","9"],"authp":["0","2","4"],"rserv":["0","1","2","3","4","5","6","7"]} # service code
        t1disdata = {"pvki": ["A","4"],"pvv": ["1234","4321"],"cvv": ["123","456"]} # discretionary data
        et1sentinel = ["?"] # represents stop of sentinel data section
        t1lrc = ["5"] # not real of course

        # track 2:
        #
        st2sentinel = [";"]
        t2pan = list(t1pan)
        t2fsep = ["="]
        t2expdata = list(t1expdate)
        t2scode = dict(t1scode)
        t2disdata = dict(t1disdata)
        et2sentinel = list(et1sentinel)
        t2lrc = list(t1lrc)
        tlist.append(random.choice(st1sentinel))
        tlist.append(random.choice(fcode))
        tlist.append(random.choice(t1pan))
        tlist.append(random.choice(t1fsep))
        tlist.append(random.choice(t1name))
        rexpd = random.choice(t1expdate)
        tlist.append(random.choice(rexpd))
        for t in t1scode.keys():
            tlist.append(random.choice(t1scode[t]))

        for d in t1disdata.keys():
            tlist.append(random.choice(t1disdata[d]))

        tlist.append(random.choice(et1sentinel))
        tlist.append(random.choice(t1lrc))
        tlist.append(random.choice(st2sentinel))
        tlist.append(random.choice(t2pan))
        tlist.append(random.choice(t2fsep))
        tlist.append(random.choice(rexpd))
        tlist.append(random.choice(t))
        tlist.append(random.choice(d))
        tlist.append(random.choice(et2sentinel))
        tlist.append(random.choice(t2lrc))

        __builtin__.savedtrack = newtrack.join(tlist)
        print savedtrack