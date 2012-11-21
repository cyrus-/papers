import numpy as np
import ace.OpenCL.bindings as cl
from listing1 import map
from listing2 import add5

cl.ctx = cl.Context.for_device(0, 0)

input = np.ones((1024,))
d_in = cl.to_device(input)
d_out = cl.alloc(like=d_in)

map(d_in, d_out, add5, 
    global_size=d_in.shape, local_size=(128,))

out = cl.from_device(d_out)
assert (out == a + 5).all()
