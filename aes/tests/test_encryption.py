from unittest import TestCase

from aes.encryption import AESEncryption


class TestEncryption(TestCase):

    def test_encryption(self):
        msg = 'theblockbreakers'.encode()
        key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
        aes_encrypt = AESEncryption(key=key)

        encrypted_msg = aes_encrypt.encrypt(msg=msg)

        self.assertEqual(
            encrypted_msg.hex(),
            'c69f25d0025a9ef32393f63e2f05b747'
        )

        self.assertEqual(
            aes_encrypt.decrypt(msg_encrypted=encrypted_msg),
            msg
        )

        msg = 'Nice work reza!!'.encode()
        self.assertEqual(aes_encrypt.decrypt(aes_encrypt.encrypt(msg=msg)), msg)


