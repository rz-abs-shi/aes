from unittest import TestCase

from encryption import encrypt
from state import AESState


class TestEncryption(TestCase):

    def test_encryption(self):
        self.assertEqual(
            encrypt(key='2b7e151628aed2a6abf7158809cf4f3c', msg='theblockbreakers').hex(),
            'c69f25d0025a9ef32393f63e2f05b747'
        )
