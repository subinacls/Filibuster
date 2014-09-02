#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#
from Crypto.Cipher import AES
import __builtin__
import os
import time
import base64

class encryptor(object):

	def __init__(self):
		pass

	def encrypt(self, sident):
		BLOCK_SIZE = 16  # highest setting for AES
		PADDING = '}'  # padding to keep blocksize true
		pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING  # pads data string as needed
		EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
		secret = 'E"h|X.yvTl8~5EYPg^bO4>1cn\KJeAOl'
		cipher = AES.new(secret)  # create a cipher object using the random secret
		time.sleep(3)
		return EncodeAES(cipher, sident)  # encode a string

	def decrypt(self, dedata):
		PADDING = '}'  # padding to keep blocksize true
		DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)  # check for base64 and then decode
		secret = 'E"h|X.yvTl8~5EYPg^bO4>1cn\KJeAOl'
		cipher = AES.new(secret)  # create a cipher object using the random secret
		time.sleep(0)
		return DecodeAES(cipher, dedata)  # decode the encoded string
