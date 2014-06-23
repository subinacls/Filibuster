#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information

I needed a way to make some test data for MagStrip - this is not formatted correctly needs help

	Well, there's three tracks (ISO 3554), all 0.110" wide.
	The top one is 210 BPI and has 7 bits per chr. (incl. parity). Total 79 alpha-num. chrs.
	The second track has 75 BPI, 5 bits per chr. (incl. par.) total 40 digits
	The third track has agian 210 BPI, 5 bits per chr (yeah incl. par.) total 107 digits.

Read more at: http://www.epanorama.net/documents/smartcard/magcard.html

	VISA ATM example:


		Track 1:
				%B1234567890123445^PADILLA/L.                ^99011200000000000000**XXX******?*
				^^^               ^^                         ^^   ^       ^         ^        ^^
				|||_ Card number  ||_ Card holder            ||   |       |         |_ CVV** ||_ LRC
				||_ Format code   |_ Field separator         ||   |       |                  |_ End sentinel
				|_ Start sentinel           Field separator _||   |       |_ Discretionary data
				                                  Expiration _|   |_ Service code

		Track 2:
				;1234567890123445=99011200XXXX00000000?*
				^^               ^^   ^   ^           ^^
				||_ Card number  ||   |   |_ Encrypted||_ LRC
				|_ Start sentinel||   |      PIN***   |_ End sentinel
				                 ||   |_ Service code
				Field separator _||_ Expiration

		Track 3:
				;011234567890123445=724724100000000000030300XXXX040400099010=************************==1=0000000000000000?*
				^^ ^               ^^  ^  ^            ^ ^  ^   ^^ ^   ^    ^^                       ^^^^^               ^^
				|| |               ||  |  |_ Currency  | |  |   || |   |    ||_ First subsidiary     |||||_ Additional   ||
				|| |               ||  |     exponent  | |  |   || |   |    |   account number (FSAN)||||   data         ||
				|| |_ Card number  ||  |_ Currency     | |  |   || |   |    |_ Field separator       ||||_ Field         ||_ LRC
				||_ Format code    ||     (Peseta)     | |  |   || |   |_ Expiration                 |||   separator     |_ End sentinel
				|_ Start sentinel  ||_ Country (Spain) | |  |   || |_ FSAN service restriction       |||_ Relay marker
				                   |_ Field separator  | |  |   ||_ PAN service restriction          ||_ Field separator
				                         Cycle length _| |  |   |_ Interchange control               |_ Field separator
				                            Retry count _|  |_ Encrypted PIN***

		%B1234567890123445^PADILLA/L.                ^99011200000000000000**XXX******?*
		;1234567890123445=99011200XXXX00000000?*
		;011234567890123445=724724100000000000030300XXXX040400099010=************************==1=0000000000000000?*

	VISA ELECT CARD:


		Track 1:
				%B1234567890123445^PADILLA/L.                ^99011X100000*000000000XXX000000?*
				^^^               ^^                         ^^   ^       ^         ^        ^^
				|||_ Card number  ||_ Card holder            ||   |       |         |_ CVV   ||_ LRC
				||_ Format code   |_ Field separator         ||   |       |                  |_ End sentinel
				|_ Start sentinel           Field separator _||   |       |_ Discretionary data
				                                  Expiration _|   |_ Service code: 101 for VISA and 121 for VISA Electron

		Track 2:
				;1234567890123445=99011X10XXXXXXX00000?*
				^^               ^^   ^   ^   ^       ^^
				||_ Card number  ||   |   |   |_ CVV  ||_ LRC
				|_ Start sentinel||   |   |           |_ End sentinel
				Field separator _||   |   |_ Encrypted PIN (except if duplicate card)
				      Expiration _|   |_ Service code: 101 for VISA and 121 for VISA Electron

		Track 3:
				;011234567890123445=724724000000000****00300XXXX020200099010=********************==1=100000000000000000**?*
				^^ ^               ^^  ^           ^     ^  ^   ^^ ^   ^    ^^                   ^^^^^                   ^^
				|| |               ||  |_ Currency |     |  |   || |   |    ||_ FSAN             |||||                   ||
				|| |_ Card number  ||     (Peseta) |     |  |   || |   |    |_ Field separator   |||||_ Additional data  ||_ LRC
				||_ Format code    ||_ Country     |     |  |   || |   |_ Expiration             ||||_ Field separator   |_ End sentinel
				|_ Start sentinel  |   (Spain)     |     |  |   || |_ FSAN service restriction   |||_ Relay marker
				                   |_ Field        |     |  |   ||_ PAN service restriction      ||_ Field separator
				                      separator    |     |  |   |_ Interchange control           |_ Field separator
				                    Validity date _|     |  |_ Encrypted PIN (except if duplicate card)
				              (except if duplicate card) |_ Retry count

		%B1234567890123445^PADILLA/L.                ^99011X100000*000000000XXX000000?*
		;1234567890123445=99011X10XXXXXXX00000?*
		;011234567890123445=724724000000000****00300XXXX020200099010=********************==1=100000000000000000**?*

	VISA ELECT CARD:


		Track 1:
				%B1234567890123445^PADILLA/L.                ^99011X100000*000000000XXX000000?*
				^^^               ^^                         ^^   ^       ^         ^        ^^
				|||_ Card number  ||_ Card holder            ||   |       |         |_ CVV   ||_ LRC
				||_ Format code   |_ Field separator         ||   |       |                  |_ End sentinel
				|_ Start sentinel           Field separator _||   |       |_ Discretionary data
				                                  Expiration _|   |_ Service code: 101 for VISA and 121 for VISA Electron

		Track 2:
				;1234567890123445=99011X10XXXXXXX00000?*
				^^               ^^   ^   ^   ^       ^^
				||_ Card number  ||   |   |   |_ CVV  ||_ LRC
				|_ Start sentinel||   |   |           |_ End sentinel
				Field separator _||   |   |_ Encrypted PIN (except if duplicate card)
				      Expiration _|   |_ Service code: 101 for VISA and 121 for VISA Electron

		Track 3:
				;011234567890123445=724724000000000****00300XXXX020200099010=********************==1=100000000000000000**?*
				^^ ^               ^^  ^           ^     ^  ^   ^^ ^   ^    ^^                   ^^^^^                   ^^
				|| |               ||  |_ Currency |     |  |   || |   |    ||_ FSAN             |||||                   ||
				|| |_ Card number  ||     (Peseta) |     |  |   || |   |    |_ Field separator   |||||_ Additional data  ||_ LRC
				||_ Format code    ||_ Country     |     |  |   || |   |_ Expiration             ||||_ Field separator   |_ End sentinel
				|_ Start sentinel  |   (Spain)     |     |  |   || |_ FSAN service restriction   |||_ Relay marker
				                   |_ Field        |     |  |   ||_ PAN service restriction      ||_ Field separator
				                      separator    |     |  |   |_ Interchange control           |_ Field separator
				                    Validity date _|     |  |_ Encrypted PIN (except if duplicate card)
				              (except if duplicate card) |_ Retry count

		%B1234567890123445^PADILLA/L.                ^99011X100000*000000000XXX000000?*
		;1234567890123445=99011X10XXXXXXX00000?*
		;011234567890123445=724724000000000****00300XXXX020200099010=********************==1=100000000000000000**?*

	MasterCard:


		Track 1:
				%B1234567890123445^PADILLA/L.                ^99011211XXXX*000000**0XXX0**000?*
				^^^               ^^                         ^^   ^  ^^   ^         ^        ^^
				|||_ Card number  ||_ Card holder            ||   |  ||   |_ Discr. |_ CVV   ||_ LRC
				||_ Format code   |_ Field separator         ||   |  ||      data            |_ End sentinel
				|_ Start sentinel           Field separator _||   |  ||_ PVV*
				                                  Expiration _|   |  |_ PVV key indicator
				                                                  |_ Service code

		Track 2:
				;1234567890123445=99011211XXXXXXX00***?*
				^^               ^^   ^  ^^   ^       ^^
				||_ Card number  ||   |  ||   |_ CVV  ||_ LRC
				|_ Start sentinel||   |  ||_ PVV*     |_ End sentinel
				Field separator _||   |  |_ PVV key indicator
				      Expiration _|   |_ Service code

		Track 3:
				;011234567890123445=000978100000000****8330*0000920000099010=************************==1=0000000*00000000?*
				^^ ^               ^   ^  ^        ^   ^ ^      ^^     ^    ^^                       ^^^^^               ^^
				|| |               |   |  |_ Curr. |   | |_Retry||     |    ||_ FSAN                 |||||_ Additional   ||_ LRC
				|| |_ Card number  | Curr.   expon.|   |   count||     |    |_ Field separator       ||||   data         |_ End sentinel
				||_ Format code    | (Euro)        |   |        ||     |_ Expiration                 ||||_ Field separator
				|_ Start sentinel  |_ Field        |   |_ Cycle ||_ PAN service restriction          |||_ Relay marker
				                      separator    |      length|_ Interchange control               ||_ Field separator
				                    Validity date _|                                                 |_ Field separator

		%B1234567890123445^PADILLA/L.                ^99011211XXXX*000000**0XXX0**000?*
		;1234567890123445=99011211XXXXXXX00***?*
		;011234567890123445=000978100000000****8330*0000920000099010=************************==1=0000000*00000000?*

	MasterCard:

		Track 1:
				%B1234567890123445^PADILLA/L.                ^990110100000000XXX****XXX******?*
				^^^               ^^                         ^^   ^       ^  ^      ^        ^^
				|||_ Card number  ||_ Card holder            ||   |       |  |      |_ CVV   ||_ LRC
				||_ Format code   |_ Field separator         ||   |       |  |_ Number       |_ End sentinel
				|_ Start sentinel           Field separator _||   |       |_ Discretionary data
				                                  Expiration _|   |_ Service code

		Track 2:
				;1234567890123445=990110100000XXXXXX00?*
				^^               ^^   ^       ^  ^    ^^
				||_ Card number  ||   |  CVV _|  |    ||_ LRC
				|_ Start sentinel||   |  Number _|    |_ End sentinel
				                 ||   |_ Service code
				Field separator _||_ Expiration

		Track 3:
				;011234567890123445=7247241000000000000001000000040400099010=************************==0=0002000000******?*
				^^ ^               ^^  ^  ^              ^      ^^ ^   ^    ^^                       ^^^^^               ^^
				|| |_ Card number  ||  |  |_ Currency    |      || |   |    ||_ First subsidiary     |||||_ Additional   ||
				||_ Format code    ||  |     exponent    |      || |   |    |   account number (FSAN)||||   data         ||
				|_ Start sentinel  ||  |_ Currency       |      || |   |    |_ Field separator       ||||_ Field         ||_ LRC
				  Field separator _||     (Peseta)       |      || |   |_ Expiration                 |||   separator     |_ End sentinel
				                    |_ Country (Spain)   |      || |_ FSAN service restriction       |||_ Relay marker
				                            Retry count _|      ||_ PAN service restriction          ||_ Field separator
				                                                |_ Interchange control               |_ Field separator

		%B1234567890123445^PADILLA/L.                ^990110100000000XXX****XXX******?*
		;1234567890123445=990110100000XXXXXX00?*
		;011234567890123445=7247241000000000000001000000040400099010=************************==0=0002000000******?*

	Social security card:


		Track 1:
				%B999999^PDVS123456789012^PADILLA L.                    ^0X0000399           ?*
				^^^     ^^^^^^           ^^                             ^ ^   ^              ^^
				|||     ||||||_ Card     ||_ Card holder                | |   |_ Expiration  ||_ LRC
				|||     |||||   number(2)|_ Field separator (formerly =)| |                  |_ End sentinel
				|||     |||||_ 3rd letter from 2nd surname              | |_ = 1 -> Non pensioner
				|||     ||||_ 1st letter from 2nd surname               |    = 2 -> Pensioner
				|||     |||_ 3rd letter from 1st surname                |_ Field separator (formerly =)
				|||     ||_ 1st letter from 1st surname
				|||     |_ Field separator (formerly =)
				|||_ Card number(1)
				||_ Format code
				|_ Start sentinel

		Track 2:
				;999999554749123456789012=00X990300000?*
				^^     ^  ^  ^           ^  ^^        ^^
				||     |  |  |_ Card     |  ||        ||_ LRC
				||     |  |     number(2)|  ||        |_ End sentinel
				||     |  |              |  ||_ Expiration
				||     |  |              |  |_ See above
				||     |  |              |_ Field separator
				||     |  |_ = 30 x (#V - 30) + #S - 22, where #X means decimal value of character X in the ALPHA format (#A = 33, #B = 34, ...)
				||     |_ = 30 x (#P - 30) + #D - 22, where P, D, V and S come from the card number (see above)
				||_ Card number(1)
				|_ Start sentinel

		%B999999^PDVS123456789012^PADILLA L.                    ^0X0000399           ?*
		;999999554749123456789012=00X990300000?*

"""

import sys
import random
import __builtin__

class magstripgen():

    def __init__(self):
        pass

    def encode(self, s):
        """Read in K=4 bits at a time and write out those plus parity bits"""
        while len(s) >= K:
            nybble = s[0:K]
            sys.stdout.write(self.hamming(nybble))
            s = s[K:]

    def hamming(self, bits):
        """Return given 4 bits plus parity bits for bits (1,2,3), (2,3,4) and (1,3,4)"""
        t1 = self.parity(bits, [0,1,2])
        t2 = self.parity(bits, [1,2,3])
        t3 = self.parity(bits, [0,2,3])
        return bits + t1 + t2 + t3

    def parity(self, s, indicies):
        """Compute the parity bit for the given string s and indicies"""
        sub = ""
        for i in indicies:
            sub += s[i]
        return str(str.count(sub, "1") % 2)

    def makemagdata(self):

        newtrack = ""
        t1track = ""
        tlist = []
        t1list = []
        t2track = ""
        t2list = []

        # track: 1
        #    format: B
        st1sentinel = ["%"] # represents start of sentinel data section
        fcode = ["B"] # sets this track data type
        t1pan = ["1234567890123456","9988776655443322","1212232323434345454","9999888877776666"] # represents card number
        t1fsep = ["^"] # seperation character
        t1name = ["Test User Mr "] # card holders name
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
        et2sentinel = list(et1sentinel)
        t2lrc = list(t1lrc)
        __builtin__.K = 5
        t1list.append(random.choice(st1sentinel))
        t1list.append(random.choice(fcode))
        t1list.append(random.choice(t1pan))
        t1list.append(random.choice(t1fsep))
        t1list.append(random.choice(t1name))
        rexpd = random.choice(t1expdate)
        t1list.append(random.choice(rexpd))
        for t in t1scode.keys():
            t1list.append(random.choice(t1scode[t]))

        for d in t1disdata.keys():
            t1list.append(random.choice(t1disdata[d]))

        t1list.append(random.choice(et1sentinel))
        t1list.append(random.choice(t1lrc))
        tlist.append(self.encode(t1track.join(t1list)))

        __builtin__.K = 4

        t2list.append(random.choice(st2sentinel))
        t2list.append(random.choice(t2pan))
        t2list.append(random.choice(t2fsep))
        t2list.append(random.choice(rexpd))
        t2list.append(random.choice(t))
        t2list.append(random.choice(d))
        t2list.append(random.choice(et2sentinel))
        t2list.append(random.choice(t2lrc))
        tlist.append(self.encode(t2track.join(t2list)))

        try:
            __builtin__.savedtrack = newtrack.join(tlist)
            return savedtrack+"\n"
        except:
            pass
