import torch
from state import State


if __name__ == '__main__':
    model = torch.load('nets/value.pth', map_location=lambda storage, loc:storage)
    s = State()
    output = model(s.serialize())
    print(output)