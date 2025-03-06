from unittest import TestCase

from aes.state import AESState


class TestState(TestCase):

    def test_state(self):
        msg = '000102030405060708090a0b0c0d0e0f'
        state = AESState(bytes.fromhex(msg))
        self.assertEqual(state.hex(), '000102030405060708090a0b0c0d0e0f')

        self.assertEqual(state.sub_bytes().hex(), '637c777bf26b6fc53001672bfed7ab76')
        self.assertEqual(state.revert_sub_bytes().hex(), '000102030405060708090a0b0c0d0e0f')

        self.assertEqual(state.shift_rows().hex(), '00050a0f04090e03080d02070c01060b')
        self.assertEqual(state.shift_rows(reverse=True).hex(), '000102030405060708090a0b0c0d0e0f')
