import importlib

class Encoder:
    def name(self):
        raise NotImplmentedError()

    def encode(self, game_state):
        raise NotImplmentedError()

    def encode_point(self, point):
        raise NotImplmentedError()

    def decode_point_index(self, index):
        raise NotImplmentedError()

    def num_points(self):
        raise NotImplmentedError()

    def shape(self):
        raise NotImplmentedError()


def get_encoder_by_name(name, board_size):
    if isinstance(board_size, int):
        board_size = (board_size, board_size)
    module = importlib.import_module('dlgo.encoders.' + name)
    constructor = getattr(module, 'create')
    return constructor(board_size)
