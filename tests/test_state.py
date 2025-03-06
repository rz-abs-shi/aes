from unittest import TestCase

from state import AESState


class TestState(TestCase):

    def test_state(self):
        msg = bytes.fromhex('000102030405060708090a0b0c0d0e0f')
        state = AESState(msg)
        print(state)
        print('Row 3', state.get_row(3).hex())
        print('Col 2', state.get_column(2).hex())

        state.sub_bytes()
        print(state)

        state.shift_rows()
        print(state)

