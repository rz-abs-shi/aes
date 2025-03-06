from key_expansion import expand_key, hex_key_to_bytes
from state import AESState


def encrypt(key: str, msg: str) -> bytes:
    keys = expand_key(bytes.fromhex(key))
    state = AESState.from_str(msg)

    # pre-whitening
    state.add_round_key(keys[0])

    # rounds
    for key in keys[1: 10]:
        state.sub_bytes().shift_rows().mix_columns().add_round_key(key)

    # final round
    state.sub_bytes().shift_rows().add_round_key(keys[10])

    print(state)
    return state.data


def decrypt(key: str, msg_encrypted: str):
    keys = expand_key(bytes.fromhex(key))
    state = AESState.from_str(msg_encrypted)

    state.add_round_key(keys[10])

