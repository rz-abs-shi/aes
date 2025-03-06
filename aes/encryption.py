from .state import AESState
from .key_expansion import expand_key


class AESEncryption:
    def __init__(self, key: bytes, rounds: int = 10):
        self.rounds = rounds
        self.keys = expand_key(key, count=rounds)

    def encrypt(self, msg: bytes) -> bytes:
        state = AESState(msg)

        # pre-whitening
        state.add_round_key(self.keys[0])

        # rounds
        for key in self.keys[1: self.rounds]:
            state.sub_bytes().shift_rows().mix_columns().add_round_key(key)

        # final round
        state.sub_bytes().shift_rows().add_round_key(self.keys[self.rounds])

        return state.data

    def decrypt(self, msg_encrypted: bytes) -> bytes:
        state = AESState(msg_encrypted)

        state.add_round_key(self.keys[self.rounds]).shift_rows(reverse=True).revert_sub_bytes()

        for key in self.keys[self.rounds - 1:0:-1]:
            state.add_round_key(key).revert_mix_columns().shift_rows(reverse=True).revert_sub_bytes()

        state.add_round_key(self.keys[0])
        return state.data
