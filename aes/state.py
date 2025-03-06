from typing import List

from aes.helpers import *
from aes.mix_columns import field_matrix_multiple


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

    def sub_bytes(self) -> 'AESState':
        self.data = bytes([SUB_WORD_MAPPING[d] for d in self.data])
        return self

    def revert_sub_bytes(self):
        self.data = bytes([SUB_WORD_MAPPING_REVERSE[d] for d in self.data])
        return self

    def shift_rows(self, reverse: bool = False) -> 'AESState':
        new_rows = []
        for i in range(4):
            row = self.get_row(i)
            if reverse:
                i = -i
            new_rows.append(rot_word(row, i))

        self._reset_by_rows(new_rows)
        return self

    def _reset_by_rows(self, rows: List[bytes]):
        assert len(rows) == 4
        self.data = bytes([rows[i % 4][i // 4] for i in range(16)])

    def _reset_by_columns(self, columns: List[bytes]):
        self.data = b''.join(columns)
        assert len(self.data) == 16

    def _matrix_multiply(self, matrix):
        columns = []

        for i in range(4):
            col = self.get_column(i)
            columns.append(field_matrix_multiple(matrix, col))

        self._reset_by_columns(columns)

    def mix_columns(self) -> 'AESState':
        matrix = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2],
        ]
        self._matrix_multiply(matrix)
        return self

    def revert_mix_columns(self):
        matrix = [
            [14, 11, 13, 9],
            [9, 14, 11, 13],
            [13, 9, 14, 11],
            [11, 13, 9, 14],
        ]
        self._matrix_multiply(matrix)
        return self

    def add_round_key(self, key: bytes) -> 'AESState':
        self.data = xor(self.data, key)
        return self

    def hex(self):
        return self.data.hex()
