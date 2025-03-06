from typing import List

from helpers import *


class AESState:
    def __init__(self, data: bytes):
        assert len(data) == 16

        self.data = data

    @classmethod
    def from_str(cls, text: str) -> 'AESState':
        return AESState(bytes(text, 'utf-8'))

    def __repr__(self):
        print('State:')
        rows = []
        for i in range(4):
            for j in range(4):
                rows.append(format(self.get_byte(i, j), '02x') + ' ')

            rows.append('\n')

        return ''.join(rows)

    def get_byte(self, i, j) -> int:
        assert 0 <= i < 4
        assert 0 <= j < 4

        return self.data[i + j * 4]

    def get_row(self, i) -> bytes:
        return bytes([self.get_byte(i, j) for j in range(4)])

    def get_column(self, i) -> bytes:
        return self.data[i * 4: i * 4 + 4]

    def sub_bytes(self):
        self.data = bytes([SUB_WORD_MAPPING[d] for d in self.data])

    def shift_rows(self):
        new_rows = []
        for i in range(4):
            row = self.get_row(i)
            new_rows.append(rot_word(row, i))

        self.data = bytes([new_rows[i % 4][i // 4] for i in range(16)])
