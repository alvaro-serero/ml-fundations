"""Save and Load Model Weights with state_dict"""

import io
import torch
import torch.nn as nn

def copy_weights(src: nn.Module, dst: nn.Module) -> nn.Module:
    # TODO: serialize src's state dict into a buffer, rewind, then load it into dst

    # Create buffer
    buffer = io.BytesIO()

    # Get the state dict of src and serialize it into the buffer
    torch.save(src.state_dict(), buffer)

    # Rewind cursor to the start of the buffer
    buffer.seek(0)

    # Deserialize the state dict from the buffer
    loaded_state_dict = torch.load(buffer)

    # Load the state dict into dst
    dst.load_state_dict(loaded_state_dict)

    return dst


torch.manual_seed(0)
src = nn.Linear(3, 1)
torch.manual_seed(1)
dst = nn.Linear(3, 1)
print(torch.equal(src.weight, dst.weight))
copy_weights(src, dst)
print(torch.equal(src.weight, dst.weight))
print(torch.equal(src.bias, dst.bias))