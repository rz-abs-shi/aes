from unittest import TestCase

from encryption import encrypt, decrypt
from state import AESState


class TestEncryption(TestCase):

    def test_encryption(self):
        msg = 'theblockbreakers'.encode()
        key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')

        encrypted_msg = encrypt(key=key, msg=msg)

        self.assertEqual(
            encrypted_msg.hex(),
            'c69f25d0025a9ef32393f63e2f05b747'
        )

        self.assertEqual(
            decrypt(key=key, msg_encrypted=encrypted_msg),
            msg
        )

        msg = 'Nice work reza!!'.encode()
        self.assertEqual(decrypt(key=key, msg_encrypted=encrypt(key=key, msg=msg)), msg)


