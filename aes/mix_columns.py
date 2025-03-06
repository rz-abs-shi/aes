from typing import List

from .helpers import xor
from .mix_columns_mapping import MULTIPLICATION_MAPPING


def field_matrix_multiple(matrix: List[List[int]], word: bytes) -> bytes:
    new_word_bytes = []

    for row in matrix:
        new_byte = bytes(1)
        for i in range(len(row)):
            multiplier = row[i]
            if multiplier == 1:
                byte = word[i]
            else:
                byte = MULTIPLICATION_MAPPING[multiplier][word[i]]
            new_byte = xor(new_byte, byte.to_bytes(1, 'big'))

        new_word_bytes.append(new_byte)

    return b''.join(new_word_bytes)
