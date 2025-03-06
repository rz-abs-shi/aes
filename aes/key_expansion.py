from typing import List
from .helpers import *


def hex_key_to_bytes(key: str) -> bytes:
    return bytes.fromhex(key)


def first_column_round_key(word1: bytes, word2: bytes, round_number: int) -> bytes:
    key1 = xor(word1, sub_word(rot_word(word2)))
    key2 = rcon(round_number)
    return xor(key1, key2)


def next_round_key(key: bytes, round_number: int) -> bytes:
    assert len(key) == 16, 'RSA key should be 128 bits'

    words = [key[:4], key[4:8], key[8: 12], key[12:]]
    words.append(first_column_round_key(words[0], words[3], round_number))

    for i in range(3):
        words.append(
            xor(words[-1], words[-4])
        )

    return b''.join(words[4:])


def expand_key(key: bytes, count: int = 10) -> List[bytes]:
    assert len(key) == 16, 'RSA key should be 128 bits'

    keys = [key]

    for i in range(count):
        keys.append(next_round_key(keys[-1], i + 1))

    return keys


def generate_keys(key: str):
    keys = expand_key(hex_key_to_bytes(key))

    print('\n'.join(map(lambda x: x.hex(), keys)))
