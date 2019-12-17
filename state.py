#!usr/bin/en/python3
"""
author - Pritesh raj
coded on - 17th December 2019 at 10:30 AM
follow the instruction

"""

import chess


class State(object):
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bits according to the readme
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TODO: add neural network here
        return 1


if __name__ == '__main__':
    s = State()
    print(s.edges())