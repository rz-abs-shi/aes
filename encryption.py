from key_expansion import expand_key, hex_key_to_bytes
from state import AESState


def encrypt(key: bytes, msg: bytes) -> bytes:
    keys = expand_key(key)
    state = AESState(msg)

    # pre-whitening
    state.add_round_key(keys[0])

    # rounds
    for key in keys[1: 10]:
        state.sub_bytes().shift_rows().mix_columns().add_round_key(key)

    # final round
    state.sub_bytes().shift_rows().add_round_key(keys[10])

    return state.data


def decrypt(key: bytes, msg_encrypted: bytes) -> bytes:
    keys = expand_key(key)
    state = AESState(msg_encrypted)

    state.add_round_key(keys[10]).shift_rows(reverse=True).revert_sub_bytes()

    for key in keys[9:0:-1]:
        state.add_round_key(key).revert_mix_columns().shift_rows(reverse=True).revert_sub_bytes()

    state.add_round_key(keys[0])
    return state.data
