

class AESState:

    def __init__(self, data: bytes):
        assert len(data) == 16
        self.data = data

    @classmethod
    def from_str(cls, text: str) -> 'AESState':
        return AESState(bytes(text, 'utf-8'))

    def __repr__(self):
        d = self.data.hex()
        rows = []
        for i in range(4):
            for j in range(4):
                ind = j * 4 + i
                rows.append(d[ind * 2: ind * 2 + 2] + ' ')

            if i != 3:
                rows.append('\n')

        return ''.join(rows)
