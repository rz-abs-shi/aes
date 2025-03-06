from unittest import TestCase

from state import AESState


class TestState(TestCase):

    def test_sub_bytes(self):
        msg = '000102030405060708090a0b0c0d0e0f'
        state = AESState(bytes.fromhex(msg))
        self.assertEqual(state.data.hex(), '000102030405060708090a0b0c0d0e0f')

        # state.sub_bytes()
        # print(state)
        #
        # state.shift_rows()
        # print(state)
        #
        # state.mix_columns()
        # print(state)
